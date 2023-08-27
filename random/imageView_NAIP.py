### Method 1

# # importing modules
# import urllib.request
# from PIL import Image
#
url = r'https://gis.apfo.usda.gov/arcgis/services/NAIP/USDA_CONUS_PRIME/ImageServer/WMSServer?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-11476828.433411,4812056.919678,-11476306.708679,4812587.195496&CRS=EPSG:3857&WIDTH=256&HEIGHT=256&LAYERS=0&STYLES=&FORMAT=image/jpeg&DPI=96&MAP_RESOLUTION=96&FORMAT_OPTIONS=dpi:96&TRANSPARENT=TRUE'
#
# urllib.request.urlretrieve(url,"test.jpg")
#
# img = Image.open("test.jpg")
# img.show()


### Method 2

# # Imports PIL module
# from PIL import Image
#
# # open method used to open different extension image file
# im = Image.open(r"C:\Users\System-Pc\Desktop\ybear.jpg")
#
# # This method will show image in any image viewer
# im.show()

### Method 3
from io import BytesIO

from PIL import Image, ImageTk
import requests

url = r'https://gis.apfo.usda.gov/arcgis/services/NAIP/USDA_CONUS_PRIME/ImageServer/WMSServer?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-11476828.433411,4812056.919678,-11476306.708679,4812587.195496&CRS=EPSG:3857&WIDTH=256&HEIGHT=256&LAYERS=0&STYLES=&FORMAT=image/jpeg&DPI=96&MAP_RESOLUTION=96&FORMAT_OPTIONS=dpi:96&TRANSPARENT=TRUE'
response = requests.get(url)
load = Image.open(response)

render = ImageTk.PhotoImage(load)
img = Label(self, image=render)
img.image = render
img.place(x=0, y=0)