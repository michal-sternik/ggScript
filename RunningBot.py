import random
import string
import pyautogui
import win32api
import win32con
import win32process
from pyautogui import *


class RunningBot:
    def __init__(self, iterationNumber, playersName, application):
        self.EXE_NAME = r"C:\Program Files (x86)\Goodgame Gangster\Goodgame Gangster.exe"
        self.runApplication(iterationNumber, playersName, application)

    def main(self):
        si = win32process.STARTUPINFO()
        si.dwFlags = win32con.STARTF_USESHOWWINDOW
        si.wShowWindow = win32con.SW_MAXIMIZE
        h_proc, h_thr, pid, tid = win32process.CreateProcess(None, self.EXE_NAME, None, None, False, 0, None, None, si)
        print(h_proc, h_thr, pid, tid)

    def runAndFullScreen(self):
        self.main()
        s = None
        while True:
            if s is None:
                s = pyautogui.locateOnScreen("images/screenshot8.png")
            else:
                break
        sleep(1)
        self.fastclick(s.left + 50, s.top + 20)
        print("self.clicked")
        self.fastclick(s.left + 50, s.top + 20)
        print("self.clicked")

    def checkIfGameRuns(self):
        print("locating")
        s = pyautogui.locateOnScreen("images/9.png")
        print(s)
        if s is None:
            return False
        else:
            return True

    def runApplication(self, iterationNumber, playersName, application):
        application.destroy()
        self.runAndFullScreen()
        sleep(3)

        logoutButton = pyautogui.locateOnScreen("images/logout.png")
        print(logoutButton)#d
        if logoutButton is not None:
            pyautogui.moveTo(logoutButton)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.1)
            self.click(960, 730)  # reconnect button
            sleep(1)

        self.iteration(iterationNumber, playersName)  # here we gonna run script
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
        letters = string.ascii_lowercase  # + "1234567890" without numbers because of wrong names sometimes (still little probability of creating two same accounts)
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    def createAccount(self):
        self.click(953, 557)  # new here? button
        self.click(1150, 890)  # here we go button
        # user input
        self.click(1143, 519)  # login self.click
        self.typeLogin()
        self.click(1063, 573)  # email self.click
        self.typeEmail()
        self.click(1145, 624)  # password self.click
        self.typePassword()
        self.click(975, 694)  # accept rules
        self.click(1136, 900)  # continue
        time.sleep(3)

    def tutorial(self):
        self.click(1045, 544)  # tutorial
        self.click(789, 965)  # godfather
        self.click(1135, 896)  # okay button
        self.click(1549, 486)  # velvet mission
        self.click(1264, 719)  # start mission
        time.sleep(21)
        self.click(668, 721)  # mission start
        time.sleep(1)
        self.click(959, 875)  # skip battle
        self.click(964, 632)  # ok button
        time.sleep(0.5)
        self.click(1284, 714)  # lvl up notification
        self.click(699, 957)  # character tab
        self.click(1484, 889)  # ok button
        self.clickAndDrag(startX=372, startY=515, endX=1051, endY=604)  # drag pistol
        for i in range(3):
            self.click(744, 415)  # add points 3 times
        self.click(1039, 974)  # self.click shop
        self.click(1112, 518)  # self.click consumables
        self.clickAndDrag(startX=1059, startY=729, endX=372, endY=515)  # buy dynamite
        self.click(699, 957)  # character tab
        self.clickAndDrag(startX=372, startY=515, endX=1032, endY=694)  # equip dynamite
        self.click(646, 679)  # equip button
        time.sleep(0.4)
        self.click(789, 965)  # godfather
        self.click(1187, 672)  # okay button

    def selling(self):
        self.click(699, 957)  # character tab
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

        self.click(1039, 974)  # self.click shop

        # selling
        self.clickAndDrag(372, 515, 1524, 611)  # sell pistol
        self.clickAndDrag(495, 526, 1524, 611)  # sell dynamite
        self.click(662, 682)
        time.sleep(0.5)
        self.clickAndDrag(605, 526, 1524, 611)  # sell 1st slot
        time.sleep(0.5)
        self.click(1247, 624)  # collect gold from achievment
        time.sleep(0.5)
        self.clickAndDrag(712, 526, 1524, 611)  # sell 2nd slot
        self.clickAndDrag(814, 527, 1524, 611)  # sell 3rd slot
        # 2nd row
        self.clickAndDrag(378, 616, 1524, 611)
        self.clickAndDrag(498, 616, 1524, 611)
        self.clickAndDrag(605, 616, 1524, 611)
        self.clickAndDrag(710, 616, 1524, 611)
        self.clickAndDrag(820, 616, 1524, 611)

        self.click(1302, 514)  # corner shop
        self.clickAndDrag(1520, 864, 372, 515)  # buy for gold 1
        self.click(1017, 635)  # new tab
        self.clickAndDrag(1520, 864, 495, 526, )  # buy for gold 2

        time.sleep(0.5)
        self.click(660, 720)  # okey stack items
        time.sleep(0.5)

        self.clickAndDrag(372, 515, 1524, 611)  # sell food
        self.click(662, 682)  # confirm sell food
        time.sleep(0.5)
        self.clickAndDrag(495, 526, 1524, 611)  # sell 2nd food
        time.sleep(1)

    def battle(self, name):
        self.click(872, 965)  # duel tab
        self.click(1151, 744)  # okey button
        for i in range(3):
            self.click(784, 552)  # type players name
            for i in name:
                pyautogui.keyDown(i)
            self.click(1025, 552)  # confirm
            self.click(738, 408)  # attack button
            self.click(958, 382)  # start the fight button
            self.click(959, 875)  # skip battle
            self.click(959, 548)  # okay button

    def logout(self):
        self.click(1588, 58)  # logout button
        time.sleep(2)
        self.click(960, 730)  # reconnect button
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
            self.resotreIfCrashed()
            print(r'Iteration number {} done!'.format(counter))
            if amount == counter:
                break

    def resotreIfCrashed(self):
        isRunning = self.checkIfGameRuns()
        if not isRunning:
            sleep(1800) #sleep if game crashed to avoid crash once again
            self.runAndFullScreen()
            logoutButton = pyautogui.locateOnScreen("images/logout.png")
            if logoutButton is not None:
                pyautogui.moveTo(logoutButton)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                time.sleep(0.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                time.sleep(0.1)
                self.click(960, 730)  # reconnect button
                sleep(1)


# if __name__ == "__main__":
#     iterationNumber = input("Select number of iterations (o for loop): ")
#     playersName = input("Enter player's name: ")
#     #enter amount=0 for infinite loop
#     iteration(iterationNumber, playersName)
#     input("Press any key to exit...")