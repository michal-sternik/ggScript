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


class RunningBot():
    def __init__(self, iterationNumber, playersName, application):
        self.EXE_NAME = r"C:\Program Files (x86)\Goodgame Gangster\Goodgame Gangster.exe"
        self.runApplication(iterationNumber, playersName, application)

    def main(self):
        si = win32process.STARTUPINFO()
        si.dwFlags = win32con.STARTF_USESHOWWINDOW
        si.wShowWindow = win32con.SW_MAXIMIZE
        h_proc, h_thr, pid, tid = win32process.CreateProcess(None, self.EXE_NAME, None, None, False, 0, None, None, si)
        print(h_proc, h_thr, pid, tid)

    def runApplication(self, iterationNumber, playersName, application):
        application.destroy()
        self.main()
        s = None
        while True:
            if s is None:
                s = pyautogui.locateOnScreen("images/screenshot8.png")
            else:
                break
        sleep(1)
        self.fastclick(s.left+50, s.top+20)
        print("clicked")
        self.fastclick(s.left+50, s.top+20)
        print("clicked")
        sleep(3)

        logoutButton = pyautogui.locateOnScreen("images/logout.png")
        if logoutButton is not None:
            pyautogui.moveTo(logoutButton)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.1)
            click(960, 730)  # reconnect button
            sleep(1)

        self.iteration(iterationNumber, playersName) #here we gonna run script
        print("Iterations done!")
        time.sleep(2)


    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.5)

    def fastclick(self, x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.1)


    def clickAndDrag(self, startX, startY, endX, endY):
        win32api.SetCursorPos((startX, startY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.5)
        win32api.SetCursorPos((endX, endY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        time.sleep(0.5)


    def typeLogin(self):
        global login
        login = self.generateRandomInput(15)
        for i in login:
            pyautogui.keyDown(i)


    def typeEmail(self):
        domain = self.generateRandomInput(random.randint(5, 10))
        email = login + "@" + domain + ".com"
        for i in email:
            pyautogui.keyDown(i)


    def typePassword(self):
        for i in login:
            pyautogui.keyDown(i)


    def generateRandomInput(self, length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase #+ "1234567890" without numbers because of wrong names sometimes (still little probability of creating two same accounts)
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str


    def createAccount(self):
        click(953, 557)  # new here? button
        click(1150, 890)  # here we go button
        # user input
        click(1143, 519)  # login click
        self.typeLogin()
        click(1063, 573)  # email click
        self.typeEmail()
        click(1145, 624)  # password click
        self.typePassword()
        click(975, 694)  # accept rules
        click(1136, 900)  # continue
        time.sleep(3)


    def tutorial(self):
        click(1045, 544)  # tutorial
        click(789, 965)  # godfather
        click(1135, 896)  # okay button
        click(1549, 486)  # velvet mission
        click(1264, 719)  # start mission
        time.sleep(21)
        click(668, 721)  # mission start
        time.sleep(1)
        click(959, 875)  # skip battle
        click(964, 632)  # ok button
        time.sleep(0.5)
        click(1284, 714)  # lvl up notification
        click(699, 957)  # character tab
        click(1484, 889)  # ok button
        self.clickAndDrag(startX=372, startY=515, endX=1051, endY=604)  # drag pistol
        for i in range(3):
            click(744, 415)  # add points 3 times
        click(1039, 974)  # click shop
        click(1112, 518)  # click consumables
        self.clickAndDrag(startX=1059, startY=729, endX=372, endY=515)  # buy dynamite
        click(699, 957)  # character tab
        self.clickAndDrag(startX=372, startY=515, endX=1032, endY=694)  # equip dynamite
        click(646, 679)  # equip button
        time.sleep(0.4)
        click(789, 965)  # godfather
        click(1187, 672)  # okay button


    def selling(self):
        click(699, 957)  # character tab
        time.sleep(0.5)
        self.clickAndDrag(startX=1051, startY=604, endX=372, endY=515)  # drag back pistol
        self.clickAndDrag(startX=1032, startY=694, endX=495, endY=526)  # drag back dynamite
        self.clickAndDrag(1046, 242, 605, 526)  # drag 1st slot
        self.clickAndDrag(1188, 258, 712, 518)
        self.clickAndDrag(1318, 255, 814, 527)
        self.clickAndDrag(1471, 249, 378, 616)
        self.clickAndDrag(1052, 348, 498, 616)
        self.clickAndDrag(1185, 349, 605, 608)
        self.clickAndDrag(1316, 359, 710, 615)
        self.clickAndDrag(1446, 351, 820, 608)  # drag 8th slot

        click(1039, 974)  # click shop

        # selling
        self.clickAndDrag(372, 515, 1524, 611)  # sell pistol
        self.clickAndDrag(495, 526, 1524, 611)  # sell dynamite
        click(662, 682)
        time.sleep(0.5)
        self.clickAndDrag(605, 526, 1524, 611)  # sell 1st slot
        time.sleep(0.5)
        click(1247, 624)  # collect gold from achievment
        time.sleep(0.5)
        self.clickAndDrag(712, 526, 1524, 611)  # sell 2nd slot
        self.clickAndDrag(814, 527, 1524, 611)  # sell 3rd slot
        # 2nd row
        self.clickAndDrag(378, 616, 1524, 611)
        self.clickAndDrag(498, 616, 1524, 611)
        self.clickAndDrag(605, 616, 1524, 611)
        self.clickAndDrag(710, 616, 1524, 611)
        self.clickAndDrag(820, 616, 1524, 611)

        click(1302, 514)  # corner shop
        self.clickAndDrag(1520, 864, 372, 515)  # buy for gold 1
        click(1017, 635)  # new tab
        self.clickAndDrag(1520, 864, 495, 526, )  # buy for gold 2

        time.sleep(0.5)
        click(660, 720)  # okey stack items
        time.sleep(0.5)

        self.clickAndDrag(372, 515, 1524, 611)  # sell food
        click(662, 682)  # confirm sell food
        time.sleep(0.5)
        self.clickAndDrag(495, 526, 1524, 611)  # sell 2nd food
        time.sleep(1)


    def battle(self, name):
        click(872, 965)  # duel tab
        click(1151, 744)  # okey button
        for i in range(3):
            click(784, 552)  # type players name
            for i in name:
                pyautogui.keyDown(i)
            click(1025, 552)  # confirm
            click(738, 408)  # attack button
            click(958, 382)  # start the fight button
            click(959, 875)  # skip battle
            click(959, 548)  # okay button


    def logout(self):
        click(1588, 58)  # logout button
        time.sleep(2)
        click(960, 730)  # reconnect button
        time.sleep(2)


    def game(self, name):
        self.tutorial()
        self.selling()
        self.battle(name)
        self.logout()


    def iteration(self, amount, name):
        counter = 0
        while True:
            self.createAccount()
            self.game(name)
            counter += 1
            print(r'Iteration number {} done!'.format(counter))
            if amount == counter:
                break


# if __name__ == "__main__":
#     iterationNumber = input("Select number of iterations (o for loop): ")
#     playersName = input("Enter player's name: ")
#     #enter amount=0 for infinite loop
#     iteration(iterationNumber, playersName)
#     input("Press any key to exit...")

