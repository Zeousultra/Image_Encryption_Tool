from PIL import Image
import numpy as np
import os

def xor_encrypt_decrypt(data, key):
    return data ^ key

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    data = np.array(image)

    # Apply XOR operation to each color channel
    encrypted_data = np.bitwise_xor(data, key)
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")
    data = np.array(image)

    # Apply XOR operation to decrypt (same as encryption)
    decrypted_data = np.bitwise_xor(data, key)
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def main():
    print("Image Encryption Tool (XOR-based)")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()

    if choice in ['e', 'd']:
        input_path = input("Enter the input image path: ")
        output_path = input("Enter the output image path: ")
        try:
            key = int(input("Enter the encryption/decryption key (integer 0–255): "))
            if key < 0 or key > 255:
                raise ValueError("Key must be between 0 and 255.")
        except ValueError as e:
            print("Invalid key:", e)
            return

        if not os.path.exists(input_path):
            print("Input file does not exist.")
            return

        if choice == 'e':
            encrypt_image(input_path, output_path, key)
        else:
            decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
