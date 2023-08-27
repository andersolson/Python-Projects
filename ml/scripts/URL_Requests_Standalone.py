import os
import logging
import geopandas as gpd
import requests
import time
from pyproj import Transformer
from joblib import Parallel,delayed
from datetime import datetime as dt

# create logger
logFile = os.path.dirname(os.path.abspath(__file__)) + os.sep + "NAIPtoImage.log"
logging.basicConfig(filename=logFile, filemode='a', level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logger = logging.getLogger()
logger.info("Logging has been initiated")

#zipSHP = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_Labels\Labels_Merge.zip'
zipSHP = r'D:\Projects\WORKING\ML\vectors\Firebreak_2022_11_Labels\Inference_CO_WW_Test_Set_Mini.zip'
logger.info(f'Input data: {zipSHP}')

# Read the zipped shapefile with geopandas
gpRead = gpd.read_file(zipSHP)

# Query select only Wildland and Water in shapefile
gdfQuery = gpRead[gpRead['BREAK_NAME'].isin(['Wildland','Water'])]

# Create geodataframe and add geometry field
gdf = gpd.GeoDataFrame(gdfQuery, geometry='geometry')

# Populate a 'bounds' field with the geometry field
gdf['bounds'] = gdf['geometry'].apply(lambda x: x.bounds)
logger.info(f'Bounds Field Calculated')

# Define a transformer for Decimal Degrees to Meters-UTM for URL request
proj = Transformer.from_crs(4326,3857,always_xy=True)

def get_meters(x):
    x_min,y_min,x_max,y_max = x[0],x[1],x[2],x[3]
    ll   = proj.transform(x_min,y_min)
    ur   = proj.transform(x_max,y_max)
    bbox = ll + ur
    return(bbox)

# Populate a new field with the bounding box defined in Meters-UTM
gdf['bounds_m'] = gdf['bounds'].apply(get_meters)
logger.info(f'Bounds Meters-UTM Field Calculated')

# Create the output save locations for NAIP image tiles if they do not exist
save_dir = r'D:/Projects/WORKING/ML/imagery/CO_Water_Wildland'
logger.info(f'Output Image Directory: {save_dir}')

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for label_name in gdf['BREAK_NAME'].str.lower().str.replace(' ', '_').str.replace('-', '_').unique():
    logger.info(f'Label name found: {label_name}')
    if not os.path.exists(os.path.join(save_dir, label_name)):
        os.makedirs(os.path.join(save_dir, label_name))

# Add a field to dataframe for the output location of the NAIP tiles
gdf['file_save'] = gdf.apply(lambda row: os.path.join(save_dir + '/',row['BREAK_NAME'].lower().replace(' ','_').replace('-','_') + '/' + str(row['ID'])+'.jpg'),axis=1)
logger.info(f'File Save Location Field Calculated')

# Define function for crafting the url request from bound box field
def get_save_url(x):
    #url = """https://gis.apfo.usda.gov/arcgis/services/NAIP/USDA_CONUS_PRIME/ImageServer/WMSServer?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={}&CRS=EPSG:4326&WIDTH=256&HEIGHT=256&LAYERS=0&STYLES=&FORMAT=image/jpeg&DPI=96&MAP_RESOLUTION=96&FORMAT_OPTIONS=dpi:96&TRANSPARENT=TRUE"""
    url = """https://gis.apfo.usda.gov/arcgis/services/NAIP/USDA_CONUS_PRIME/ImageServer/WMSServer?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={}&CRS=EPSG:3857&WIDTH=256&HEIGHT=256&LAYERS=0&STYLES=&FORMAT=image/jpeg&DPI=96&MAP_RESOLUTION=96&FORMAT_OPTIONS=dpi:96&TRANSPARENT=TRUE"""
    return url.format(','.join([str(val) for val in [x[0],x[1],x[2],x[3]]]))

# Populate 'url' field in dataframe with the correct url path using bounding box
gdf['url'] = gdf['bounds_m'].apply(get_save_url)
logger.info('URL Field Calculated')

# Function to request data from url path and write the output path to a list
def save_data(url,path):
    res = requests.get(url)
    with open(path,'wb') as f:
        f.write(res.content)
    #return res.status_code

# Call function to write lists
url_list  = gdf['url'].tolist()
save_list = gdf['file_save'].tolist()
logger.info(f'Number of URL calls: {len(url_list)}')

# Start a timer
startTime = dt.now()

# Begin the image download
cnt = 0
newlst = zip(url_list, save_list)

Parallel(n_jobs=10, backend='threading')
for url, path in newlst:
    cnt += 1
    runT = dt.now() - startTime
    logger.info((f'{cnt} {runT}'))

    try:
        status_codes = delayed(save_data(url=url, path=path))

    except:
        print("Connection refused by the server..")
        print("Let me sleep for 10 seconds")
        print("ZZzzzz...")
        time.sleep(10)
        print("Was a nice sleep, now let me continue...")
        continue

logger.info("Complete! Total runtime: {0}".format(dt.now() - startTime))


#### FROM CHAT GPT, TREAT WITH SKEPTICISM

# import os
# import logging
# import geopandas as gpd
# import requests
# import time
# from pyproj import Transformer
# from joblib import Parallel, delayed
# from datetime import datetime as dt
# from multiprocessing import Pool
#
# # Rest of your code...
#
# def save_data(url_path):
#     url, path = url_path
#     res = requests.get(url)
#     with open(path, 'wb') as f:
#         f.write(res.content)
#
# # Call function to write lists
# url_list = gdf['url'].tolist()
# save_list = gdf['file_save'].tolist()
# logger.info(f'Number of URL calls: {len(url_list)}')
#
# # Start a timer
# startTime = dt.now()
#
# # Begin the image download
# cnt = 0
# newlst = zip(url_list, save_list)
#
# def download_image(url_path):
#     global cnt
#     cnt += 1
#     runT = dt.now() - startTime
#     logger.info((f'{cnt} {runT}'))
#
#     try:
#         save_data(url_path)
#     except:
#         logger.info("Connection refused by the server..")
#         logger.info("Let me sleep for 10 seconds")
#         logger.info("ZZzzzz...")
#         time.sleep(10)
#         logger.info("Was a nice sleep, now let me continue...")
#         return
#
#     return "Completed"
#
# # Use multiprocessing to parallelize the image downloads
# with Pool(processes=10) as pool:
#     results = pool.map(download_image, newlst)
#
# logger.info("Complete! Total runtime: {0}".format(dt.now() - startTime))
