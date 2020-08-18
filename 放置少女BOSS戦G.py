from pyautogui import pixelMatchesColor as p
from pyautogui import click as c
from time import sleep as s
while True:
    if p(356,868,(221,190,114)) == True:
        c(356,868)
    while p(471,960,(255,255,232)) == False:
        c(356,868)
    s(0.2)
    c(485,963)
    while p(290,900,(52,37,38)) == False:
        c(485,963)
        c(290,900)