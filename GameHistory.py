from tkinter import *

"""class yang berkaitan dengan proses penulisan file riwayat permainan"""
class GameHistory:
    def __init__(self):
        self.window = Tk()
        self.window.title("Riwayat Permainan")

        self.textRiwayat = Text(self.window)

        fileRiwayat = open("gamehistory.txt", "r+")
        self.textRiwayat.insert("1.0", fileRiwayat.read())
        fileRiwayat.close()

        self.textRiwayat.pack()
        self.window.mainloop()
