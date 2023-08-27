import os
import pathlib
import shutil

main_dir = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\images'
cat_dir  = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\pets\cats'
dog_dir  = r'C:\Users\andolson\Documents\WORKING\WildFire\Tensorflow_Images\pets\dogs'

data_dir = pathlib.Path(main_dir)
#print(data_dir)

pets = list(data_dir.glob('*.jpg'))
#print(pets)

catsList = []
dogsList = []

for i in pets:

    txtSplit    = str(i).split("\\")
    pet         = txtSplit[-1:]
    #print(pet)

    firstLetter = (pet[0][:1])
    #print(firstLetter)

    if (firstLetter.isupper()) == True:
        catsList.append(pet)
        #print(pet)
    else:
        dogsList.append(pet)
        #print(pet)

#print(catsList)

for cat in catsList:
    source = main_dir + "\\" + cat[0]
    #print(source)

    destination = cat_dir + "\\" + cat[0]
    #print(destination)

    shutil.move(source, destination)

for dog in dogsList:
    source = main_dir + "\\" + dog[0]
    #print(source)

    destination = dog_dir + "\\" + dog[0]
    #print(destination)

    shutil.move(source, destination)