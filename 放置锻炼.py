from pyautogui import pixelMatchesColor as p
from pyautogui import click as c
from time import sleep as s
c(157,789)
s(0.2)
while True:
    if p(416,552,(161,38,28)) == p(415,601,(164,33,27)) == True:
        break
    else:
        c(157,789)
        s(0.1)
