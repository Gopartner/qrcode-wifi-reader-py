import os
from pyzbar.pyzbar import decode
from PIL import Image
from colorama import Fore, Back, Style, init
from urllib.parse import unquote

# Initialize Colorama
init()

# Path to the directory containing images
image_dir = 'image/'

# List all files in the image directory
files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Display files with index numbers
print("Select an image by entering the corresponding number:")
for i, file in enumerate(files):
    print(f"{i}: {file}")

# Get user input for image selection
try:
    choice = int(input("Enter the number of the image you want to select: "))
    if 0 <= choice < len(files):
        image_path = os.path.join(image_dir, files[choice])
        image = Image.open(image_path)
        print(f"Image '{files[choice]}' selected and opened.")
    else:
        print("Invalid choice. Please enter a valid number.")
        exit()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Decode QR code
decoded_objects = decode(image)

# Create a formatted output
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + " QR Code Reader Output " + Style.RESET_ALL)
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)

# Prompt user for choice of displaying cleaned or raw data
display_choice = input("Do you want to see cleaned data? (yes/no): ").strip().lower()

if decoded_objects:
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        if display_choice == 'yes':
            cleaned_data = unquote(data)
            output_data = cleaned_data
        else:
            output_data = data
        
        # Print formatted output for each QR code found
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"\nQR Code Data: {output_data}" + Style.RESET_ALL)
else:
    print(Fore.RED + Back.BLACK + Style.BRIGHT + " No QR code found." + Style.RESET_ALL)

print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)

