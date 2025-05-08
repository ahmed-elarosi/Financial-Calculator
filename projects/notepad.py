import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class SimpleNotepad:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Elarosi's Notepad")

        # Text widget
        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == "__main__":
    main()
