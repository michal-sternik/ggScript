import configparser
import shutil
import sys
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, messagebox
from tkinter.constants import NSEW
import os
import time
from tkinter import *
from PIL import Image, ImageTk
# from ggscrpit import runApplication
from PIL.Image import Resampling

from RunningBot import RunningBot
from utils import resource_path

DEFAULTAMOUNT = 10
actualAmount = DEFAULTAMOUNT


IMAGES_TO_SAVE = [
    ('images/config/fullscreen_example.png', 'fullscreen.png'),
    ('images/config/logout_example.png', 'logout.png'),
    # ('images/config/mainscreen_example.png', 'mainscreen.png'),
]
class FirstRunSetup(tk.Toplevel):
    def __init__(self, master=None, step=0):

        super().__init__(master)
        self.master = master
        self.step = step
        self.exe_path = None #r"C:\Program Files (x86)\Goodgame Gangster\Goodgame Gangster.exe" #default
        self.title(f"First Run Setup - Step {self.step + 1}")
        self.geometry("950x500")
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.configure(bg='#FFF3E6')

    def on_close(self):

        if messagebox.askyesno("Exit Setup",
                               "Are you sure you want to exit the setup? The application will close."):
            self.master.destroy()

    def create_widgets(self):

        for widget in self.winfo_children():
            widget.destroy()

        if self.step == 0:

            self.label = tk.Label(self, text="Please select the .exe file for the game.\n"
                                             "It's probalby in C:\Program Files (x86)\Goodgame Gangster\Goodgame Gangster.exe")
            self.label.pack(pady=10)
            self.label.configure(bg="#FFF3E6")

            self.example_image = Image.open(resource_path('images/config/exe_example.png'))
            max_height = 250

            original_width, original_height = self.example_image.size

            aspect_ratio = original_width / original_height
            new_width = int(max_height * aspect_ratio)

            self.example_image = self.example_image.resize((new_width, max_height), Resampling.LANCZOS)
            self.example_photo = ImageTk.PhotoImage(self.example_image)
            self.example_label = tk.Label(self, image=self.example_photo, borderwidth=0, highlightthickness=0)
            self.example_label.pack(pady=10)

            self.upload_button = tk.Button(self, text="Select .exe File", command=self.select_exe_file)
            self.upload_button.pack(pady=10)

            self.path_label = tk.Label(self, text="", fg="blue")
            self.path_label.pack(pady=10)

            button_frame = tk.Frame(self, bg='#FFF3E6')  # Dodaj tło takie samo jak okno, jeśli chcesz

            self.next_button = tk.Button(button_frame, text="Next", command=self.next_step, state=tk.DISABLED)
            self.next_button.pack(side=tk.LEFT, padx=10)  # Umieszczamy przycisk po lewej stronie z odstępem 10px

            self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.cancel_setup)
            self.cancel_button.pack(side=tk.LEFT, padx=10)

            button_frame.pack(pady=10)

        else:

            self.label = tk.Label(self, text=f"Please upload the required image for step {self.step}.")
            self.label.pack(pady=10)

            if self.step <= len(IMAGES_TO_SAVE):
                example_image_path, _ = IMAGES_TO_SAVE[self.step-1]

                self.example_image = Image.open(resource_path(example_image_path))
                max_height = 250

                original_width, original_height = self.example_image.size

                aspect_ratio = original_width / original_height
                new_width = int(max_height * aspect_ratio)

                self.example_image = self.example_image.resize((new_width, max_height), Resampling.LANCZOS)

                self.example_photo = ImageTk.PhotoImage(self.example_image)
                self.example_label = tk.Label(self, image=self.example_photo, borderwidth=0, highlightthickness=0)
                self.example_label.pack(pady=10)
            else:
                self.example_label = tk.Label(self, text="No example image for this step.")
                self.example_label.pack(pady=10)

            self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
            self.upload_button.pack(pady=10)

            self.path_label = tk.Label(self, text="", fg="blue")
            self.path_label.pack(pady=10)

            button_frame = tk.Frame(self, bg='#FFF3E6')  # Dodaj tło takie samo jak okno, jeśli chcesz

            self.next_button = tk.Button(button_frame, text="Next", command=self.next_step, state=tk.DISABLED)
            self.next_button.pack(side=tk.LEFT, padx=10)  # Umieszczamy przycisk po lewej stronie z odstępem 10px

            self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.cancel_setup)
            self.cancel_button.pack(side=tk.LEFT, padx=10)  # Umieszczamy przycisk obok

            button_frame.pack(pady=10)

    def select_exe_file(self):

        default_path = r"C:\Program Files (x86)\Goodgame Gangster"
        file_path = filedialog.askopenfilename(
            initialdir=default_path,
            title="Select the .exe file",
            filetypes=[("Executable files", "*.exe")]
        )

        if file_path:
            self.exe_path = file_path
            self.path_label.config(text=f"Selected: {file_path}")
            self.next_button.config(state=tk.NORMAL)

    def upload_image(self):

        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:

            _, target_filename = IMAGES_TO_SAVE[self.step-1]

            destination_path = resource_path(os.path.join('images/logic', target_filename))
            shutil.copy(file_path, destination_path)

            self.path_label.config(text=f"Uploaded: {file_path}")


            self.next_button.config(state=tk.NORMAL)

    def next_step(self):

        self.step += 1

        if self.step <= len(IMAGES_TO_SAVE):

            self.create_widgets()
        else:

            self.finish_setup()

    def cancel_setup(self):

        if messagebox.askyesno("Cancel Setup", "Are you sure you want to cancel the setup process?"):
            self.master.destroy()

    def finish_setup(self):

        config = configparser.ConfigParser()
        config['DEFAULT'] = {'first_run': 'False', 'exe_path': self.exe_path}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        messagebox.showinfo("Setup Complete", "All images and the .exe file have been uploaded successfully.")
        self.destroy()

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
        self.photo = ImageTk.PhotoImage(Image.open(resource_path('images/gui/logo.png')).resize((950, 500), Resampling.LANCZOS))
        self.backround_photo = ImageTk.PhotoImage(
            Image.open(resource_path('images/gui/settingsbackground.png')).resize((870, 420), Resampling.LANCZOS))
        self.photo_save = ImageTk.PhotoImage(Image.open(resource_path('images/gui/saveandquit.png')).resize((262, 57), Resampling.LANCZOS))
        self.photo_return = ImageTk.PhotoImage(Image.open(resource_path('images/gui/returntomenu.png')).resize((262, 57), Resampling.LANCZOS))
        self.increasebutton = ImageTk.PhotoImage(Image.open(resource_path('images/gui/increase1.png')))
        self.increasebutton10 = ImageTk.PhotoImage(Image.open(resource_path('images/gui/increase10.png')))
        self.decreasebutton = ImageTk.PhotoImage(Image.open(resource_path('images/gui/decrease1.png')))
        self.decreasebutton10 = ImageTk.PhotoImage(Image.open(resource_path('images/gui/decrease10.png')))
        self.clearDataButton = ImageTk.PhotoImage(Image.open(resource_path('images/gui/cleardata.png')).resize((230, 50), Resampling.LANCZOS))

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

        clearDataButton = Button(self.canvas, image=self.clearDataButton, borderwidth=0,
                                  command=lambda: self.clearData())
        clearDataButton.place(x=600, y=275)


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

    def clearData(self):
        try:
            if os.path.exists("config.ini"):
                os.remove("config.ini")
            else:
                print("Config file does not exist.")
        except Exception as e:
            print(f"Error while deleting config file: {e}")

        self.master.destroy()
        #restart app
        python = sys.executable
        os.execl(python, python, *sys.argv)


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
        self.image_logo = Image.open(resource_path('images/gui/logo.png'))
        self.image_logo = self.image_logo.resize((950, 500), Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image_logo)

        self.image_input = Image.open(resource_path('images/gui/input_form.png'))
        self.resized_image = self.image_input.resize((318, 206), Resampling.LANCZOS)
        self.photo_input = ImageTk.PhotoImage(self.resized_image)

        self.canvas = Canvas(root, height=950, width=500)
        self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
        self.canvas.create_image(560, 235, image=self.photo_input, anchor=NW)
        # self.canvas.create_window(10,10, anchor=NW, window=self.loginButton)

        self.settingsImage = ImageTk.PhotoImage(Image.open(resource_path("images/gui/settings.png")).resize((230, 50), Resampling.LANCZOS))
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

        self.start_image = Image.open(resource_path('images/gui/start.png'))
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


def check_first_run():
    config = configparser.ConfigParser()
    if not os.path.exists('config.ini'):
        config['DEFAULT'] = {'first_run': 'True'}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        return True
    else:
        config.read('config.ini')
        if config['DEFAULT'].getboolean('first_run'):
            return True
        else:
            #if setup has beed done then assign exe variable
            RunningBot.EXE_NAME = config['DEFAULT'].get('exe_path')
            return False

if __name__ == '__main__':
    root = tk.Tk()
    root.title("ggScript")
    if check_first_run():
        root.withdraw()
        first_run_setup = FirstRunSetup(root)
        root.wait_window(first_run_setup)
        # root.deiconify()

        try:
            if root.winfo_exists():
                root.deiconify()
            else:
                sys.exit()
        except tk.TclError:
            sys.exit()
    config = configparser.ConfigParser()
    config.read('config.ini')
    RunningBot.EXE_NAME = config['DEFAULT'].get('exe_path')
    app = AppGui(master=root)
    app.mainloop()
    pass
