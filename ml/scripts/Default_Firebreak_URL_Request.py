import os
import logging
import geopandas as gpd
import requests
from pyproj import Transformer
from datetime import datetime as dt

# Create Logger
logFile = os.path.dirname(os.path.abspath(__file__)) + os.sep + "NAIPtoImageAZ.log"
logging.basicConfig(filename=logFile, filemode='a', level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logger = logging.getLogger()
logger.info("Logging has been initiated")

# Define local variables

# Input shapefile
zipSHP = r'B:\projects\FirebreakML\Firebreak_Water_Wildland\vector\National_WW\AZ_WW_Merge.zip'
logger.info(f'Input data: {zipSHP}')

# Create the output save location for NAIP image tiles
save_dir = r'B:/projects/FirebreakML/Firebreak_Water_Wildland/imagery/AZ_Water_Wildland'
logger.info(f'Output Image Directory: {save_dir}')

# Define a transformer for Decimal Degrees to Meters-UTM (required for url request)
proj = Transformer.from_crs(4326, 3857, always_xy=True)

# Define Functions

# Function to convert Decimal Degrees bbox to Meters-utm
def get_meters(x):
    x_min,y_min,x_max,y_max = x[0],x[1],x[2],x[3]
    ll   = proj.transform(x_min,y_min)
    ur   = proj.transform(x_max,y_max)
    bbox = ll + ur
    return(bbox)

# Define function for crafting the url request from bound box field
def get_save_url(x):
    url = """https://gis.apfo.usda.gov/arcgis/services/NAIP/USDA_CONUS_PRIME/ImageServer/WMSServer?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={}&CRS=EPSG:3857&WIDTH=256&HEIGHT=256&LAYERS=0&STYLES=&FORMAT=image/jpeg&DPI=96&MAP_RESOLUTION=96&FORMAT_OPTIONS=dpi:96&TRANSPARENT=TRUE"""
    return url.format(','.join([str(val) for val in [x[0],x[1],x[2],x[3]]]))

# Function to write the url path and the output path to a list
def save_data(url,path):
    res = requests.get(url)
    #res = requests.get(url, auth=HTTPBasicAuth('andolson@corelogic.com', '5p4rkl3p0ny#M'))
    with open(path,'wb') as f:
        f.write(res.content)
    #return res.status_code

# Function to return zip list of URL call and output jpg save file location
def get_url_call_and_output_location(zippedShapefile):

    # Read the zipped shapefile with geopandas
    gpRead = gpd.read_file(zippedShapefile)

    # Query select only Wildland and Water in shapefile
    gdfQuery = gpRead[gpRead['BREAK_NAME'].isin(['Wildland','Water'])]

    # Create geodataframe and add geometry field
    gdf = gpd.GeoDataFrame(gdfQuery, geometry='geometry')

    # Populate a 'bounds' field with the geometry field
    gdf['bounds'] = gdf['geometry'].apply(lambda x: x.bounds)
    logger.info(f'Bounds Field Calculated')

    # Populate a new field with the bounding box defined in Meters-UTM
    gdf['bounds_m'] = gdf['bounds'].apply(get_meters)
    logger.info(f'Bounds Meters-UTM Field Calculated')

    # Add a field to dataframe for the output location of the NAIP tiles
    gdf['file_save'] = gdf.apply(lambda row: os.path.join(save_dir + '/',row['BREAK_NAME'].lower().replace(' ','_').replace('-','_') + '/' + str(row['ID'])+'.jpg'),axis=1)
    logger.info(f'File Save Location Field Calculated')

    # Populate 'url' field in dataframe with the correct url path using bounding box
    gdf['url'] = gdf['bounds_m'].apply(get_save_url)
    logger.info('URL Field Calculated')

    # Call function to write lists
    url_list  = gdf['url'].tolist()
    save_list = gdf['file_save'].tolist()

    logger.info(f'Number of URL calls: {len(url_list)}')

    # Create ouput zip list of http request and jpg file save info
    newlst = zip(url_list, save_list)

    return newlst

# Call functions

# Start a timer
startTime = dt.now()

# Call function to start jpg downloads using grids from zipped shp
UrlAndOuputJpg = get_url_call_and_output_location(zipSHP)

logger.info("Complete! Total runtime: {0}".format(dt.now() - startTime))