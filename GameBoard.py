from tkinter import *
from numpy import *
from math import *
import time

"""class yang berfungsi untuk menginisiasi papan permainan sesuai input yang diberikan dari class GameMNK"""
class GameBoard():  # class untuk menghasilkan papan permainan
    def __init__(self, row, col, requiretowin, tilesize):
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.title("MNK Game")
        self.window.iconbitmap(r'MNK-Game.ico')

        self.infoFrame = Frame(self.window)

        self.boardFill = []  # list yang digunakan untuk menyimpan informasi event klik mouse, agar lokasi yang telah diklik tidak dapat diklik kembali

        self.m = row
        self.n = col
        self.k = requiretowin
        self.size = tilesize

        self.complete = False

        self.counter = 0  # variabel untuk menentukan giliran main
        self.posLst = []  # list dua dimensi yang digunakan untuk menyimpan informasi koordinat 'p1' dan 'p2' terletak

        self.canvas = Canvas(self.window, width=row * self.size, height=col * self.size)
        self.currentstatus = Label(self.infoFrame, text="Giliran", font="Times 15 bold")
        self.turnLabel = Label(self.infoFrame, text="Pemain 1", font="Calibri 13 ")
        self.canvas.pack()
        self.infoFrame.pack()
        self.currentstatus.pack()
        self.turnLabel.pack()

        # loop yang digunakan untuk membuat objek kotak sebesar self.size
        for i in range(row):
            self.posLst.append(
                [])  # list self.posLst merupakan list berdimensi dua yang digunakan untuk meletakkan informasi letak 'p1' dan 'p2'
            for j in range(col):
                self.posLst[i].append(j)
                self.posLst[i][j] = 0

                self.rectangle = self.canvas.create_rectangle(self.size * i, self.size * j, (i + 1) * self.size,
                                                              (j + 1) * self.size, fill="blue", outline='white')
                # menerapkan proses dimana kotak dapat di klik
                self.canvas.tag_bind(self.rectangle, '<Button-1>', lambda event, arg=self.rectangle: self.click(arg))

        localtime = time.asctime(time.localtime(time.time()))  # meminta informasi waktu pada sistem
        self.historyFile = open("gamehistory.txt",
                                "a")  # membuat fileRiwayatPermainan.txt untuk menyimpan informasi riwayat permainan
        self.historyFile.write("\n" + "Permainan baru dimulai pada " + str(localtime) + "." + "\n")

        self.centerofscreen(self.window)
        self.window.mainloop()

    def click(self, event):  # method yang digunakan untuk menjalankan perintah dari klik kiri mouse
        if (not self.complete):
            if self.counter % 2 == 0:
                self.historyFile.write(
                    "Giliran Pemain 1" + " turn" + str(self.counter) + "." + "\n")  # tulis ke file riwayat

                if event not in self.boardFill:
                    self.canvas.itemconfig(event, fill='red')  # mengubah warna merah untuk pemain1
                    self.boardFill.append(event)
                    self.posLst[(event % self.m) - 1][(ceil(event / self.n) - 1)] = "p1"
                    self.counter += 1
                else:
                    pass

                self.turnLabel.config(text="Pemain 2", font="Calibri 13 ")  # menampilkan giliran pemain

            else:
                self.historyFile.write("Giliran Pemain 2" + " turn" + str(self.counter) + "." + "\n")

                if event not in self.boardFill:
                    self.canvas.itemconfig(event, fill='green')  # mengubah warna hijau untuk pemain 2
                    self.boardFill.append(event)
                    self.posLst[(event % self.m) - 1][(ceil(event / self.n) - 1)] = "p2"
                    self.counter += 1
                else:
                    pass

                self.turnLabel.config(text="Pemain 1", font="Calibri 13 ")  # menampilkan giliran pemain

            for i in self.posLst:
                print(i)
            print(" ")

            # cek 'p1' dan 'p2' secara horizontal
            self.totalp1Col = 0
            self.totalp2Col = 0

            for i in range((self.m)):
                self.totalp1Col = 0
                self.totalp2Col = 0
                for j in range((self.n)):
                    if self.posLst[i][j] == 'p1':
                        self.totalp1Col += 1
                        if self.totalp1Col == int(self.k):
                            self.p1win()
                    else:
                        self.totalp1Col = 0

                    if self.posLst[i][j] == 'p2':
                        self.totalp2Col += 1
                        if self.totalp2Col == int(self.k):
                            self.p2win()
                    else:
                        self.totalp2Col = 0

                        # cek 'p1' dan 'p2' secara vertikal
            self.totalp1Row = 0
            self.totalp2Row = 0

            for j in range((self.m)):
                self.totalp1Row = 0
                self.totalp2Row = 0
                for i in range((self.n)):
                    if self.posLst[i][j] == 'p1':
                        self.totalp1Row += 1
                        if self.totalp1Row == int(self.k):
                            self.p1win()
                    else:
                        self.totalp1Row = 0

                    if self.posLst[i][j] == 'p2':
                        self.totalp2Row += 1
                        if self.totalp2Row == int(self.k):
                            self.p2win()
                    else:
                        self.totalp2Row = 0

                        # List posisi normal 'p1' dan 'p2' secara diagonal
            lstDiagonal_normal = []
            for i in range(-(self.m), (self.m) + 1):
                lstDiagonal_normal.append(diag(self.posLst, k=i))

            print(lstDiagonal_normal)

            # Cek posisi 'p1' dan 'p2' secara Diagonal Kanan
            self.totalp1Rightdiag = 0
            self.totalp2Rightdiag = 0

            for i in range(len(lstDiagonal_normal)):
                self.totalp1Rightdiag = 0
                self.totalp2Rightdiag = 0
                for j in range(len(lstDiagonal_normal[i])):
                    if lstDiagonal_normal[i][j] == 'p1':
                        self.totalp1Rightdiag += 1
                        if self.totalp1Rightdiag == (self.k):
                            self.p1win()
                    else:
                        self.totalp1Rightdiag = 0

                    if lstDiagonal_normal[i][j] == 'p2':
                        self.totalp2Rightdiag += 1
                        if self.totalp2Rightdiag == (self.k):
                            self.p2win()
                    else:
                        self.totalp2Rightdiag = 0

                        # list posisi yang dibalik 'p1' dan 'p2' secara diagonal
            lstDiagonal_reversed = []
            for i in range(-(self.m), (self.m) + 1):
                lstDiagonal_reversed.append(diag(list(reversed(self.posLst)), k=i))

            print(lstDiagonal_reversed)

            # Cek posisi 'p1' dan 'p2' secara Diagonal kiri
            self.totalp1Leftdiag = 0
            self.totalp2Leftdiag = 0

            for i in range(len(lstDiagonal_reversed)):
                self.totalp1Leftdiag = 0
                self.totalp2Leftdiag = 0
                for j in range(len(lstDiagonal_reversed[i])):
                    if lstDiagonal_reversed[i][j] == 'p1':
                        self.totalp1Leftdiag += 1
                        if self.totalp1Leftdiag == (self.k):
                            self.p1win()
                    else:
                        self.totalp1Leftdiag = 0

                    if lstDiagonal_reversed[i][j] == 'p2':
                        self.totalp2Leftdiag += 1
                        if self.totalp2Leftdiag == (self.k):
                            self.p2win()
                    else:
                        self.totalp2Leftdiag = 0

                        # mengecek bila permainan seri
            if self.counter == (int(self.m) * int(self.n)):
                if (self.p1p2tie()): self.window.destroy()

    """method untuk meletakkan window di center of screen"""
    def centerofscreen(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    """method yang dilaksanakan saat p1 menang"""
    def p1win(self):
        # messagebox.showinfo(title="Permainan Selesai",
        #                              message="Selamat!, Pemain 1 Menang saat giliran ke " + str(
        #                                  self.counter) + ".")
        self.complete = True
        self.currentstatus.config(text="Permainan Berakhir")
        self.turnLabel.config(text="Pemain 1 Menang", font="Calibri 13 ")
        self.boardFill = [angka for angka in range(self.m * self.n)]
        self.historyFile.write(
            "Selamat!, Pemain 1 Menang saat giliran ke " + str(self.counter) + "." + "\n")
        self.historyFile.close()

    """method yang dilaksanakan saat p2 menang"""
    def p2win(self):
        # messagebox.showinfo(title="Permainan Selesai",
        #                              message="Selamat!, Pemain 2 Menang saat giliran ke " + str(
        #                                  self.counter) + ".")
        self.complete = True
        self.currentstatus.config(text="Permainan Berakhir")
        self.turnLabel.config(text="Pemain 2 Menang", font="Calibri 13 ")
        self.boardFill = [angka for angka in range(self.m * self.n)]
        self.historyFile.write(
            "Selamat!, Pemain 2 Menang saat giliran ke " + str(self.counter) + "." + "\n")
        self.historyFile.close()

    """method yang dilaksanakan saat keadaan seri"""
    def p1p2tie(self):
        # messagebox.showinfo(title="Game Over", message="Permainan selesai dengan keadaan seri!")
        self.complete = True
        self.currentstatus.config(text="Permainan Berakhir")
        self.turnLabel.config(text="Permainan Berakhir Seri", font="Calibri 13 ")
        self.boardFill = [angka for angka in range(self.m * self.n)]
        self.historyFile.write("Permainan Seri")
        self.historyFile.close()