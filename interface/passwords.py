from pwd_manager.interface import window_base as wb
import tkinter as tk


class Passwords_window(wb.Window):

    def __init__(self, passwords: dict):
        super().__init__(title="Your Passwords")
        self.passwords = passwords

    def show_passwords(self):
        row_index = 0
        for pw in self.passwords:
            name = tk.Label(self.window, width=15, text=pw)
            password = tk.Label(self.window, width=15, text=self.passwords[pw])

            name.grid(column=0, row=row_index)
            password.grid(column=1, row=row_index)
            row_index += 1

    ### TODO: only show passwords as plaintext when button is pressed