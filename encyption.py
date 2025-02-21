import cv2
import os

def encrypt_image(image_path, output_path):
    # Load image
    img = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if img is None:
        print("Error: Image file not found or cannot be read!")
        return

    msg = input("Enter secret message: ") + '\0'  # Add end marker
    password = input("Enter a passcode: ")

    # Dictionary for encoding
    d = {chr(i): i for i in range(256)}

    rows, cols, _ = img.shape  # Get image dimensions
    max_chars = rows * cols * 3  # Max characters we can store

    if len(msg) > max_chars:
        print("Error: Message is too long for this image!")
        return

    m, n, z = 0, 0, 0

    # Encrypt the message into the image
    for char in msg:
        img[n, m, z] = d[char]  # Store character in RGB channel
        z = (z + 1) % 3  # Cycle through R, G, B
        
        m += 1
        if m >= cols:  # Move to the next row when reaching the column limit
            m = 0
            n += 1

    # Save encrypted image
    cv2.imwrite(output_path, img)
    print(f"Encryption complete! Encrypted image saved as: {output_path}")

    os.system(f"start {output_path}")  # Open the image

    # Save the password for decryption
    with open("password.txt", "w") as f:
        f.write(password)

if __name__ == "__main__":
    image_path = r"python\code1.png"
    output_path = "encryptedImage.png"
    encrypt_image(image_path, output_path)
