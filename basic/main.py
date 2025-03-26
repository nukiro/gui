import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title: str, size: tuple[int]):
        width, height = size

        # Main window setup
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.minsize(width, height)

        # Widget if there is any
        self.menu = Menu(self)
        self.segment_one = Segment(self, "label", "button")
        self.segment_two = Segment(self, "test", "click")
        self.segment_three = Segment(self, "hello", "test")

    def run(self):
        # Run
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(
            self, background="red", text="Hello World", padding=10, anchor="center"
        ).pack(fill="both")

        self.pack(fill="x")


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        # widgets
        ttk.Label(self, text=label_text, background="blue").grid(
            row=0, column=0, padx=5, sticky="se"
        )
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew", pady=15)

        # placing the segment
        self.pack(expand=True, fill="both")


app = App("Basic Layout", (600, 400))
app.run()
