from pyzbar.pyzbar import decode
from PIL import Image
from colorama import Fore, Back, Style, init

# Initialize Colorama
init()

# Path to your image file
image_path = 'image/pass.jpg'

# Load the image
image = Image.open(image_path)

# Decode QR code
decoded_objects = decode(image)

# Create a formatted output
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + " QR Code Reader Output " + Style.RESET_ALL)
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)

if decoded_objects:
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        # Split the data into key-value pairs
        fields = data.split(';')
        wifi_type = fields[0]
        password = next((field[2:] for field in fields if field.startswith('P:')), None)
        ssid = next((field[2:] for field in fields if field.startswith('S:')), None)
        hidden = next((field[2:] for field in fields if field.startswith('H:')), None)

        # Print formatted output
        print(Fore.GREEN + Back.BLACK + Style.BRIGHT + f"\n{wifi_type};" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Password : {password};" + Style.RESET_ALL)
        print(Fore.YELLOW + f"SSID : {ssid};" + Style.RESET_ALL)
        print(Fore.YELLOW + f"H : {hidden};" + Style.RESET_ALL)
else:
    print(Fore.RED + Back.BLACK + Style.BRIGHT + " No QR code found." + Style.RESET_ALL)

print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 50 + Style.RESET_ALL)

