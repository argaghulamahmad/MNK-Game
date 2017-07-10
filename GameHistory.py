from tkinter import *

"""class yang berkaitan dengan proses penulisan file riwayat permainan"""
class GameHistory:
    def __init__(self):
        self.window = Tk()
        self.window.title("Riwayat Permainan")

        self.historyText = Text(self.window)

        historyFile = open("gamehistory.txt", "r+")
        self.historyText.insert("1.0", historyFile.read())
        historyFile.close()

        self.historyText.pack()
        self.window.mainloop()