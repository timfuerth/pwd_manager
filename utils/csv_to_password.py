import csv
from pwd_manager.utils import password as pw
from pwd_manager.utils.encrypt import decrypt_data, encrypt_line


def get_decrypted_passwords(key):

    decrypted_passwords: list[pw.Password] = []

    with decrypt_data(key) as file:
        for row in csv.reader(csvfile=file, delimiter=';'):
            username, password, comment = row
            password = pw.Password(username, password, comment)
            decrypted_passwords += password

    return decrypted_passwords


def encrypt_password(password, key):

    with open('encrypted_data.csv', 'a') as file:

        row = password.username, password.password, password.comment
        encrypt_line(row, key)

        writer = csv.writer(csvfile=file, delimiter=';')
        writer.writerow(row)



