#   PROGRAM AÇIKLAMASI
#
#   Elinizdeki her satırda bir ismin bulunduğu
#   .txt uzantılı dosyayı açar ve içerisinden
#   rasgele bir satır (isim) seçer.


# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import font
import random
from tkinter import filedialog

# GENEL ARAYÜZ FONKSİYONLARI
pnc = Tk()
pnc.title("Çekiliş | Hallederiz")
pnc.geometry("600x315+330+150")
pnc.resizable(False, False)
slinder1 = PhotoImage(file="çekiliş.png")
slinder = Label(image=slinder1, cursor="hand2")
slinder.place(x=-2, y=-2)


# DOSYAYI AÇAR VE İÇERİSİNDEN RASGELE KİŞİ SEÇER
def fileoperations():
    opn = open(ext["text"])
    opn_lines = opn.readlines()
    liste = []
    for line in opn_lines:
        liste.append(line)
    person = random.choice(liste)
    opn.close()
    winner["text"] = person


# DOSYAYI KULLANICININ SEÇMESİNİ SAĞLAR
def selectfile():
    dsy = filedialog.askopenfilename()
    ext["text"] = dsy
    select = Button(text="Choose the Winner", height=4, bg="black", fg="red", font="Forte", cursor="hand2",
                    command=fileoperations)
    select.place(x=5, y=195)


ext = Label(text="No File Selected")
ext.place(x=75, y=132)

dosya = Button(text="Select File", cursor="hand2", command=selectfile, bg="black", fg="white")
dosya.place(x=5, y=130)

on = Label(text="Winner :", font="Algerian", fg="red")
on.place(x=200, y=220)

winner = Label(text="Not Yet Determined")
winner.place(x=285, y=221)

author = Label(text="                                                               Yazan: Yunus AYDIN")
author.place(x=50, y=280)

mainloop()
