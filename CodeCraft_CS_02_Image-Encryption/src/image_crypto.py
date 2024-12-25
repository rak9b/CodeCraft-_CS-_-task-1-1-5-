# src/image_crypto.py

from PIL import Image

class ImageCrypto:
    """
    ImageCrypto provides methods for encrypting and decrypting images using RGB channel manipulation.
    """

    @staticmethod
    def encrypt_image(input_path: str, output_path: str) -> None:
        """
        Encrypts an image by swapping its RGB channels.
        
        Args:
        - input_path (str): Path to the input image.
        - output_path (str): Path where the encrypted image will be saved.
        """
        with Image.open(input_path) as img:
            # Ensure the image is in RGB format
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Access pixels
            pixels = img.load()
            width, height = img.size
            
            # Perform the RGB channel swap (R, G, B) -> (B, R, G)
            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (b, r, g)
            
            # Save the encrypted image
            img.save(output_path)
            print(f"Image encrypted and saved as {output_path}")

    @staticmethod
    def decrypt_image(input_path: str, output_path: str) -> None:
        """
        Decrypts an image by reversing the RGB channel swap.
        
        Args:
        - input_path (str): Path to the encrypted image.
        - output_path (str): Path where the decrypted image will be saved.
        """
        with Image.open(input_path) as img:
            # Access pixels
            pixels = img.load()
            width, height = img.size
            
            # Reverse the RGB channel swap (B, R, G) -> (R, G, B)
            for y in range(height):
                for x in range(width):
                    b, r, g = pixels[x, y]
                    pixels[x, y] = (r, g, b)
            
            # Save the decrypted image
            img.save(output_path)
            print(f"Image decrypted and saved as {output_path}")
