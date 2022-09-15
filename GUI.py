import configparser
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import NSEW
import os
import time
from tkinter import *
from PIL import Image, ImageTk
# from ggscrpit import runApplication
from PIL.Image import Resampling

from RunningBot import RunningBot

DEFAULTAMOUNT = 10
actualAmount = DEFAULTAMOUNT

class Settings(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.parent = master
        # master.destroy()
        # self.parent = tk.Tk()
        self.parent.geometry("950x500")
        self.create_background()
        # self.userLabel = Label(self, text="You have logged in ")
        # self.loginButton = Button(self, text="Settings", command=lambda: (self.destroy(), AppGui(master=root)))
        # self.userLabel.pack()
        # self.loginButton.pack()
        # self.pack()

    def create_background(self):

        # images
        self.photo = ImageTk.PhotoImage(Image.open('images/logo.png').resize((950, 500), Resampling.LANCZOS))
        self.backround_photo = ImageTk.PhotoImage(
            Image.open('images/settingsbackground.png').resize((870, 420), Resampling.LANCZOS))
        self.photo_save = ImageTk.PhotoImage(Image.open('images/saveandquit.png').resize((262, 57), Resampling.LANCZOS))
        self.photo_return = ImageTk.PhotoImage(Image.open('images/returntomenu.png').resize((262, 57), Resampling.LANCZOS))
        self.increasebutton = ImageTk.PhotoImage(Image.open('images/increase1.png'))
        self.increasebutton10 = ImageTk.PhotoImage(Image.open('images/increase10.png'))
        self.decreasebutton = ImageTk.PhotoImage(Image.open('images/decrease1.png'))
        self.decreasebutton10 = ImageTk.PhotoImage(Image.open('images/decrease10.png'))

        self.canvas = Canvas(root, height=950, width=500)
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.canvas.create_image(40, 40, image=self.backround_photo, anchor=NW)
        self.canvas.pack(fill="both", expand=True)

        # quit and save, return buttons
        saveButton = Button(self.canvas, image=self.photo_save, borderwidth=0,
                            command=lambda: self.returnToMenu())
        saveButton.place(x=600, y=390)
        returnButton = Button(self.canvas, image=self.photo_return, borderwidth=0,
                              command=lambda: self.returnToMenu(saveButton=self))
        returnButton.place(x=330, y=390)

        # increase, decrease buttons
        increaseButton = Button(self.canvas, image=self.increasebutton, borderwidth=0,
                                command=lambda: self.changeIterationAmount(1))
        increaseButton.place(x=625, y=175)
        increaseButton10 = Button(self.canvas, image=self.increasebutton10, borderwidth=0,
                                  command=lambda: self.changeIterationAmount(10))
        increaseButton10.place(x=565, y=175)

        decreaseButton = Button(self.canvas, image=self.decreasebutton, borderwidth=0,
                                command=lambda: self.changeIterationAmount(-1))
        decreaseButton.place(x=770, y=175)
        decreaseButton10 = Button(self.canvas, image=self.decreasebutton10, borderwidth=0,
                                  command=lambda: self.changeIterationAmount(-10))
        decreaseButton10.place(x=830, y=175)

        # entry (sum of iterations)
        self.infinite = Text(self.canvas, width=2, height=1, fg='black', border=0, bg="white",
                             font=('Minecraftia', 20, 'bold'))
        self.infinite.place(x=704, y=170)
        self.infinite.insert(END, str(actualAmount))
        self.infinite.configure(state=DISABLED)

    def changeIterationAmount(self, amount):
        global actualAmount
        actualAmount += amount
        if actualAmount <= 0:
            actualAmount = 0
        elif actualAmount >= 100:
            self.infinite["width"] = 3
            self.infinite["font"] = ('Minecraftia', 14, 'bold')
        elif actualAmount < 100:
            self.infinite["width"] = 2
            self.infinite["font"] = ('Minecraftia', 20, 'bold')

        self.infinite.configure(state=NORMAL)
        if self.infinite.get("1.0", END) != "\n":
            self.infinite.delete("1.0", END)
        self.infinite.insert(END, str(actualAmount))
        self.infinite.configure(state=DISABLED)

    def returnToMenu(self, saveButton=None):
        global actualAmount, username, choice
        if saveButton is not None:
            actualAmount = DEFAULTAMOUNT
        choice = actualAmount
        self.canvas.destroy()
        print("settings:" + str(choice))
        AppGui(master=root, username=username, choice=choice)


username = ""
choice = 0

class AppGui(tk.Frame):
    startFiniteInfinite = 0

    def __init__(self, master=None, username="", choice=0):
        tk.Frame.__init__(self, master)
        self.parent = master
        self.parent.geometry("950x500")
        self.create_background()

        self.create_base_menu()
        self.create_status_bar()
        self.create_logic(username, choice)

    def create_background(self):
        self.image_logo = Image.open('images/logo.png')
        self.image_logo = self.image_logo.resize((950, 500), Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image_logo)

        self.image_input = Image.open('images/input_form.png')
        self.resized_image = self.image_input.resize((318, 206), Resampling.LANCZOS)
        self.photo_input = ImageTk.PhotoImage(self.resized_image)

        self.canvas = Canvas(root, height=950, width=500)
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.canvas.create_image(560, 235, image=self.photo_input, anchor=NW)
        # self.canvas.create_window(10,10, anchor=NW, window=self.loginButton)

        self.settingsImage = ImageTk.PhotoImage(Image.open("images/settings.png").resize((230, 50), Resampling.LANCZOS))
        self.loginButton = Button(self.canvas, image=self.settingsImage, highlightthickness=0, borderwidth=0, border=0,
                                  command=lambda: (self.savePreviousChoice(),self.canvas.destroy(),  Settings(master=root) ))
        self.loginButton.place(x=20, y=20)
        # self.pack()
        self.canvas.pack(fill="both", expand=True)

    def create_logic(self, prevUsername="", choice=0):
        self.username = Entry(self.canvas, width=29, fg='black', border=0, bg="white", font=('Minecraftia', 9, 'bold'))
        self.username.place(x=570, y=271)
        if prevUsername == "":
            self.username.insert(END, "Your username")
        else:
            self.username.insert(END, prevUsername)
        self.username.configure(state=DISABLED)

        def onclick(event):
            self.username.configure(state=NORMAL)
            self.username.delete(0, END)

        self.username.bind("<Button-1>", onclick)

        infinite = Entry(self.canvas, width=1, fg='black', border=0, bg="white", font=('Minecraftia', 10, 'bold'))
        finite = Entry(self.canvas, width=1, fg='black', border=0, bg="white", font=('Minecraftia', 10, 'bold'))
        finite.place(x=728, y=345)
        infinite.place(x=578, y=345)
        if choice == 0:
            infinite.insert(END, "X")
            infinite.configure(state=DISABLED)
        else:
            finite.insert(END, "X")
            finite.configure(state=DISABLED)
            self.startFiniteInfinite = choice



        def onclickInfinite(event):
            finite.configure(state=NORMAL)
            finite.delete(0, END)
            infinite.insert(END, "X")
            infinite.configure(state=DISABLED)
            if len(infinite.get()) != 0:
                self.startFiniteInfinite = 0
                # self.startFinite = False

        infinite.bind("<Button-1>", onclickInfinite)

        def onclickFinite(event):
            infinite.configure(state=NORMAL)
            infinite.delete(0, END)
            finite.insert(END, "X")
            finite.configure(state=DISABLED)
            if len(finite.get()) != 0:
                self.startFiniteInfinite = actualAmount  # set in options

        finite.bind("<Button-1>", onclickFinite)

        # r = IntVar()
        # r.set(1)
        # self.radiobutton_infinite = Radiobutton(root, text="", variable=r, value=1, image=self.photo_input, height=5).place(x=50, y=50)
        # self.radiobutton_finite = Radiobutton(root, text="", variable=r, value=2, image=self.photo_input, height=5).place(x=50, y=150)

        self.start_image = Image.open('images/start.png')
        self.start_button = self.start_image.resize((312, 40), Resampling.LANCZOS)
        self.start_button_image = ImageTk.PhotoImage(self.start_button)
        startButton = Button(self.canvas, image=self.start_button_image, borderwidth=0,
                             command=lambda: RunningBot(self.startFiniteInfinite, self.username.get(), self.parent)) #(runApplication(self.startFiniteInfinite, self.username.get(), self.parent))
        startButton.place(x=560, y=390)
        # lambda:(self.destroy(), Settings(master=root))

    def create_base_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("Settings...", lambda: (self.canvas.destroy(), Settings(master=root)), "Ctrl+S", "<Control-s>"),
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

    def file_settings(self, cont):
        # event=event
        frame = cont
        frame.reset()
        frame.tkraise()

    def savePreviousChoice(self):
        global username, choice
        username = self.username.get()
        choice = self.startFiniteInfinite
        print(choice)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Goodgame gangster script")
    app = AppGui(master=root)
    app.mainloop()
    pass
