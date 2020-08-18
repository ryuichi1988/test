from pyautogui import pixelMatchesColor as pmc
from pyautogui import click as c
from pyautogui import press
import pyautogui
from time import sleep
pyautogui.FAILSAFE = False
c(0,0)

n = 35
with open("暴力破解.TXT","a") as file:
    while pmc(933,851,(84,62,29)) == False:
        m = "%06d" % n
        l = list(str(m))
        print(l)
        pyautogui.hotkey("alt","f9")
        pyautogui.press(l)
        pyautogui.press("enter")
        file.write(str(l)+"\n")
        n += 1
        sleep(1)

