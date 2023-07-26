from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import pyminizip
import cryptography
import shutil

zip_pwd = "DCÖÜ,8ÖV[]Bzpa9FP_>}f+wrD(%}$d0QgeG]}T8g!:$g]:m?xrWdPHUiu9&öRpIM"


def secure_file_name(file_name):
    try:
        special_characters = ['/', '$', '*', '&', '<', '>']
        for i in special_characters:
            # Replace the special character with an empty string
            file_name = file_name.replace(i, "")
        return file_name
    except Exception as e:
        raise Exception("Error occurred while encrypting file: {e}")


def derive_key_from_password(password: str, salt):
    password = bytes(password, "UTF-8")
    # Generate a key from the password and salt using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000,  # Use the same number of iterations as in encryption
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key


def encrypt_one_file(password: str, file_name: str):
    try:
        # Removing special chars to prevent '../'
        file_name = secure_file_name(file_name)

        with open("data/" + file_name, 'rb') as open_file:
            plaintext_message = open_file.read()
        if plaintext_message[-12:] == b":::ENCRYPTED":
            return "File is already encrypted!"
        # Generate a Fernet key
        salt = os.urandom(16)
        key = derive_key_from_password(password, salt)

        # Initialize the Fernet cipher with the generated key
        cipher_suite = Fernet(key)

        # Encrypt the message
        print(plaintext_message)
        encrypted_message = cipher_suite.encrypt(plaintext_message)
        print(encrypted_message)
        with open("data/" + file_name, 'wb') as file:  # SAVE SALT / ENCRYPTED DATA
            file.write(base64.urlsafe_b64encode(salt))
            file.write(encrypted_message)
            file.write(b":::ENCRYPTED")
        return "ENCRYPTED!"
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"Error occurred while encrypting file: {e}"


def zip_files():
    file_list = [os.path.join("data", f) for f in os.listdir("data") if
                 os.path.isfile(os.path.join("data", f))]
    pyminizip.compress_multiple(file_list, [], "output_zip_file.zip", "123", 0)
    shutil.rmtree('data')


def unzip_files():
    data_directory = "data"
    output_zip_file = "output_zip_file.zip"

    if not os.path.exists(data_directory):
        os.makedirs(data_directory)

    password = "123"

    # Extract the files from the password-protected ZIP archive
    pyminizip.uncompress(output_zip_file, data_directory, password, 0)


# Call the function to perform the extraction

'''def encrypt_data_and_save(password):
    file_list = list_files_in_directory("data")
    for file in file_list:
        with open(file, 'rb') as open_file:
            plaintext_message = open_file.read()
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
    os.remove("encrypted_data.csv")'''


def decrypt_file(password: str, file_name: str):
    # TODO vulnerability patch: path injections ("../")
    # Read the encrypted data and key from the file
    try:
        with open("data/" + file_name, 'rb') as file:
            encrypted_data_with_key = file.read()

        # Separate key from encrypted data
        salt = base64.urlsafe_b64decode(encrypted_data_with_key[:24])
        key = derive_key_from_password(password, salt)

        encrypted_data = encrypted_data_with_key[24:]

        # Initialize the Fernet cipher with the key
        cipher_suite = Fernet(key)

        # Decrypt the data
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        with open("data/" + file_name, 'wb') as dec_file:
            dec_file.write(decrypted_data)
        return decrypted_data

    except FileNotFoundError:
        return "File not found. Please check the file path."
    except cryptography.fernet.InvalidToken:
        return "Decryption failed. The provided password is incorrect."
    except Exception as e:
        return f"Error occurred while decrypting file: {e}"


'''def append_encrypted(password: bytes, plaintext_message: bytes):
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
    os.remove("encrypted_data.csv")'''
