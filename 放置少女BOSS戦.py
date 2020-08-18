import pyautogui,PIL,pytesseract
import time
#time.sleep(1)
#print(pyautogui.position())
#im = pyautogui.screenshot("GUANBI.png",region=(91,660,160,60))

#print(im)

#button7location = pyautogui.locateOnScreen('1.png')
#print(button7location)
#buttonBlevelcenter = pyautogui.center(button7location)

#
boss = pyautogui.locateOnScreen("C:\\Users\\大胆的豌豆\\boss.PNG")

bossS = pyautogui.center(boss)
skipS =  (bossS.x+216,bossS.y+100)
closeS = (bossS.x,bossS.y+100)

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
print(bossS)
n=0
bossn = 0
y=0
NG=0
url = "C:\\Users\\大胆的豌豆\\textpic.png"
list = []
while True:
    textpic = pyautogui.screenshot(url,region=(bossS.x-79,bossS.y-227, 169, 30))
    textpic = PIL.Image.open(url).convert("L")
    textpic.save("textpic.png")
    config = '--tessdata-dir "D:\\Program Files\\Tesseract-OCR\\tessdata"'
    text = pytesseract.image_to_string(PIL.Image.open(url),config = config,lang="JPN")
    try:
        print(list[0])
    except IndexError:
        list.append(text)
    if text == list[-1]:
        print(text+" {}次".format(bossn))
        bossn += 1
    else:
        list.append(text)
        print("过关")
        bossn = 0
    print(list)

    pyautogui.click(bossS)

    time.sleep(2.4)
    pyautogui.click(skipS)
    time.sleep(0.4)
    if pyautogui.pixelMatchesColor(bossS.x,bossS.y,(24,21,18), tolerance=10) == True:
        pyautogui.click(closeS)
    else:
        print(bossS)
        print(pyautogui.pixel(bossS.x,bossS.y))
        time.sleep(1)
        pyautogui.click(closeS)
    time.sleep(0.2)
 #   if pyautogui.pixelMatchesColor(KINRYOKU_YANSEZUOBIAOx,KINRYOKU_YANSEZUOBIAOy,(67, 132, 27)) == True :
 #       pyautogui.click(Center_ButtonRIGHT_point)
    
    n+=1
    print("""
执行第{}次\n成功{}次\n失败{}次
""".format(n,y,NG))
 #   except:
 #       pass

        



