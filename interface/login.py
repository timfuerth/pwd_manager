from pwd_manager.interface import window_base as wb
import tkinter as tk
from tkinter import ttk


class Login_window(wb.Window):

    def __init__(self):
        super().__init__()
        self.window.title("login")
        self.password = tk.StringVar()
        self.passwd_entry = ttk.Entry(self.window, show="*", width=15, textvariable=self.password)
        self.paswd_button = ttk.Button(self.window, text="login", width=4, command=self.login())

    def start(self):
        self.passwd_entry.pack()
        self.paswd_button.pack()
        super().start()

    def login(self):
        print(self.password.get())









