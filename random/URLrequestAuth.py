import geopandas as gpd
import requests
from requests.auth import HTTPBasicAuth
import os
from joblib import Parallel,delayed
import time

start_time = time.perf_counter()

# Input shapefile
zipSHP = r'D:\Projects\WORKING\ML\imagery\maxartest\testSHP.zip'

# Read the zipped shapefile with geopandas
gpRead = gpd.read_file(zipSHP)

# Create geodataframe and add geometry field
gdf = gpd.GeoDataFrame(gpRead, geometry='geometry')

# Populate a 'bounds' field with the geometry field
gdf['bounds'] = gdf['geometry'].apply(lambda x: x.bounds)
print(f'Bounds Field Calculated')

def get_bbox(x):
    x_min,y_min,x_max,y_max = x[0],x[1],x[2],x[3]
    ll   = x_min,y_min
    ur   = x_max,y_max
    bbox = ll + ur
    return(bbox)

# Create the output save locations for Maxar image tiles if they do not exist
save_dir = r'D:\Projects\WORKING\ML\imagery\maxartest'
print(f'Output Image Directory: {save_dir}')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for label_name in gdf['BREAK_NAME'].str.lower().str.replace(' ', '_').str.replace('-', '_').unique():
    print(f'Label name found: {label_name}')
    if not os.path.exists(os.path.join(save_dir, label_name)):
        os.makedirs(os.path.join(save_dir, label_name))

# Add a field to dataframe for the output location of the maxar tiles
gdf['file_save'] = gdf.apply(lambda row: os.path.join(save_dir + '/',row['BREAK_NAME'].lower().replace(' ','_').replace('-','_') + '/' + str(row['ID'])+'.jpg'),axis=1)
print(f'File Save Location Field Calculated')

# Define function for crafting the url request from bound box field
def get_save_url(x):
    url = """https://securewatch.maxar.com/mapservice/wmsaccess?connectId=c8475cb2-647b-44a2-a2dd-a9ccf2dbcbbc&SERVICE=WMS&REQUEST=GetMap&version=1.1.1&SRS=EPSG:4326&BBOX={}&WIDTH=1102&HEIGHT=712&LAYERS=DigitalGlobe:Imagery&format=image/jpeg"""
    return url.format(','.join([str(val) for val in [x[0],x[1],x[2],x[3]]]))

# Populate 'url' field in dataframe with the correct url path using bounding box
gdf['url'] = gdf['bounds'].apply(get_save_url)
print('URL Field Calculated')

# Function to write the url path and the output path to a list
def save_data(url,path):
    res = requests.get(url, auth=HTTPBasicAuth('andolson@corelogic.com', '5p4rkl3p0ny#M'))
    with open(path,'wb') as f:
        f.write(res.content)
    return res.status_code

# Call function to write lists
url_list  = gdf['url'].tolist()
save_list = gdf['file_save'].tolist()
print(f'Number of URL calls: {len(url_list)}')

# Begin the image download
total_grids = len(url_list)
cnt         = 0
newlst      = zip(url_list, save_list)

Parallel(n_jobs=3, backend='threading')
for url, path in newlst:

    try:
        status_codes = delayed(save_data(url=url, path=path))

    except:
        print("Connection refused by the server..")
        print("Let me sleep for 10 seconds")
        print("ZZzzzz...")
        time.sleep(10)
        print("Was a nice sleep, now let me continue...")
        continue

finish_time = time.perf_counter()

print(f"Program finished in {finish_time - start_time} seconds")