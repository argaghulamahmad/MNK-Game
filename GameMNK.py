from GameHistory import *
from GameBoard import *

"""class yang menginisiasi menu utama MNK Game"""
class GameMNK:
    def __init__(self, screenWidth, screenHeight):
        self.window = Tk()
        self.window.resizable(False, False)
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.fixWindowSize()
        self.window.title(" MNK Game ")
        self.window.iconbitmap(r'MNK-Game.ico')

        self.inputFrame = Frame(self.window)
        self.bttnFrame = Frame(self.window)

        self.color1 = "blue"
        self.color2 = "yellow"

        self.m = StringVar()
        self.n = StringVar()
        self.k = StringVar()

        self.gametitleLabel = Label(self.window, text="MNK Game", font='times 42 bold')
        self.labelM = Label(self.inputFrame, text="M : ")
        self.labelN = Label(self.inputFrame, text="N : ")
        self.labelK = Label(self.inputFrame, text="K : ")

        self.rowEnt = Entry(self.inputFrame, textvariable=self.m)
        self.colEnt = Entry(self.inputFrame, textvariable=self.n)
        self.requiretowin = Entry(self.inputFrame, textvariable=self.k)

        self.startBttn = Button(self.window, text="Mulai Game", command=self.generateBoard)
        self.historyBttn = Button(self.bttnFrame, text="Riwayat", command=self.gameHistory)
        self.aboutBttn = Button(self.bttnFrame, text="Tentang", command=self.gameAbout)

        self.gametitleLabel.pack(padx=5, pady=20)
        self.inputFrame.pack(padx=5, pady=100)
        self.startBttn.pack(padx=5, pady=50)
        self.bttnFrame.pack(padx=5, pady=50)
        self.labelM.grid(row=1, column=1)
        self.rowEnt.grid(row=1, column=2)
        self.labelN.grid(row=2, column=1)
        self.colEnt.grid(row=2, column=2)
        self.labelK.grid(row=3, column=1)
        self.requiretowin.grid(row=3, column=2)

        self.historyBttn.grid(row=2, column=1)
        self.aboutBttn.grid(row=2, column=2)
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
        if (self.checkInput()):
            return

        if (int(self.m.get()) <= 5 or int(self.n.get()) <= 5):
            tilesize = 60
        elif (int(self.m.get()) <= 15 or int(self.n.get()) <= 15):
            tilesize = 37
        elif (int(self.m.get()) <= 30 or int(self.n.get()) <= 30):
            tilesize = 19
        elif (int(self.m.get()) <= 40 or int(self.n.get()) <= 40):
            tilesize = 14
        elif (int(self.m.get()) <= 50 or int(self.n.get()) <= 50):
            tilesize = 10
        else:
            tilesize = 5

        try:
            self.GenerateBoard = GameBoard(int(self.m.get()), int(self.n.get()), int(self.k.get()), tilesize)
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

    """method untuk memeriksa nilai m,n, dan k"""
    def checkInput(self):
        if (int(self.m.get()) != int(self.n.get())):
            messagebox.showwarning("Input Value M or N is different", "Nilai m atau n direkomendasikan sama.")
            return True
        if (int(self.m.get()) < 3 or int(self.n.get()) < 3):
            messagebox.showwarning("Input Value M or N is too low", "Nilai m atau n Minimal adalah tiga")
            return True
        if (int(self.m.get()) > 110 or int(self.n.get()) > 110):
            messagebox.showwarning("Input Value M or N is Overload", "Nilai m (max: 250) atau n (max:110) telah melampaui batas maksimum!")
            return True
        if (int(self.k.get()) > int(self.m.get()) or int(self.k.get()) > int(self.n.get())):
            messagebox.showwarning("Input Value K is Overload", "Nilai k telah melampaui batas maksimum!")
            return True