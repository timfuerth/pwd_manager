from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import pyminizip

zip_pwd = "DCÖÜ,8ÖV[]Bzpa9FP_>}f+wrD(%}$d0QgeG]}T8g!:$g]:m?xrWdPHUiu9&öRpIM"


def derive_key_from_password(password, salt):
    # Generate a key from the password and salt using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,  # Use the same number of iterations as in encryption
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


def list_files_in_directory(directory_path):
    file_list = []
    for root, dirs, files in os.listdir(directory_path):
        for file_name in files:
            file_list.append(os.path.join(root, file_name))
    return file_list


def encrypt_data_and_save(password):

    with open('encrypted_data.csv', 'rb') as file:
        plaintext_message = file.read()
    # Generate a Fernet key
    salt = os.urandom(16)
    key = derive_key_from_password(password, salt)
    print(key)
    # Initialize the Fernet cipher with the generated key
    cipher_suite = Fernet(key)

    # Encrypt the message
    encrypted_message = cipher_suite.encrypt(plaintext_message)

    # Save the encrypted data and key to a file

    with open('encrypted_data.csv', 'wb') as file:  # SAVE PWD HASH / SALT
        file.write(base64.urlsafe_b64encode(salt))
        # file.write(b'|')
        file.write(encrypted_message)

    pyminizip.compress('encrypted_data.csv', None, "data.zip", zip_pwd, 0)
    os.remove("encrypted_data.csv")


def decrypt_data(password):
    pyminizip.uncompress("data.zip", zip_pwd, None, 0)
    os.remove("data.zip")
    # Read the encrypted data and key from the file
    with open('encrypted_data.csv', 'rb') as file:
        encrypted_data_with_key = file.read()

    # Separate key from encrypted data
    salt = base64.urlsafe_b64decode(encrypted_data_with_key[:24])
    key = derive_key_from_password(password, salt)
    print(key)
    encrypted_data = encrypted_data_with_key[24:]

    # Initialize the Fernet cipher with the key
    cipher_suite = Fernet(key)

    # Decrypt the data
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open('encrypted_data.csv', 'wb') as dec_file:
        dec_file.write(decrypted_data)
    return decrypted_data


def append_encrypted(password: bytes, plaintext_message: bytes):
    #test = list_files_in_directory("data")
    #print(test[0])
    pyminizip.uncompress("data.zip", zip_pwd, None, 0)
    os.remove("data.zip")
    # Read the existing salt from the file
    with open('encrypted_data.csv', 'rb') as file:
        encrypted_data_with_key = file.read()
        salt = base64.urlsafe_b64decode(encrypted_data_with_key[:24])

    # Derive the key from the password and the existing salt
    key = derive_key_from_password(password, salt)

    # Initialize the Fernet cipher with the generated key
    cipher_suite = Fernet(key)

    # Encrypt the new message
    encrypted_message = cipher_suite.encrypt(plaintext_message)

    # Append the encrypted message to the file
    with open('encrypted_data.csv', 'ab') as encrypted_file:
        encrypted_file.write(encrypted_message)

    # Recompress the updated 'encrypted_data.csv' to 'data.zip'
    pyminizip.compress('encrypted_data.csv', None, "data.zip", zip_pwd, 0)

    # Remove the temporary 'encrypted_data.csv'
    os.remove("encrypted_data.csv")

