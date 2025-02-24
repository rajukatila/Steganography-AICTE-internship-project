import cv2
import os
import string
img = cv2.imread(r"python\heroasta.jpg")

if img is None:
    print("Error: Image file not found or cannot be read!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")


d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

rows, cols, _ = img.shape  

m = 0
n = 0
z = 0


for i in range(len(msg)):
    if n >= rows: 
        print("Error: Message is too long for this image!")
        exit()
    
    img[n, m, z] = d[msg[i]]  
    z = (z + 1) % 3  
    
    m += 1
    if m >= cols:  
        m = 0
        n += 1

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        if n >= rows: 
            break
        
        message += c[img[n, m, z]]
        z = (z + 1) % 3 
        
        m += 1
        if m >= cols:  
            m = 0
            n += 1

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")
