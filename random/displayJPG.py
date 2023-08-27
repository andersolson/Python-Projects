from PIL import Image

# Define image path
jpgPath = r'B:\projects\FirebreakML\Firebreak_Water_Wildland\imagery\CO_Water_Wildland\wildland\0.jpg'

# Open the image with open()
jpg = Image.open(jpgPath)

# Display the image
jpg.show()