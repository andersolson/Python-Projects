count = 0
def uniqueID():
    global count

    startNumber = 40220

    while count <= 200:

        count += 1

        startNumber += 1

        return startNumber

genID()