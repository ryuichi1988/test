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
y=0
NG=0
url = "C:\\Users\\大胆的豌豆\\textpic.png"
while True:
    textpic = pyautogui.screenshot(url,region=(bossS.x-72,bossS.y-515, 154, 25))
    config = '--tessdata-dir "D:\\Program Files\\Tesseract-OCR\\tessdata"'
    text = pytesseract.image_to_string(PIL.Image.open(url),config = config,lang="JPN")

    print(text)

    pyautogui.click(bossS)

    time.sleep(3)
    pyautogui.click(skipS)
    time.sleep(1)
    pyautogui.click(closeS)
    time.sleep(1)
 #   if pyautogui.pixelMatchesColor(KINRYOKU_YANSEZUOBIAOx,KINRYOKU_YANSEZUOBIAOy,(67, 132, 27)) == True :
 #       pyautogui.click(Center_ButtonRIGHT_point)
    
    n+=1
    print("""
执行第{}次\n成功{}次\n失败{}次
""".format(n,y,NG))
 #   except:
 #       pass

        



