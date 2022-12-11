
from ast import main
from pickle import NEWOBJ_EX 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = tk.Tk()
root.title("MOVIE TICKET BOOKING SYSTEM")
root.geometry("1000x650")

resim1 = Image.open("foto.jpg")
resize_resim1 = resim1.resize((1000,650))
resim2 = ImageTk.PhotoImage(resize_resim1)

canvas1 = Canvas(root, width=1000, height = 650)
canvas1.pack(fill="both", expand= True)
canvas1.create_image(0,0, image= resim2, anchor="nw")

k = "  -  STAR CINEMA  -  "
text= canvas1.create_text(500,50,text= k, font= " Helvatica 35 bold", fill ="white")

bbox = canvas1.bbox(text)
canvas1.create_rectangle(bbox, outline="white")


kullanici_adi = Label(canvas1, text= "Kullanici Adi: ", font= " Helvatica 25 bold", background= "white", foreground = "black")
kullanici_adi.place(x=200, y=120)

kullanici_adi_entry = tk.Entry(root , textvariable = "kullanici adi stringi" , font= " Helvatica 25 " )
kullanici_adi_entry.place(x=450, y=120)

sifre = Label(canvas1, text= "Sifre: ", font= " Helvatica 25 bold", background= "white", foreground = "black")
sifre.place(x=325, y=180)

sifre_entry = tk.Entry(root, textvariable= "sifre stringi" , font = " Helvatica 25 " , show="*")
sifre_entry.place(x=450, y=180)
                                                            



class pencere_olustur:
    def __init__(self,pencere):
        self.pencere = pencere
        self.pencere =Toplevel(root)
        self.pencere.geometry("1000x650")
        self.pencere.title("ANASAYFA      |      HOSGELDINIZ")

        resim3 = Image.open("anasayfa.jpg")
        resize_resim3 = resim3.resize((1000,650))
        resim4 = ImageTk.PhotoImage(resize_resim3)
        
        canvas2= Canvas(self.pencere ,  width=1000, height = 650)
        canvas2.pack(fill="both", expand= True)
        canvas2.create_image(0,0, image= resim4, anchor="nw")
       
        k2= "  -  STAR CINEMA  -  "
        text2=canvas2.create_text(500,70,text= k, font= " Helvatica 35 bold", fill ="black")

        bbox2= canvas2.bbox(text2)
        canvas2.create_rectangle(bbox2,outline="white") 
        root.withdraw()

        film_ara_kutusu = Label(canvas2 , text= "Film Ara :",font= " Helvatica 18 bold", background= "white",foreground="black")
        film_ara_kutusu.place(x=200, y=125)

        film_secme_listesi = ["Adina gore ara","Cikis tarihine gore ara",
                         "Diline gore ara","Sehir ismine gore ara",
                         "Turune gore ara",]    

        film_secme_butonu = ttk.Combobox(canvas2, values = film_secme_listesi,font= " Helvatica 18 bold")
        film_secme_butonu.set("Seciniz..")
        film_secme_butonu.place(x=320 , y=125)
        
        mainloop()


def Anasayfa_penceresi():
   
   anasayfa_func= pencere_olustur("anasayfa_misafir")


#def uye_olma_penceresi():
#    uye_olma = Toplevel(root)
#    uye_olma.geometry("1000x650")
#    uye_olma.title(" UYE OL ")
#    root.withdraw()



misafir_girisi = tk.Button(root, text= "Misafir Girisi" , font= " Helvatica 18 bold", background= "#bc8f8f", foreground = "black" , command= Anasayfa_penceresi)
misafir_girisi.place(x=700, y=350)

giris_yap = tk.Button(root, text= "Giris Yapiniz" ,font= " Helvatica 18 bold", background= "white", foreground = "black", command= Anasayfa_penceresi)
giris_yap.place(x=650 , y=250)

uye_ol = tk.Button(root, text= "Uye Ol",font= " Helvatica 18 bold", background= "#a52a2a", foreground = "white")
uye_ol.place(x=735, y=425)

mainloop()

