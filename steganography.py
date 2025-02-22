import cv2
import os
import string

# Load image
img = cv2.imread(r"python\heroasta.jpg")

# Check if the image is loaded correctly
if img is None:
    print("Error: Image file not found or cannot be read!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Creating dictionaries for encoding and decoding
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

rows, cols, _ = img.shape  # Get image dimensions

m = 0
n = 0
z = 0

# Encrypt the message into the image
for i in range(len(msg)):
    if n >= rows:  # Prevents out-of-bounds errors
        print("Error: Message is too long for this image!")
        exit()
    
    img[n, m, z] = d[msg[i]]  # Store character in RGB channel
    z = (z + 1) % 3  # Cycle through R, G, B channels
    
    m += 1
    if m >= cols:  # Move to the next row when reaching the column limit
        m = 0
        n += 1

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens the image

# Decryption Process
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        if n >= rows:  # Prevents out-of-bounds errors
            break
        
        message += c[img[n, m, z]]
        z = (z + 1) % 3  # Cycle through R, G, B channels
        
        m += 1
        if m >= cols:  # Move to the next row when reaching the column limit
            m = 0
            n += 1

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
