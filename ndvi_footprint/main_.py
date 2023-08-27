import os
import glob

import param
import pyproj
import requests
import rioxarray
import panel as pn
import numpy as np
import pandas as pd
import geoviews as gv
import geopandas as gpd
import cartopy.crs as ccrs
from shapely.geometry import Point, box, shape

pn.param.ParamMethod.loading_indicator = True
pn.extension()


class NAIPStructure(param.Parameterized):

    def __init__(self):
        self.data_dir = os.path.join(os.sep, "mnt", "perm", "San_Jose_CA_Cover_Areas")
        self.index_gdf = self.get_index()

        address = "200 Madrone Ave, Ben Lomond, CA 95005"
        self.address_input = pn.widgets.AutocompleteInput(
            name="Address", value=address,
            restrict=False, case_sensitive=False)
        self.address_input.param.watch(self.get_type_ahead, "value_input")
        self.alpha_input = pn.widgets.FloatSlider(name="Alpha", value=1, step=0.1)
        self.ndvi_average = pn.widgets.StaticText(name="NDVI Average")
        self.buffer_input = pn.widgets.DiscreteSlider(name="Buffer (ft)", options=[0, 5, 10, 30, 50])

        self.plot_pane = pn.panel(pn.bind(self.update_plot, self.address_input, self.buffer_input), sizing_mode="stretch_both")

        self.template = pn.template.VanillaTemplate()
        self.template.sidebar.extend([self.address_input, self.alpha_input, self.buffer_input.param.value_throttled, self.ndvi_average])
        self.template.main.extend([self.plot_pane])

    def read_xml(self, fp):
        with open(fp, "r") as f:
            lines = f.read().splitlines()

        points = {}
        append = False
        keywords = ["northBoundLatitude", "southBoundLatitude", "westBoundLongitude", "eastBoundLongitude"]

        for line in lines:
            if "<bounding>" in line or any(f"<gmd:{keyword}>" in line for keyword in keywords):
                append = True
                if "north" in line:
                    key = "ymax"
                elif "south" in line:
                    key = "ymin"
                elif "east" in line:
                    key = "xmax"
                elif "west" in line:
                    key = "xmin"
                continue
            elif "</bounding" in line:
                break
            elif any(f"</gmd:{keyword}>" in line for keyword in keywords):
                continue
            elif append:
                try:
                    point = float(line.split(">")[1].split("<")[0])
                    points[key] = point
                except ValueError:
                    break
        return box(points["xmin"], points["ymin"], points["xmax"], points["ymax"])

    def get_index(self):
        gdf_list = []
        for i, fp in enumerate(glob.glob(os.path.join(self.data_dir, "*.xml"))):
            geom = self.read_xml(fp)
            _, id_, quadrant, _, _, date = os.path.basename(fp.split(".")[0]).split("_")
            gdf = gpd.GeoDataFrame({"id": id_, "quadrant": quadrant}, geometry=[geom], index=[i])
            gdf_list.append(gdf)
        gdf = pd.concat(gdf_list)
        return gdf

    def get_type_ahead(self, address):
        base_url = "http://pxpoint-dev-cluster.corelogicspatial.com/GetAddressTypeahead"
        headers = {'Content-Type': 'application/json'}

        # less strict on input
        json = {
            "options": {
                "enableCache": False,
                "numReturns": 5
            },
            "search": f"{address}",
            "typeaheadDataset": "parcel_us_atx"
        }

        response = requests.post(base_url, headers=headers, json=json)
        content = response.json()["result"]
        matches = [match["match"] for match in content["matches"]]
        self.address_input.options = matches

    def get_location(self, address):
        base_url = "http://pxpoint-dev-cluster.corelogicspatial.com/GeocodeAddress"
        headers = {'Content-Type': 'application/json'}

        json = {
            "address": address,
            "output": {
                "addAttributes": {
                    "ANY": ["Geometry:GeoJSON"]
                }
            }
        }

        response = requests.post(base_url, headers=headers, json=json)
        content = response.json()["result"]
        lon = None
        lat = None
        coords = None
        for key, val in content.items():
            geo_data = val[0]
            lon = geo_data["Longitude"]
            lat = geo_data["Latitude"]
            coords = shape(geo_data["Geometry"])
            gdf = gpd.GeoDataFrame(geometry=[coords])
            break
        return lon, lat, gdf

    def to_cartopy(self, proj_crs):
        # IS THIS CORRECT? DOUBLE CHECK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        cart_crs = ccrs.epsg(proj_crs.to_epsg())
        return cart_crs

    def get_naip(self, gdf, lon, lat, buffer):
        point = Point(lon, lat)
        print(point)
        print(self.index_gdf)
        row = self.index_gdf.loc[
            self.index_gdf.intersects(point), ["id", "quadrant"]
        ]
        print(row)
        row = row.iloc[0]

        wild_fi = "*" + "_".join(row) + "*.tif"
        wild_fp = os.path.join(self.data_dir, wild_fi)
        print(wild_fp)
        jp2_fp = sorted(glob.glob(wild_fp))[0]

        ds = rioxarray.open_rasterio(jp2_fp)
        self.ds_crs = pyproj.CRS(ds["spatial_ref"].attrs["crs_wkt"])

        print(jp2_fp)
        gdf.crs = "epsg:4326"
        gdf_proj = gdf.to_crs("epsg:2249")
        gdf_proj["geometry"] = gdf_proj["geometry"].buffer(buffer)
        gdf_proj = gdf_proj.to_crs(self.ds_crs)
        ds = ds.rio.clip(gdf_proj["geometry"])

        ds = ds.where(np.isfinite(ds))
        print(ds)
        ds = (ds[3] - ds[0]) / (ds[3] + ds[0])
        return ds

    def update_plot(self, address, buffer):
        esri_tiles = gv.tile_sources.EsriImagery().opts(responsive=True, max_zoom=22)

        lon, lat, gdf = self.get_location(address)
        ds = self.get_naip(gdf, lon, lat, buffer)
        self.ndvi_average.value = f"{ds.mean().item():.2f}"
        if len(gdf) > 0:
            structure_polygons = gv.Polygons(gdf, crs=ccrs.PlateCarree()).opts(fill_alpha=0.2)
            ndvi_image = gv.Image(ds, ["x", "y"], crs=self.to_cartopy(self.ds_crs)).opts(
                cmap="BrBG", clim=(-1, 1), colorbar=True
            ).apply.opts(
                alpha=self.alpha_input.param.value
            )
            plot_overlay = (esri_tiles * structure_polygons * ndvi_image).opts(responsive=True)
            self.plot_overlay = plot_overlay
            return plot_overlay
        else:
            return self.plot_overlay

    def view(self):
        return self.template

naip_structure = NAIPStructure().view()
naip_structure.servable()
