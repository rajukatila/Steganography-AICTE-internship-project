# Steganography-AICTE-internship-project
Steganography in images involves hiding secret data within an image file in such a way that it remains invisible to human perception. When combined with encryption, it adds an extra layer of security, ensuring that even if the hidden data is extracted, it remains unreadable without a decryption key.

Process:-
Encrypt the Data:
Before hiding the message in an image, encrypt it using algorithms like AES, DES, or RSA.
This ensures that even if the message is extracted, it remains unreadable.

Hide Data in the Image (Steganography Methods): 
Modify the least significant bits of pixels in the image to embed data.

Discrete Cosine Transform (DCT) Method: 
Hide data in the frequency domain of a compressed image (JPEG).

Pixel Value Differencing (PVD):
Modify pixel values based on differences between neighboring pixels.

Save & Transmit the Stego Image:
The modified image is saved in formats like PNG or BMP (lossless formats work best).
The image is shared over communication channels (email, cloud, etc.).

Extract & Decrypt Data:
The receiver extracts the hidden data using the same steganography method.
The encrypted message is then decrypted using the private key.

 Encrypted Image Steganography uses or applications
✔ Secure communication without detection
✔ Protect sensitive documents in images
✔ Digital watermarking with an encrypted signature
✔ Avoid censorship and surveillance
