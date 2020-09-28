import pyautogui as pg
from time import sleep as sl
pg.moveTo(150,18)
sl(0.5)
pg.drag(1,-1,0.5,button="left")
