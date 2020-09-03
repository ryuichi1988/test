
import pyautogui,time


for a in ("220","110"):
    for b in ("102","101"):
        for c in ("1988","1980"):
            for d in ("04","08","01"):
                for e in ("19","08","01"):
                    for f in ("04","08","01"):
                        for g in ("32","31","01","11","08","04","88"):
                            id = a+b+c+d+e+f+g
                            if pyautogui.pixelMatchesColor(1551,394,(255,255,255)) == True:
                                pyautogui.click(1484,311)
                                time.sleep(0.1)
                                pyautogui.press("tab")
                                time.sleep(0.2)
                                pyautogui.write(id)
                                time.sleep(0.1)
                                if pyautogui.pixelMatchesColor(1429,510,(113,202,24)) == True:
                                    pyautogui.click(1429,510)
                                while pyautogui.pixelMatchesColor(1595,173,(38,122,233)) == False:
                                    continue
                                time.sleep(0.1)
                                pyautogui.click(1595,173)
                                while pyautogui.pixelMatchesColor(1785,425,(255,137,101)) == False:
                                    continue
                                time.sleep(0.1)
                                with open("d:\\1\\hllog.txt","a") as file:
                                    file.write(id)+"\n"
                                time.sleep(0.1)