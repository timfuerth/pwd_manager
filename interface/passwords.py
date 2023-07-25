from pwd_manager.interface import window_base as wb
from pwd_manager.interface import password as pwd
from pwd_manager.interface import new_password
import tkinter as tk


class Passwords_window(wb.Window):

    def __init__(self, passwords: list[pwd.Password]):
        super().__init__(title="Your Passwords")
        self.passwords = passwords

    def show_passwords(self):
        row_index = 0
        for pw in self.passwords:
            name = tk.Label(self.window, width=15, text=pw.username)
            password = tk.Label(self.window, width=15, text=pw.password)
            comment = tk.Label(self.window, width=15, text=pw.comment)

            name.grid(column=0, row=row_index)
            password.grid(column=1, row=row_index)
            comment.grid(column=2, row=row_index)

            row_index += 1

    def create_new_password(self):
        password_window = new_password.New_password_window()
        password_window.start()

    def start(self):
        self.show_passwords()
        tk.Button(self.window, text="new password", command=self.create_new_password).grid()
        super().start()

    ### TODO: only show passwords as plaintext when button is pressed