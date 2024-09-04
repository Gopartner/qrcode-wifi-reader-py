from pyzbar.pyzbar import decode
from PIL import Image

# Path to your image file
image_path = 'image/pass.jpg'

# Load the image
image = Image.open(image_path)

# Decode QR code
decoded_objects = decode(image)

# Print QR code data
for obj in decoded_objects:
    print('QR Code Data:', obj.data.decode('utf-8'))

