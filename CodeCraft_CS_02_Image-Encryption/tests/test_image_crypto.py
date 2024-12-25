# tests/test_image_crypto.py

import pytest
from PIL import Image
from src.image_crypto import ImageCrypto
import os

@pytest.fixture
def test_image():
    """
    Fixture to create a test image for encryption and decryption tests.
    """
    # Create a simple 100x100 red image
    img = Image.new('RGB', (100, 100), color='red')
    path = 'test_image.png'
    img.save(path)
    yield path  # Provide the test image path to the test function
    os.remove(path)  # Cleanup: remove the test image after the test

def test_encryption_decryption(test_image):
    """
    Test that encryption and decryption functions work correctly.
    """
    crypto = ImageCrypto()
    
    # Define paths for encrypted and decrypted images
    encrypted_path = 'encrypted_test.png'
    decrypted_path = 'decrypted_test.png'
    
    # Encrypt the test image
    crypto.encrypt_image(test_image, encrypted_path)
    
    # Verify that the encrypted image exists
    assert os.path.exists(encrypted_path), "Encrypted image was not saved."

    # Decrypt the image
    crypto.decrypt_image(encrypted_path, decrypted_path)
    
    # Verify that the decrypted image exists
    assert os.path.exists(decrypted_path), "Decrypted image was not saved."

    # Verify that the decrypted image is the same as the original
    original_image = Image.open(test_image)
    decrypted_image = Image.open(decrypted_path)
    
    # Compare pixel-by-pixel to ensure the images are identical
    original_pixels = original_image.load()
    decrypted_pixels = decrypted_image.load()
    
    for y in range(original_image.height):
        for x in range(original_image.width):
            assert original_pixels[x, y] == decrypted_pixels[x, y], f"Pixels do not match at ({x}, {y})"
    
    # Clean up: remove encrypted and decrypted images
    os.remove(encrypted_path)
    os.remove(decrypted_path)
