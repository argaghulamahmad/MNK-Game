# Nama Mahasiswa	: Arga Ghulam Ahmad
# NPM Mahasiswa		: 1606821601
# Mata Kuliah       : Dasar Dasar Pemrograman 1
# Kelas             : A
# Tugas  		    : MNK Game
# Tanggal Deadline	: 16 November 2016
# Interpreter		: Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55)

from GameMNK import *
from win32api import GetSystemMetrics

"""jalankan file ini di konsol untuk memulai MNK Game"""
try:
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
except:
    width = 800
    height = 600

GameMNK(width, height)