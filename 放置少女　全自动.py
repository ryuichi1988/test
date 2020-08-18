#白天背景 主页面开始

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
checkpositionpic = pyautogui.locateOnScreen("放置自动基准点.PNG")

checkCenter = pyautogui.center(checkpositionpic)
print(checkCenter) #325 998
home =  (checkCenter.x-(325-49),checkCenter.y-(998-972))

mail = (checkCenter.x-(325-124),checkCenter.y-(998-178))
mail2need2 =  (checkCenter.x-(325-425),checkCenter.y-(998-867))
mail3 =  (checkCenter.x-(325-146),checkCenter.y-(998-867))
mail3OK =  (checkCenter.x-(325-386),checkCenter.y-(998-604))
pyautogui.click(mail)
time.sleep(1)
pyautogui.click(mail2need2)
time.sleep(1)
pyautogui.click(mail2need2)
time.sleep(1)
pyautogui.click(mail3)
time.sleep(1)
pyautogui.click(mail3OK)
time.sleep(1)
pyautogui.click(home)
time.sleep(1)
pyautogui.click(home)
time.sleep(1)


kyougi =  (checkCenter.x-(325-67),checkCenter.y-(998-775))
kyougi2 =  (checkCenter.x-(325-253),checkCenter.y-(998-237))
kyougi3 =  (checkCenter.x-(325-459),checkCenter.y-(998-644))
kyougibattle =  (checkCenter.x-(325-476),checkCenter.y-(998-641))
kyougiBattleSkip = (checkCenter.x-(325-489),checkCenter.y-(998-967))

pyautogui.click(kyougi)
time.sleep(1)
pyautogui.click(kyougi2)
time.sleep(1)
pyautogui.click(kyougi3)
time.sleep(1)
for i in range(5):
    pyautogui.click(kyougibattle)
    time.sleep(2)
    pyautogui.click(kyougiBattleSkip)
    time.sleep(1)
    pyautogui.click(home)
    time.sleep(10)
    









#event = (checkCenter.x-(325-510),checkCenter.y-(998-252))
jinei = (checkCenter.x-(325-237),checkCenter.y-(998-974))
jineiNumber3 = (checkCenter.x-(325-276),checkCenter.y-(998-137))
jineiNumber3KUNREN_double = (checkCenter.x-(325-79),checkCenter.y-(998-685))
#jineiNumber3yurei = (checkCenter.x-(325-507),checkCenter.y-(998-590))

pyautogui.click(jinei)
time.sleep(1)
pyautogui.click(jineiNumber3)
time.sleep(1)
pyautogui.click(jineiNumber3KUNREN_double)
time.sleep(1)
pyautogui.click(jineiNumber3KUNREN_double)
time.sleep(1)
pyautogui.click(jineiNumber3KUNREN_double)
time.sleep(1)
pyautogui.click(jineiNumber3KUNREN_double)
time.sleep(1)
pyautogui.click(home)
time.sleep(1)



senjyou = (checkCenter.x-(325-142),checkCenter.y-(998-971))
senjyouQuest = (checkCenter.x-(325-96),checkCenter.y-(998-855))
senjyouQuestBossSAOTAO = (checkCenter.x-(325-467),checkCenter.y-(998-607))
senjyouQuestKunrenjyotopButton = (checkCenter.x-(325-215),checkCenter.y-(998-132))
senjyouQuestKunrenjyoButton2 = (checkCenter.x-(325-151),checkCenter.y-(998-464))
senjyouQuestKunrenjyoButton3 = (checkCenter.x-(325-151),checkCenter.y-(998-464))
senjyouQuestKunrenjyoButton4 = (checkCenter.x-(325-151),checkCenter.y-(998-464))
senjyouQuestKunrenjyoButton5 = (checkCenter.x-(325-176),checkCenter.y-(998-784))
senjyouQuestKunrenjyoButton6 = (checkCenter.x-(325-459),checkCenter.y-(998-484))
senjyouQuestKunrenjyoButton7 = (checkCenter.x-(325-286),checkCenter.y-(998-684))







