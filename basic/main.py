import tkinter as tk


class App(tk.Tk):
    def __init__(self, title: str, size: tuple[int]):
        width, height = size

        # Main window setup
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.minsize(width, height)

        # Widget if there is any

    def run(self):
        # Run
        self.mainloop()


app = App("Basic Layout", (600, 400))
app.run()
