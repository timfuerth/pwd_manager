import tkinter as tk
from tkinter import ttk


class Window:
    def __init__(self, title="Password-manager"):
        self.window = tk.Tk()
        self.window.title(title)

    def start(self):
        self.set_size(600, 500)
        self.window.mainloop()

    def set_size(self, width, height):
        new_geometry = f"{width}x{height}" \
                       f"+{int(self.window.winfo_screenwidth() / 2) - width}" \
                       f"+{int(self.window.winfo_screenheight() / 2) - height}"
        self.window.geometry(new_geometry)
