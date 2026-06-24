from PIL import Image

KEY = 50

def encrypt_image(input_image, output_image):
    img = Image.open(input_image)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r + KEY) % 256,
                (g + KEY) % 256,
                (b + KEY) % 256
            )

    img.save(output_image)
    print("Image Encrypted Successfully!")

def decrypt_image(input_image, output_image):
    img = Image.open(input_image)
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r - KEY) % 256,
                (g - KEY) % 256,
                (b - KEY) % 256
            )

    img.save(output_image)
    print("Image Decrypted Successfully!")

choice = input("Encrypt or Decrypt (E/D): ").upper()

if choice == "E":
    encrypt_image("input.jpg", "encrypted.jpg")
elif choice == "D":
    decrypt_image("encrypted.jpg", "decrypted.jpg")
else:
    print("Invalid Choice")