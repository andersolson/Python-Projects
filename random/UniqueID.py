count = 0
startNumber = 40220
def uniqueID():

    global count,startNumber

    while count <= 200:

        count += 1
        startNumber += 1

        return startNumber

uniqueID()
