from GameHistory import *
from GameBoard import *


class GameMNK:
    def __init__(self, screenWidth, screenHeight):
        self.window = Tk()
        self.window.resizable(False, False)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.fixWindowSize()
        self.window.title(" MNK Game ")

        self.inputFrame = Frame(self.window)
        self.bttnFrame = Frame(self.window)

        self.warna1 = "blue"
        self.warna2 = "yellow"

        self.m = StringVar()
        self.n = StringVar()
        self.k = StringVar()
        self.tilesize = StringVar()

        self.labelJudulPermainan = Label(self.window, text="MNK Game", font='times 42 bold')
        self.labelM = Label(self.inputFrame, text="M : ")
        self.labelN = Label(self.inputFrame, text="N : ")
        self.labelK = Label(self.inputFrame, text="K : ")
        self.labelTilesize = Label(self.inputFrame, text="Tile Size : ")

        self.barisEnt = Entry(self.inputFrame, textvariable=self.m)
        self.kolomEnt = Entry(self.inputFrame, textvariable=self.n)
        self.syaratmenangEnt = Entry(self.inputFrame, textvariable=self.k)
        self.tilesizeEnt = Entry(self.inputFrame, textvariable=self.tilesize)

        self.mulaiBttn = Button(self.window, text="Mulai Game", command=self.generateBoard)
        self.riwayatBttn = Button(self.bttnFrame, text="Riwayat", command=self.gameHistory)
        self.tentangBttn = Button(self.bttnFrame, text="Tentang", command=self.gameAbout)

        self.labelJudulPermainan.pack(padx=5, pady=20)
        self.inputFrame.pack(padx=5, pady=100)
        self.mulaiBttn.pack(padx=5, pady=50)
        self.bttnFrame.pack(padx=5, pady=50)
        self.labelM.grid(row=1, column=1)
        self.barisEnt.grid(row=1, column=2)
        self.labelN.grid(row=2, column=1)
        self.kolomEnt.grid(row=2, column=2)
        self.labelK.grid(row=3, column=1)
        self.tilesizeEnt.grid(row=4, column=2)
        self.syaratmenangEnt.grid(row=4, column=1)
        self.labelTilesize.grid(row=4, column=1)
        self.syaratmenangEnt.grid(row=3, column=2)

        self.riwayatBttn.grid(row=2, column=1)
        self.tentangBttn.grid(row=2, column=2)
        self.centerofscreen(self.window)
        self.window.mainloop()

    """method untuk meletakkan window di center of screen"""
    def centerofscreen(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    """method untuk menginisasi board"""
    def generateBoard(self):
        try:
            self.GenerateBoard = GameBoard(int(self.m.get()), int(self.n.get()), int(self.k.get()), int(self.tilesize.get()))
        except ValueError:
            messagebox.showwarning("Info", "Dimohon agar mengisi input dengan benar.")

    """method untuk mengakes class game history"""
    def gameHistory(self):
        GameHistory()

    """method untuk menampilkan info program"""
    def gameAbout(self):
        messagebox.showinfo("Info",
                            "Created with love by " + "\n" + "Arga Ghulam Ahmad, 1606821601" + "\n" + "Fasilkom, Universitas Indonesia")

    """method untuk menetapkan size window"""
    def fixWindowSize(self):
        self.window.minsize(width=800, height=600)
        self.window.maxsize(width=self.screenWidth, height=self.screenHeight)
