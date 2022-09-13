import tkinter

from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import string
# import tkinter as Tk
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import subprocess
import sys
import win32process

EXE_NAME = r"C:\Program Files (x86)\Goodgame Gangster\Goodgame Gangster.exe"
def main():
    si = win32process.STARTUPINFO()
    si.dwFlags = win32con.STARTF_USESHOWWINDOW
    si.wShowWindow = win32con.SW_MAXIMIZE
    h_proc, h_thr, pid, tid = win32process.CreateProcess(None, EXE_NAME, None, None, False, 0, None, None, si)
    print(h_proc, h_thr, pid, tid)




if __name__ == '__main__':
    # root = Tk()
    # root.title("Goodgame gangster script")
    # app = BazoweGui(root=root)
    # app.mainloop()

    main()
    s = None
    while True:
        if s is None:
            win32api.SetCursorPos((random.randint(0,1920), random.randint(0,1080)))
            s = pyautogui.locateOnScreen("fullscreen.png")
            print(s)
        else:
            break
    sleep(1)
    click(s.left+50, s.top+20)
    click(s.left+50, s.top+20)
    # iteration() #here we gonna run script


# root = Tk()
# root.geometry("950x500+300+200")
# root.configure(bg="#fff")
# root.resizable(False,False)
# root.wm_attributes('-transparentcolor', '#faeee1')
# image = PhotoImage(file="logo.png")
# background = Label(root, image=image).place(x=0, y=0)
# img = Image.open("logo.png")
# width = 950
# height = 500
# img = img.resize((width,height), Image.ANTIALIAS)
# photoImg = ImageTk.PhotoImage(img)
# b = Button(master,image=photoImg, command=callback, width=50)
# b.pack()


# def resize_image(event):
#     new_width = event.width
#     new_height = event.height
#     image = copy_of_image.resize((new_width, new_height))
#     photo = ImageTk.PhotoImage(image)
#     label.config(image = photo)
#     label.image = photo #avoid garbage collection
#


time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.3)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.5)


