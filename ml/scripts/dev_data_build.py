import geopandas as gpd
import requests
import os
from joblib import Parallel,delayed

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define variables and environments
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

zipSHP   = r'D:\Projects\Github\SAGIS-Users\anderso\FirebreakEnhancement\data\Labels_Merge.zip'
save_dir = r'D:\Projects\WORKING\ML\imagery\label_names'

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Define functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

def get_save_url(x):
    url = """https://gis.apfo.usda.gov/arcgis/services/NAIP/USDA_CONUS_PRIME/ImageServer/WMSServer?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={}&CRS=EPSG:4326&WIDTH=256&HEIGHT=256&LAYERS=0&STYLES=&FORMAT=image/jpeg&DPI=96&MAP_RESOLUTION=96&FORMAT_OPTIONS=dpi:96&TRANSPARENT=TRUE"""
    #print(url.format(','.join([str(val) for val in [x[1],x[0],x[3],x[2]]])))
    return url.format(','.join([str(val) for val in [x[1],x[0],x[3],x[2]]]))

def save_data(url,path):
    res = requests.get(url)
    with open(path,'wb') as f:
        f.write(res.content)
    return res.status_code

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
# ================================#
# Call Functions
# ================================#
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

# Read the zipped shapefile
gpRead = gpd.read_file(zipSHP)

print('Total feature count: {0}'.format(len(gpRead)))

# Query for just one label class
gdfQuery = gpRead[gpRead['BREAK_NAME']=='Agriculture']

print('{0} features found'.format(len(gdfQuery)))

# Create a geodataframe fo the selected data
gdf = gpd.GeoDataFrame(gdfQuery, geometry='geometry')

# Define the bounds from the geometry field of the dataframe
gdf['bounds'] = gdf['geometry'].apply(lambda x: x.bounds)

# Create an output folder for saving images
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Create a labeled output folder for each label class
for label_name in gdf['BREAK_NAME'].str.lower().str.replace(' ', '_').str.replace('-', '_').unique():
    print('Creating Directory for: {0}'.format(label_name))
    if not os.path.exists(os.path.join(save_dir, label_name)):
        os.makedirs(os.path.join(save_dir, label_name))

# Add a field to gdf for the jpg save location
gdf['file_save'] = gdf.apply(lambda row: os.path.join(save_dir + '\\',row['BREAK_NAME'].lower().replace(' ','_').replace('-','_') + '\\' + str(row['ID'])+'.jpg'),axis=1)

#print(gdf['file_save'])
print(gdf['file_save'][75])

# Add a field to gdf for the constructed url request
gdf['url'] = gdf['bounds'].apply(get_save_url)

#print(gdf['url'])
print(gdf['url'][75])

# Create a list of grid url locations and save locations
url_list = gdf['url'].tolist()
save_list = gdf['file_save'].tolist()

#print(url_list)
#print(save_list)

#status_codes = Parallel(n_jobs=10,backend='threading')(delayed(save_data)(url=url,path=path) for url,path in zip(url_list,save_list))
#status_codes = Parallel(n_jobs=10,backend='threading')(delayed(save_data)(url=url,path=path) for url,path in zip(url_list,save_list))

