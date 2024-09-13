print("A.S Muhammad: PIXEL MANIPULATION ENCRYPTION PROGRAM")
print()

from PIL import Image

def encrypt_image(image_path, shift_value, output_path):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]

            r = (r + shift_value) % 256
            g = (g + shift_value) % 256
            b = (b + shift_value) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(image_path, shift_value, output_path):

    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]

            r = (r - shift_value) % 256
            g = (g - shift_value) % 256
            b = (b - shift_value) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    while True:
        print("\nSimple Image Encryption Tool")
        choice = input("Do you want to encrypt or decrypt an image? (e/d): ").lower()

        if choice in ['e', 'd']:
            image_path = input("Enter the image file path: ")
            shift_value = int(input("Enter the shift value (integer): "))
            output_path = input("Enter the output file name (with extension): ")

            if choice == 'e':
                encrypt_image(image_path, shift_value, output_path)
            else:
                decrypt_image(image_path, shift_value, output_path)
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

        again = input("Do you want to process another image? (y/n): ").lower()
        if again != 'y':
            break


if __name__ == "__main__":
    main()

