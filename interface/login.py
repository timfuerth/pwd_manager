import csv
import io
import os

from pwd_manager.interface import window_base as wb
from pwd_manager.interface import passwords as show_pw
from pwd_manager.interface import password as pw
from pwd_manager.utils import encrypt
import tkinter as tk
from tkinter import ttk


def str_to_password(password_string: str):
    print(password_string)
    passw = io.StringIO(password_string)
    print(passw)
    reader = csv.reader(password_string.split('\n'), delimiter=";")
    for row in reader:
        username, password, comment = row
        return [pw.Password(username, password, comment)]


class Login_window(wb.Window):

    def __init__(self):
        super().__init__(title="login")
        self.key = tk.StringVar()
        self.passwd_entry = ttk.Entry(self.window, show="*", width=15, textvariable=self.key)
        self.paswd_button = ttk.Button(self.window, text="login", width=4, command=self.login)

    def start(self):
        self.passwd_entry.pack()
        self.paswd_button.pack()
        super().start()

    def login(self):
        if self.key.get() != "123":
            ttk.Label(self.window, text=self.key.get()).pack()
            return

        self.window.withdraw()

        encrypt.unzip_files()

        for file in os.listdir("data"):
            encrypt.decrypt_file(file_name=file, password=self.key.get())


        pw_window = show_pw.Passwords_window(str_to_password("firefox;test;test"), self.key)

        pw_window.start()
