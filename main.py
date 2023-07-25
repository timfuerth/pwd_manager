from utils.encrypt import decrypt_data
from utils.encrypt import encrypt_data_and_save


def unlock_pwd():
    password = bytes(input("pwd: "), "UTF-8")
    # msg = bytes(input("msg: "), "UTF-8")

    decrypted_message = decrypt_data(password)
    print("Decrypted message:", decrypted_message)


def encrypt_pwd():
    password = bytes(input("pwd: "), "UTF-8")
    msg = bytes(input("msg: "), "UTF-8")

    encrypt_data_and_save(password)
    print("Encrypted")

def start():
    match input("e/d: "):
        case "e":
            encrypt_pwd()
        case "d":
            unlock_pwd()
    start()


start()
