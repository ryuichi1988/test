import pyautogui,time
from plyer import notification
#time.sleep(1)
#print(pyautogui.position())
#im = pyautogui.screenshot("GUANBI.png",region=(91,660,160,60))

#print(im)

#button7location = pyautogui.locateOnScreen('1.png')
#print(button7location)
#buttonBlevelcenter = pyautogui.center(button7location)

#

ButtonRIGHT = pyautogui.locateOnScreen("1.png")
Center_ButtonRIGHT_point = pyautogui.center(ButtonRIGHT)
ButtonLEFT = pyautogui.locateOnScreen("C.png")
Center_ButtonLEFT_point  = pyautogui.center(ButtonLEFT)

KINRYOKU_YANSEZUOBIAOx = 474
KINRYOKU_YANSEZUOBIAOy = 409
#KINRYOKU_YANSEget = pyautogui.pixel(KINRYOKU_YANSEZUOBIAOx,KINRYOKU_YANSEZUOBIAOy)
#print(KINRYOKU_YANSEget)

#red : (201, 39, 39)
#blue : (67, 132, 27)
#筋力　474 409
#敏捷 474 439
#知力 474 466
#体力 474 502



n=0
y=0
NG=0
while n<255:
    pyautogui.moveTo(508,877)
    RUNTEST = pyautogui.locateOnScreen("测试VIP字符.png")
    if RUNTEST == None:
        time.sleep(0.5)
        print('缓冲')
        continue
    else:
        pass
#    try:
    pyautogui.click(Center_ButtonRIGHT_point)
    time.sleep(0.3)
    if pyautogui.pixelMatchesColor(KINRYOKU_YANSEZUOBIAOx,KINRYOKU_YANSEZUOBIAOy,(67, 132, 27)) == True :
        pyautogui.click(Center_ButtonRIGHT_point)
        y+=1
        time.sleep(0.3)
    elif pyautogui.pixelMatchesColor(474,439,(67,132,27)) == True and (pyautogui.pixelMatchesColor(474,466,(67,132,27))) == True and pyautogui.pixelMatchesColor(474,502,(67,132,27)) == True:
        pyautogui.click(Center_ButtonRIGHT_point)
        y+=1
        time.sleep(0.3)
    else:
        pyautogui.click(Center_ButtonLEFT_point)
        time.sleep(0.3)
        NG+=1
    n+=1
    print("""
执行第{}次\n成功{}次\n失败{}次
""".format(n,y,NG))
 #   except:
 #       pass

        



