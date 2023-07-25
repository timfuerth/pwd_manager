from cryptography.fernet import Fernet
import base64

def encrypt_data_and_save(password, plaintext_message):
    # Generate a Fernet key
    key = Fernet.generate_key()

    # Initialize the Fernet cipher with the generated key
    cipher_suite = Fernet(key)

    # Encrypt the message
    encrypted_message = cipher_suite.encrypt(plaintext_message)

    # Save the encrypted data and key to a file
    with open('encrypted_data.bin', 'wb') as file:
        file.write(key)
        file.write(encrypted_message)

