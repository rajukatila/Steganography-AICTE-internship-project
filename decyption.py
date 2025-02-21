import cv2

def decrypt_image(image_path):
    # Load encrypted image
    img = cv2.imread(image_path)

    # Check if the image is loaded correctly
    if img is None:
        print("Error: Encrypted image file not found!")
        return

    # Read the password saved during encryption
    try:
        with open("password.txt", "r") as f:
            correct_password = f.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found!")
        return

    pas = input("Enter passcode for Decryption: ")

    if pas != correct_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    # Dictionary for decoding
    c = {i: chr(i) for i in range(256)}

    rows, cols, _ = img.shape  # Get image dimensions

    message = []
    n, m, z = 0, 0, 0

    while n < rows:
        char_value = img[n, m, z]  # Extract pixel value
        char = c[char_value]  # Convert to character

        if char == '\0':  # Stop at end marker
            break
        
        message.append(char)
        z = (z + 1) % 3  # Cycle through R, G, B

        m += 1
        if m >= cols:  # Move to the next row
            m = 0
            n += 1

    print("Decryption message:", "".join(message))

if __name__ == "__main__":
    image_path = "encryptedImage.png"
    decrypt_image(image_path)

