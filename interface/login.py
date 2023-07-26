import csv

from pwd_manager.interface import window_base as wb
from pwd_manager.interface import passwords as show_pw
from pwd_manager.interface import password as pw
import tkinter as tk
from tkinter import ttk


def str_to_password(password_string: str):
    for row in csv.reader(csvfile=password_string, delimiter=";"):
        username, password, comment = row
        password = pw.Password(username, password, comment)


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

        pw_window = show_pw.Passwords_window(str_to_password(), self.key)

        pw_window.start()
