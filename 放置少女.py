import time
from pyautogui import pixelMatchesColor as p
from pyautogui import click as c



kinryokuRed = 470,404,(205,43,44)
kinryokugreen = 472,409,(70,134,30)
# 筋力緑 = 472,409,(70,134,30)

binsyouGre = 472,437,(70,134,30)
binsyouRed = 469,438,(206,40,44)

chiryokuGre = 473,469,(69,134,29)
chiryokuRed = 471,474,(205,42,42)

tairyokuGre = 474,498,(68,133,28)
tairyokuRed = 469,503,(206,43,43)
yes= 0
no = 0
yesno = 0
while yesno < 1151: #此处填写有多少个丹药
    if p(384,710,(248,249,250)) == p(174,709,(234,237,238)) == True:
        c(394,708)
        time.sleep(0.3)
        while p(216,692,(76,27,33)) == False:
            continue
        if p(472,409,(70,134,30)) == True:
            c(432,697)
            yes +=1
            time.sleep(0.3)

        elif  p(472,437,(70,134,30)) == p(473,469,(69,134,29)) == p(474,498,(68,133,28)) == True:
            c(432,697)
            yes +=1
            time.sleep(0.3)
        else:
            c(250,697)
            time.sleep(0.3)
            no +=1
        yesno +=1
    print("成功{}次,失败{}次,总共{}次".format(yes,no,yesno))