a = None
b = 67
c = 'true'

oResult = []

# Test for none type
if not [x for x in (a, b, c) if x is None]:

    # Append the results to the list
    oResult.append([a, b, c])

else:
    print('None Type found')