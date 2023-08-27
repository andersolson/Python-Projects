# Mini pre-processing script to find the unique image ids for firebreak images based on image class. Can be
# used to build queries in ArcMap or QGIS to query 1/4 mile grid cells used in AI model.

import pathlib
import re

# Google drive image location
#photoDir = '/content/drive/My Drive/firebreak_images'

# Local folder of images
photoDir = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\firebreak_images\jpg_images'
data_dir = pathlib.Path(photoDir)
print('Data Dir path: {0}'.format(data_dir))

allImg   = list(data_dir.glob('*/*.jpg'))
wildland = list(data_dir.glob('Wildland/*'))
water    = list(data_dir.glob('Water/*'))
UNR      = list(data_dir.glob('UrbanNon-Residential/*'))
urban    = list(data_dir.glob('Urban/*'))
SR       = list(data_dir.glob('ScatteredResidential/*'))
MDR      = list(data_dir.glob('MediumDensityResidential/*'))
LDR      = list(data_dir.glob('LowDensityResidential/*'))
HDR      = list(data_dir.glob('HighDensityResidential/*'))
AG       = list(data_dir.glob('Agriculture/*'))

'''
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
image_count = len(list(data_dir.glob('Agriculture/*.jpg')))
print(image_count)
'''

#List of unique image Ids found in the entire collection LOCAL ONLY
idList = []
for i in allImg:
  #print(i)
  pthString = str(i)
  #print(pthString)
  fileName = pthString.split('\\')[10]
  #print(fileName)

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  idList.append(res[0])


print(len(idList))
#print(str(idList))


with open(r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\firebreak_images\Query.txt', 'w') as f:
  for id in idList:
    f.write('{0},X\n'.format(str(id)))


'''
# List of Wildland unique image Ids
wildList = []
for i in wildland:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  wildList.append(res[0])

#print(len(wildList))
print(str(wildList))

# List of Water unique image Ids
waterList = []
for i in water:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  waterList.append(res[0])

#print(len(wildList))
print(str(waterList))

# List of UNR unique image Ids
UNRList = []
for i in UNR:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  UNRList.append(res[0])

#print(len(wildList))
print(str(UNRList))

#List of urban unique image Ids
urbanList = []
for i in urban:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  urbanList.append(res[0])

#print(len(wildList))
print(str(urbanList))

#List of SR unique image Ids
SRList = []
for i in SR:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  SRList.append(res[0])

#print(len(wildList))
print(str(SRList))

#List of MDR unique image Ids
MDRList = []
for i in MDR:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  MDRList.append(res[0])

#print(len(wildList))
print(str(MDRList))

#List of LDR unique image Ids
LDRList = []
for i in LDR:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  LDRList.append(res[0])

#print(len(wildList))
print(str(LDRList))

#List of HDR unique image Ids
HDRList = []
for i in HDR:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  HDRList.append(res[0])

#print(len(wildList))
print(str(HDRList))

#List of AG unique image Ids
AGList = []
for i in AG:
  pthString = str(i)
  fileName = pthString.split('/')[6]

  temp = re.findall(r'\d+', fileName)
  res = list(map(int, temp))

  AGList.append(res[0])

#print(len(wildList))
print(str(AGList))
'''