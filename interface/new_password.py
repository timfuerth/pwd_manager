import os
from tkinter import ttk
from pwd_manager.interface import window_base as wb
from pwd_manager.interface import password
from pwd_manager.utils.encrypt import encrypt_one_file


class New_password_window(wb.Window):

    def __init__(self, key):
        super().__init__("new Password")
        self.username = ttk.Entry(self.window)
        self.password = ttk.Entry(self.window)
        self.comment = ttk.Entry(self.window)
        self.key = key

    def start(self):
        ttk.Label(self.window, text="Username: ").grid(row=0, column=0)
        self.username.grid(row=0, column=1)
        ttk.Label(self.window, text="Password: ").grid(row=1, column=0)
        self.password.grid(row=1, column=1)
        ttk.Label(self.window, text="Comment: ").grid(row=2, column=0)
        self.comment.grid(row=2, column=1)
        ttk.Button(self.window, text="create new password", command=self.save_passwd).grid()
        super().start()

    def save_passwd(self):
        passw_file_id = 0
        file_name = f"{passw_file_id}.csv"

        while os.path.isfile(file_name):
            passw_file_id = 0
            file_name = f"{passw_file_id}.csv"

        with open(file=file_name, mode='x') as file:
            pw = password.Password(username=self.username, password=self.password, comment=self.comment)
            print(str(pw))
            file.write(str(pw))

            encrypt_one_file(self.key, file_name)
            file.close()
