from pwd_manager.interface import window_base as wb
from pwd_manager.interface import password as pwd
from pwd_manager.interface import new_password
import tkinter as tk


class Row:
    def __init__(self, window, row_index, pw: pwd.Password):
        self.row_index = row_index
        self.hidden = False
        self.name = tk.Label(window, width=15, text=pw.username)
        self.password = tk.Label(window, width=15, text=pw.password)
        self.show_password_button = tk.Button(window, width=15, text="show", command=self.show_hide_password)
        self.comment = tk.Label(window, width=15, text=pw.comment)

        self.name.grid(column=0, row=row_index)
        self.password.grid(column=1, row=row_index)
        self.show_password_button.grid(column=2, row=row_index)
        self.comment.grid(column=3, row=row_index)

    def show_hide_password(self):
        if self.hidden:
            self.password.grid_remove()
        else:
            self.password.grid()
        self.hidden = not self.hidden


def create_new_password():
    password_window = new_password.New_password_window()
    password_window.start()


class Passwords_window(wb.Window):

    def __init__(self, passwords: list[pwd.Password]):
        super().__init__(title="Your Passwords")
        self.passwords = passwords

    def show_passwords(self):
        row_index = 0
        for pw in self.passwords:
            Row(self.window, row_index, pw)
            row_index += 1

    def start(self):
        self.show_passwords()
        tk.Button(self.window, text="new password", command=create_new_password).grid()
        super().start()
