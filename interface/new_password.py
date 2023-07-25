from tkinter import ttk
from pwd_manager.interface import window_base as wb
from pwd_manager.interface import password


class New_password_window(wb.Window):

    def __init__(self):
        super().__init__("new Password")
        self.username = ttk.Entry(self.window, width=15)
        self.password = ttk.Entry(self.window, width=15)
        self.comment = ttk.Entry(self.window, width=15)

    def start(self):
        self.username.grid()
        self.password.grid()
        self.comment.grid()
        ttk.Button(self.window, text="create new password", command=self.save_passwd).grid()

        super().start()

    def save_passwd(self):
        return password.Password(username=self.username, password=self.password, comment=self.comment)
