import arcpy, os, re

word = "Welcome"
print word
if re.match("a-zA-Z_", word):
    print("Valid")
else:
    print("Invalid")