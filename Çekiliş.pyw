#   PROGRAM AÇIKLAMASI
#
#   Elinizdeki her satırda bir ismin bulunduğu
#   .txt uzantılı dosyayı açar ve içerisinden
#   rasgele bir satır (isim) seçer.



#-*- coding: utf-8 -*-
from tkinter import*
from tkinter import font
import random
from tkinter import filedialog

# GENEL ARAYÜZ FONKSİYONLARI
pnc=Tk()
pnc.title("Çekiliş | Hallederiz")
pnc.geometry("600x315+330+150")
pnc.resizable(False,False)
slinder1=PhotoImage(file="çekiliş.png")
slinder=Label(image=slinder1,cursor="hand2")
slinder.place(x=-2,y=-2)


# DOSYAYI AÇAR VE İÇERİSİNDEN RASGELE KİŞİ SEÇER
def dosyaİşlem():
    opn=open(uzantı["text"])
    opn_lines=opn.readlines()
    liste=[]
    for satır in opn_lines:
        liste.append(satır)
    kazanan_kişi=random.choice(liste)
    opn.close()
    kazanan["text"]=kazanan_kişi

# DOSYAYI KULLANICININ SEÇMESİNİ SAĞLAR
def dosyaSec():
    dsy=filedialog.askopenfilename()
    uzantı["text"]=dsy
    seç=Button(text="Kazanan Belirle",height=4,bg="black",fg="red",font="Forte",cursor="hand2",command=dosyaİşlem)
    seç.place(x=5,y=195)


uzantı=Label(text="Dosya Seçilmedi")
uzantı.place(x=75,y=132)

dosya=Button(text="Dosya Seç",cursor="hand2",command=dosyaSec,bg="black",fg="white")
dosya.place(x=5,y=130)

açık=Label(text="Kazanan:",font="Algerian",fg="red")
açık.place(x=200,y=220)

kazanan=Label(text=" Henüz Belirlenmedi")
kazanan.place(x=285,y=221)


author=Label(text="                                                               Yazan: Yunus AYDIN")
author.place(x=50,y=280)

mainloop()
