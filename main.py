from random import randint
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Losowe Kotki')

menu = ImageTk.PhotoImage(Image.open("menu.png"))
kotek1 = ImageTk.PhotoImage(Image.open("Kotki/1.jpg"))
kotek2 = ImageTk.PhotoImage(Image.open("Kotki/2.jpg"))
kotek3 = ImageTk.PhotoImage(Image.open("Kotki/3.jpg"))
kotek4 = ImageTk.PhotoImage(Image.open("Kotki/4.jpg"))
kotek5 = ImageTk.PhotoImage(Image.open("Kotki/5.jpg"))
lista_kotków = [kotek1, kotek2, kotek3, kotek4, kotek5]

my_label = Label(image=menu)
my_label.grid(row=0, column=0)

def Kotek():
    global my_label
    my_label.grid_forget()

    wynik = randint(1, 5)
    if wynik == 1:
        my_label = Label(image=lista_kotków[0])
        my_label.grid(row=0, column=0)

    if wynik == 2:
        my_label = Label(image=lista_kotków[1])
        my_label.grid(row=0, column=0)

    if wynik == 3:
        my_label = Label(image=lista_kotków[2])
        my_label.grid(row=0, column=0)

    if wynik == 4:
        my_label = Label(image=lista_kotków[3])
        my_label.grid(row=0, column=0)

    if wynik == 5:
        my_label = Label(image=lista_kotków[4])
        my_label.grid(row=0, column=0)

losuj = Button(root, text="Losuj Kotka", command=Kotek)
losuj.grid()

root.mainloop()


