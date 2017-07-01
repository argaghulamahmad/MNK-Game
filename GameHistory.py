from tkinter import *


class GameHistory:
    """Class untuk menampilkan riwayat permainan"""

    def __init__(self):
        self.window = Tk()
        self.window.title("Riwayat Permainan")

        self.textRiwayat = Text(self.window)

        fileRiwayat = open("gamehistory.txt", "r+")
        self.textRiwayat.insert("1.0", fileRiwayat.read())
        fileRiwayat.close()

        self.textRiwayat.pack()
        self.window.mainloop()
