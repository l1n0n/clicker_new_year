from tkinter import *
from tkinter.messagebox import *

mainpage = Tk()
mainpage.title('Clicker')
mainpage.geometry(f'700x900+{mainpage.winfo_screenwidth() // 2 - 350}+{mainpage.winfo_screenheight()//2 - 450}')
mainpage.resizable(False, False)
mainpage.iconbitmap(default='icon.ico')

score = 0
active_page, shop_page, settings_page, coefficient = mainpage, 0, 0, 1


def click():
    score += coefficient
    label_score['text'] = str(score)


def shop():
    try:
        global label_score, clickbutton, label_settings
        label_score.destroy()
        clickbutton.destroy()
        label_settings.destroy()
    except NameError:
        pass

    label_shop = Label(mainpage, text='shop')
    label_shop.place(anchor='center', relx=0.5, rely=0.5)


def main():
    try:
        global label_shop, label_settings
        label_shop.destroy()
        label_settings.destroy()
        label_score = Label(mainpage, text=str(score), font=('Times New Roman', 80), bg='blue')
        label_score.place(anchor='center', relx=0.5, rely=0.1)

        clickbutton = Button(mainpage, text='click', command=click)
        clickbutton.place(anchor='center', relx=0.5, rely=0.45)
    except NameError:
        showinfo("", "Takogo Net")


def settings():
    try:
        global label_score, clickbutton, label_shop
        label_score.destroy()
        clickbutton.destroy()
        label_shop.destroy()
        label_settings = Label(mainpage, text='settings')
        label_settings.place(anchor='center', relx=0.5, rely=0.5)
    except NameError:
        pass


label_score = Label(mainpage, text=str(score), font=('Times New Roman', 80), bg='blue')
label_score.place(anchor='center', relx=0.5, rely=0.1)

clickbutton = Button(mainpage, text='click', command=click)
clickbutton.place(anchor='center', relx=0.5, rely=0.45)

label_shop = Label(mainpage, text='')
label_shop.place(anchor='center', relx=0.2, rely=0.8)

label_settings = Label(mainpage, text='')
label_settings.place(anchor='center', relx=0.2, rely=0.8)

button_shop = Button(mainpage, text='shop', command=shop)
button_shop.place(anchor='center', relx=0.2, rely=0.85)

button_mainpage = Button(mainpage, text='mainpage', command=main)
button_mainpage.place(anchor='center', relx=0.5, rely=0.85)

button_settings = Button(mainpage, text='settings', command=settings)
button_settings.place(anchor='center', relx=0.8, rely=0.85)

mainpage.mainloop()