# def clickAndDrag(startX, startY, endX, endY):
#     win32api.SetCursorPos((startX, startY))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     time.sleep(0.5)
#     win32api.SetCursorPos((endX, endY))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#     time.sleep(0.5)
#
#
# def typeLogin():
#     global login
#     login = generateRandomInput(15)
#     for i in login:
#         pyautogui.keyDown(i)
#
#
# def typeEmail():
#     domain = generateRandomInput(random.randint(5, 10))
#     email = login + "@" + domain + ".com"
#     for i in email:
#         pyautogui.keyDown(i)
#
#
# def typePassword():
#     for i in login:
#         pyautogui.keyDown(i)
#
#
# def generateRandomInput(length):
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase + "1234567890"
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     return result_str
#
#
# def createAccount():
#     click(953, 557)  # new here? button
#     click(1150, 890)  # here we go button
#     # user input
#     click(1143, 519)  # login click
#     typeLogin()
#     click(1063, 573)  # email click
#     typeEmail()
#     click(1145, 624)  # password click
#     typePassword()
#     click(975, 694)  # accept rules
#     click(1136, 900)  # continue
#     time.sleep(3)
#
#
# def tutorial():
#     click(1045, 544)  # tutorial
#     click(789, 965)  # godfather
#     click(1135, 896)  # okay button
#     click(1549, 486)  # velvet mission
#     click(1264, 719)  # start mission
#     time.sleep(21)
#     click(668, 721)  # mission start
#     time.sleep(1)
#     click(959, 875)  # skip battle
#     click(964, 632)  # ok button
#     time.sleep(0.5)
#     click(1284, 714)  # lvl up notification
#     click(699, 957)  # character tab
#     click(1484, 889)  # ok button
#     clickAndDrag(startX=372, startY=515, endX=1051, endY=604)  # drag pistol
#     for i in range(3):
#         click(744, 415)  # add points 3 times
#     click(1039, 974)  # click shop
#     click(1112, 518)  # click consumables
#     clickAndDrag(startX=1059, startY=729, endX=372, endY=515)  # buy dynamite
#     click(699, 957)  # character tab
#     clickAndDrag(startX=372, startY=515, endX=1032, endY=694)  # equip dynamite
#     click(646, 679)  # equip button
#     time.sleep(0.4)
#     click(789, 965)  # godfather
#     click(1187, 672)  # okay button
#
#
# def selling():
#     click(699, 957)  # character tab
#     time.sleep(0.5)
#     clickAndDrag(startX=1051, startY=604, endX=372, endY=515)  # drag back pistol
#     clickAndDrag(startX=1032, startY=694, endX=495, endY=526)  # drag back dynamite
#     clickAndDrag(1046, 242, 605, 526)  # drag 1st slot
#     clickAndDrag(1188, 258, 712, 518)
#     clickAndDrag(1318, 255, 814, 527)
#     clickAndDrag(1471, 249, 378, 616)
#     clickAndDrag(1052, 348, 498, 616)
#     clickAndDrag(1185, 349, 605, 608)
#     clickAndDrag(1316, 359, 710, 615)
#     clickAndDrag(1446, 351, 820, 608)  # drag 8th slot
#
#     click(1039, 974)  # click shop
#
#     # selling
#     clickAndDrag(372, 515, 1524, 611)  # sell pistol
#     clickAndDrag(495, 526, 1524, 611)  # sell dynamite
#     click(662, 682)
#     time.sleep(0.5)
#     clickAndDrag(605, 526, 1524, 611)  # sell 1st slot
#     time.sleep(0.5)
#     click(1247, 624)  # collect gold from achievment
#     time.sleep(0.5)
#     clickAndDrag(712, 526, 1524, 611)  # sell 2nd slot
#     clickAndDrag(814, 527, 1524, 611)  # sell 3rd slot
#     # 2nd row
#     clickAndDrag(378, 616, 1524, 611)
#     clickAndDrag(498, 616, 1524, 611)
#     clickAndDrag(605, 616, 1524, 611)
#     clickAndDrag(710, 616, 1524, 611)
#     clickAndDrag(820, 616, 1524, 611)
#
#     click(1302, 514)  # corner shop
#     clickAndDrag(1520, 864, 372, 515)  # buy for gold 1
#     click(1017, 635)  # new tab
#     clickAndDrag(1520, 864, 495, 526, )  # buy for gold 2
#
#     time.sleep(0.5)
#     click(660, 720)  # okey stack items
#     time.sleep(0.5)
#
#     clickAndDrag(372, 515, 1524, 611)  # sell food
#     click(662, 682)  # confirm sell food
#     time.sleep(0.5)
#     clickAndDrag(495, 526, 1524, 611)  # sell 2nd food
#     time.sleep(1)
#
#
# def battle(name):
#     click(872, 965)  # duel tab
#     click(1151, 744)  # okey button
#     for i in range(3):
#         click(784, 552)  # type players name
#         for i in name:
#             pyautogui.keyDown(i)
#         click(1025, 552)  # confirm
#         click(738, 408)  # attack button
#         click(958, 382)  # start the fight button
#         click(959, 875)  # skip battle
#         click(959, 548)  # okay button
#
#
# def logout():
#     click(1588, 58)  # logout button
#     time.sleep(2)
#     click(960, 730)  # reconnect button
#     time.sleep(2)
#
#
# def game(name):
#     tutorial()
#     selling()
#     battle(name)
#     logout()
#
#
# def iteration(amount, name):
#     counter = 0
#     while True:
#         createAccount()
#         game(name)
#         counter += 1
#         if amount == counter:
#             break
#
#
# if __name__ == "__main__":
#     iterationNumber = input("Select number of iterations (o for loop): ")
#     playersName = input("Enter player's name: ")
#     #enter amount=0 for infinite loop
#     iteration(iterationNumber, playersName)
#     input("Press any key to exit...")
#
