
import configparser
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import NSEW
import os
import time
from tkinter import *
from PIL import Image, ImageTk


class AppGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.geometry("950x500")
        self.create_background()
        self.create_base_menu()
        self.create_status_bar()
        self.create_logic()

    def create_background(self):
        self.image_logo = Image.open('images/logo.png')
        self.image_logo = self.image_logo.resize((950, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image_logo)

        self.image_input = Image.open('images/input_form.png')
        self.resized_image = self.image_input.resize((318, 206), Image.ANTIALIAS)
        self.photo_input = ImageTk.PhotoImage(self.resized_image)

        self.canvas = Canvas(root, height=950, width=500)
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.canvas.create_image(560, 235, image=self.photo_input, anchor=NW)
        self.canvas.pack(fill="both", expand=True)


    def create_logic(self):
        username = Entry(self.canvas, width=29, fg='black', border=0, bg="white", font=('Minecraftia', 9, 'bold'))
        username.place(x=570, y=271)
        username.insert(END, "Your username")
        username.configure(state=DISABLED)

        def onclick(event):
            username.configure(state=NORMAL)
            username.delete(0, END)

        username.bind("<Button-1>", onclick)

        infinite = Entry(self.canvas, width=1, fg='black', border=0, bg="white", font=('Minecraftia', 10, 'bold'))
        infinite.place(x=578, y=345)
        infinite.insert(END, "X")
        infinite.configure(state=DISABLED)

        finite = Entry(self.canvas, width=1, fg='black', border=0, bg="white", font=('Minecraftia', 10, 'bold'))
        finite.place(x=728, y=345)

        def onclickInfinite(event):
            finite.configure(state=NORMAL)
            finite.delete(0, END)
            infinite.insert(END, "X")
            print(len(infinite.get()) )

        infinite.bind("<Button-1>", onclickInfinite)

        def onclickFinite(event):
            infinite.configure(state=NORMAL)
            infinite.delete(0, END)
            finite.insert(END, "X")

        finite.bind("<Button-1>", onclickFinite)


        # r = IntVar()
        # r.set(1)
        # self.radiobutton_infinite = Radiobutton(root, text="", variable=r, value=1, image=self.photo_input, height=5).place(x=50, y=50)
        # self.radiobutton_finite = Radiobutton(root, text="", variable=r, value=2, image=self.photo_input, height=5).place(x=50, y=150)



    def create_base_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Settings...", self.file_settings, "Ctrl+S", "<Control-s>"),
                (None, None, None, None),
                ("Quit", self.file_quit, "Ctrl+Q", "<Control-q>")):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
                self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="File", menu=fileMenu, underline=0)
        pass

    def create_status_bar(self):
        self.statusbar = Label(self.parent, text="App started...")
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.place(x=0, y=480)
        pass

    def setStatusBar(self, txt):
        self.statusbar["text"] = txt
        self.statusbar.place(x=0, y=480)

    def clearStatusBar(self):
        self.statusbar["text"] = ""
        self.statusbar.place(x=-10, y=480)

    def file_quit(self):
        self.parent.destroy()
        pass

    def file_settings(self, event=None):
        event = event
        pass



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Goodgame gangster script")
    app = AppGui(master=root)
    app.mainloop()
    pass
