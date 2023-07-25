import csv
from pwd_manager.utils import password as pw

def read(decrypted_csv: str):
    for row in csv.reader(csvfile=decrypted_csv, delimiter=';', lineterminator="\n"):
        username, password, comment = row

        new_password = pw.Password(username, password, comment)



