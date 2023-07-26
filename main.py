import utils.encrypt as encrypt


def encrypt_file():
    pwd = input("pwd: ")
    file_name = input("file_name: ")
    print(encrypt.encrypt_one_file(pwd, file_name))


def decrypt_file():
    pwd = input("pwd: ")
    file_name = input("file_name: ")
    print(encrypt.decrypt_file(pwd, file_name))


def log_out():
    encrypt.zip_files()
    print("Zipped!")


def log_in():
    encrypt.unzip_files()
    print("unzipped")


def start():
    match input("e/d: "):
        case "e":
            encrypt_file()
        case "d":
            decrypt_file()
        case "z":
            log_out()
        case "u":
            log_in()
    start()


start()
