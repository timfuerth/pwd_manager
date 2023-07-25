from cryptography.fernet import Fernet

def decrypt_data(password, encrypted_data_with_key):
    # Separate key from encrypted data
    key = encrypted_data_with_key[:44]  # A Fernet key is 44 bytes long when base64 encoded
    encrypted_data = encrypted_data_with_key[44:]

    # Initialize the Fernet cipher with the key
    cipher_suite = Fernet(key)

    # Decrypt the data
    decrypted_data = cipher_suite.decrypt(encrypted_data)

    return decrypted_data

if __name__ == "__main__":
    # Your password (should be the same as used in encryption)
    password = b'secret'

    # Read the encrypted data and key from the file
    with open('encrypted_data.bin', 'rb') as file:
        encrypted_data_with_key = file.read()

    decrypted_message = decrypt_data(password, encrypted_data_with_key)
    print("Decrypted message:", decrypted_message)
