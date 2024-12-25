# examples/demo.py

from src.image_crypto import ImageCrypto

def main():
    """
    Interactive demo for encrypting and decrypting images using the ImageCrypto class.
    """
    crypto = ImageCrypto()
    
    print("Welcome to the Image Encryption Demo!")
    
    # Get file paths from the user
    input_path = input("Enter the path of the input image: ")
    encrypted_path = input("Enter the path to save the encrypted image: ")
    decrypted_path = input("Enter the path to save the decrypted image: ")
    
    try:
        # Encrypt the input image
        crypto.encrypt_image(input_path, encrypted_path)
        print(f"Image encrypted successfully and saved to: {encrypted_path}")
        
        # Decrypt the encrypted image
        crypto.decrypt_image(encrypted_path, decrypted_path)
        print(f"Image decrypted successfully and saved to: {decrypted_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
