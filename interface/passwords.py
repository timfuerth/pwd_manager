from pwd_manager.interface import window_base as wb
from pwd_manager.interface import password as pw
from pwd_manager.interface import new_password
# from pwd_manager.utils.encrypt import encrypt
import tkinter as tk


class Row:
    def __init__(self, window, row_index, passw: pw.Password):
        self.password = passw
        self.row_index = row_index
        self.hidden = True
        self.name_label = tk.Label(window, width=15, text=passw.username)
        self.password_label = tk.Label(window, width=15, text=passw.password)
        self.show_password_button = tk.Button(window, width=15, text="show", command=self.show_hide_password)
        self.comment_label = tk.Label(window, width=15, text=passw.comment)

        self.name_label.grid(column=0, row=row_index)
        self.password_label.grid(column=1, row=row_index)
        self.show_password_button.grid(column=2, row=row_index)
        self.comment_label.grid(column=3, row=row_index)
        self.show_hide_password()

    def show_hide_password(self):
        if self.hidden:
            self.password_label.config(text="******")
        else:
            self.password_label.config(text=self.password.password)
        self.hidden = not self.hidden


def create_new_password():
    password_window = new_password.New_password_window()
    password_window.start()


class Passwords_window(wb.Window):

    def __init__(self, passwords: list[pw.Password], key):
        super().__init__(title="Your Passwords")
        self.passwords = passwords
        self.key = key

    def logout(self):
        # encrypt(self.key)
        self.window.destroy()
        exit(0)

    def show_passwords(self):
        row_index = 0
        for passw in self.passwords:
            Row(self.window, row_index, passw)
            row_index += 1

    def start(self):
        self.show_passwords()
        tk.Button(self.window, text="new password", command=create_new_password).grid()
        tk.Button(self.window, text="logout", command=self.logout).grid()
        super().start()
