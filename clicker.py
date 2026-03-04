from tkinter import *
from tkinter.messagebox import *

mainpage = Tk()
mainpage.title('Clicker')
mainpage.geometry(f'700x900+{mainpage.winfo_screenwidth() // 2 - 350}+{mainpage.winfo_screenheight()//2 - 450}')
mainpage.resizable(False, False)
mainpage.iconbitmap(default='icon.ico')

score = 0
coefficient = 1
active = []


def click():
    global score
    score += coefficient
    label_score['text'] = str(score)


def shop():
    for i in active:
        i.destroy()

    label_shop = Label(mainpage, text='shop')
    label_shop.place(anchor='center', relx=0.5, rely=0.5)
    active.append(label_shop)


def main():
    for i in active:
        i.destroy()

    label_score = Label(mainpage, text=str(score), font=('Times New Roman', 80), bg='blue')
    label_score.place(anchor='center', relx=0.5, rely=0.1)

    clickbutton = Button(mainpage, text='click', command=click)
    clickbutton.place(anchor='center', relx=0.5, rely=0.45)

    active.append(label_score)
    active.append(clickbutton)


def settings():
    for i in active:
        i.destroy()

    label_settings = Label(mainpage, text='settings')
    label_settings.place(anchor='center', relx=0.5, rely=0.5)
    active.append(label_settings)


label_score = Label(mainpage, text=str(score), font=('Times New Roman', 80), bg='blue')
label_score.place(anchor='center', relx=0.5, rely=0.1)

clickbutton = Button(mainpage, text='click', command=click)
clickbutton.place(anchor='center', relx=0.5, rely=0.45)

active.append(label_score)
active.append(clickbutton)

button_shop = Button(mainpage, text='shop', command=shop)
button_shop.place(anchor='center', relx=0.2, rely=0.85)

button_mainpage = Button(mainpage, text='mainpage', command=main)
button_mainpage.place(anchor='center', relx=0.5, rely=0.85)

button_settings = Button(mainpage, text='settings', command=settings)
button_settings.place(anchor='center', relx=0.8, rely=0.85)

mainpage.mainloop()