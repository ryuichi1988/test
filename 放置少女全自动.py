import pyautogui,time,sys
from datetime import datetime
#pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
#textPIC = r"C:\Users\大胆的豌豆\textPIC.PNG"
checkn = 0
#checkpositionpic = pyautogui.locateOnScreen(r"C:\Users\大胆的豌豆\放置自动基准点.PNG")
if pyautogui.pixelMatchesColor(532,108,(219,85,81),tolerance=5) == True:
    pyautogui.click(532,108)
    time.sleep(1)
if pyautogui.pixelMatchesColor(512,109,(253,111,128),tolerance=20) == True:
    pyautogui.click(512,109)
    time.sleep(1)
if pyautogui.pixelMatchesColor(510,72,(169,9,43)) == True:
    pyautogui.click(510,72)
    time.sleep(1)


# 窗口位置: 0.0  556 or 557 y :  1018 or 1019  # # # # # # # # # # # # # 
def quickreturn():
    while pyautogui.pixelMatchesColor(188,45,(155,255,255)) == False:
        pyautogui.click(home)
    time.sleep(0.2)

def mianfeianniu():
    if pyautogui.pixelMatchesColor(148,878,(99,45,21)) == True:#免费按钮
        pyautogui.click(148,878)
        time.sleep(0.4)
#to set the position code
home =  (60,965)
mail = 119,172
mail2need2 =  424,870


eventButton = 521,254 #570248
eventButtonX = 359-359+570
eventButtonY = 1007-1007+248
superButton = (359-(359-178),1007-(1007-326)) #178326

ninmunumber1 = 456,419 #493 423
ninmunumber2 = 464,512 #494 528

#need time sleep 10-
zhuzaofinish = 0
#判断挂机结果画面 如果不是,跳过
def Opening():
    time.sleep(1)
    if pyautogui.pixelMatchesColor(429,320,(200,112,60)) == True:
        pyautogui.click(50,976)
        time.sleep(3)

    #判断每月活动
    if pyautogui.pixelMatchesColor(102,489,(246,234,206)) == True:
        while pyautogui.pixelMatchesColor(210,959,(171,171,173)) == False:
            pyautogui.click(210,959)
            time.sleep(0.2)
        time.sleep(0.2)
        pyautogui.click(532,112)
        time.sleep(3)

    #一朝一夕
    if pyautogui.pixelMatchesColor(240,549,(59,46,72)) == True:
        pyautogui.click(261,759)
        while pyautogui.pixelMatchesColor(201,389,(55,43,68)) == False:
            continue
        time.sleep(0.3)
        pyautogui.moveTo(201,389)
        time.sleep(0.3)
        pyautogui.drag(100,0,2,button="left")
        while pyautogui.pixelMatchesColor(130,287,(249,169,157)) == False:
            continue
        time.sleep(0.2)
        pyautogui.click(67,973)#关闭抽签结果
        time.sleep(0.5)
        pyautogui.click(455,386)#关闭抽签元宝购入窗口
        time.sleep(2)

    #首次启动新人物界面
    while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
        pyautogui.click(54,987)
        time.sleep(0.2)
    time.sleep(0.2)



    while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
        if pyautogui.pixelMatchesColor(473,890,(116,107,99)) == True:
            pyautogui.click(278,963)
            time.sleep(0.5)
            pyautogui.click(536,117)
            time.sleep(0.5)
            pyautogui.click(532,116)
            time.sleep(1)
        pyautogui.click(516,116)
        time.sleep(0.5)
        pyautogui.click(57,975)
        time.sleep(1)

    #もし装備がいっぱいになりました。
    for i in range(1):
        if pyautogui.pixelMatchesColor(353,949,(165,180,204),tolerance=30) == True:
            pyautogui.click(318,980)
            while pyautogui.pixelMatchesColor(263,869,(35,40,61)) == False:
                continue
            time.sleep(0.2)
            pyautogui.click(263,869)
            time.sleep(0.5)
            pyautogui.click(138,876)
            time.sleep(0.5)
            pyautogui.click(182,672)
            time.sleep(0.5)
            pyautogui.click(403,682)
            time.sleep(0.5)
            pyautogui.click(403,612)
        #クイックホーム戻る
            while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
                pyautogui.click(54,987)
                time.sleep(0.2)
        time.sleep(0.5)


    while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
        pyautogui.click(54,987)
        time.sleep(0.2)

    time.sleep(0.5)
    return

def checkifboss():
#    while pyautogui.pixelMatchesColor(449,411,(243,243,244),tolerance=5) == False:
#        continue
    global ninmunumber2
    global ninmunumber1
    global zhuzaofinish

    #这是BOSS扫讨


    if pyautogui.pixelMatchesColor(78,399,(14,41,143)) == True:
        print("boss扫讨开始")
        pyautogui.click(460,415)#点击训练所
        while pyautogui.pixelMatchesColor(470,577,(141,102,148)) == False:
            continue#等待训练所界面
        time.sleep(0.5)

        pyautogui.click(470,577) #dianji diyige touxiang
        while pyautogui.pixelMatchesColor(450,484,(99,160,195)) == False:
            continue#等待训练所挑战界面
        time.sleep(0.2)

        pyautogui.click(441,480)# 点击最大,把次数提升至3
        time.sleep(0.2)
        pyautogui.click(269,679)# 点击扫讨开始
        while pyautogui.pixelMatchesColor(277,654,(219,209,168)) == False:
            continue
        while pyautogui.pixelMatchesColor(188,44,(160,255,255),tolerance=10) == False:
            pyautogui.click(home)
        time.sleep(0.2)
    #クイックホーム戻る
        return
    if pyautogui.pixelMatchesColor(364,402,(186,134,99)) == True:
        #第一行は高速戦闘の場合
        ninmunumber1=ninmunumber2

    #装備強化画面の場合
    if pyautogui.pixelMatchesColor(468,471,(155,55,11),tolerance=5) == True and pyautogui.pixelMatchesColor(84,504,(236,219,52),tolerance=5) == True:
        pyautogui.click(476,516)
        while pyautogui.pixelMatchesColor(534,130,(247,149,43)) == False:
            continue
        time.sleep(0.2)
        pyautogui.click(456,137) #第４副将をクリック
        time.sleep(1.5)
        pyautogui.click(490,408)#胴クリック
        while pyautogui.pixelMatchesColor(437,285,(255,255,255)) == False:
            continue
        time.sleep(0.2)
        pyautogui.click(437,285)
        while pyautogui.pixelMatchesColor(170,673,(253,254,254)) ==False:
            continue
        time.sleep(0.2)
        for i in range (3):
            pyautogui.click(170,673)
            time.sleep(1)
    #クイックホーム戻る
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        return

    #副将訓練の判断：
    if pyautogui.pixelMatchesColor(101,514,(239,212,127))==True and\
         pyautogui.pixelMatchesColor(259,505,(211,181,151)) == False:
        print("副将訓練開始（3回）")
        pyautogui.click(427,517)
        while pyautogui.pixelMatchesColor(59,683,(143,106,48)) == False:
            continue
        time.sleep(0.1)
        pyautogui.click(59,683)
        time.sleep(0.5)

        
        if pyautogui.pixelMatchesColor(272,792,(254,255,255))==True:
            print("检测到第一副将不可训练,进行点击第二副将")
            pyautogui.click(515,213)
            while pyautogui.pixelMatchesColor(502,589,(155,111,61))==False:
                continue
            time.sleep(0.2)
            pyautogui.click(275,135)#Number 3 charctar 
            time.sleep(0.5)
        
        if pyautogui.pixelMatchesColor(272,792,(254,255,255))==True:
            print("检测到第二副将不可训练,进行点击第三副将")
            pyautogui.click(515,213)
            while pyautogui.pixelMatchesColor(502,589,(155,111,61))==False:
                continue
            time.sleep(0.2)
            pyautogui.click(352,135)#Number 3 charctar 
            time.sleep(0.5)


        pyautogui.click(59,683)
        while pyautogui.pixelMatchesColor(127,695,(228,94,108)) == False:
            #訓練書待ち
            continue
        time.sleep(0.2)
        
        for i in range (3):
            pyautogui.click(122,698) #click 訓練書１
            time.sleep(0.7)
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        print("156訓練書完了")
        time.sleep(0.2)
        return
    #遊歴の判断
    if pyautogui.pixelMatchesColor(83,501,(138,30,28))==True:
        print("遊歴開始")
        pyautogui.click(452,511)
        time.sleep(1)
        pyautogui.click(484,579)
        time.sleep(1)
        pyautogui.click(477,369)
        time.sleep(1)
        pyautogui.click(463,524)
        time.sleep(1)
        pyautogui.click(450,493)
        time.sleep(1)
        pyautogui.click(463,524)
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        print("遊歴完了")
        return


        #遊歴完了




    

    elif pyautogui.pixelMatchesColor(71,506,(203,156,63)) == pyautogui.pixelMatchesColor(367,476,(199,183,155)) == True:
        pyautogui.click(463,519)
        while pyautogui.pixelMatchesColor(294,500,(252,224,9)) == False:
            continue
        time.sleep(0.2)
        pyautogui.click(161,870)
        while pyautogui.pixelMatchesColor(390,522,(131,61,136)) == False:
            continue
        time.sleep(0.2)
        pyautogui.click(157,679) #点击所有
        time.sleep(0.2)
        pyautogui.click(408,682) #点击HAI
        while pyautogui.pixelMatchesColor(420,587,(28,54,72)) == False:#等待铸造确认界面
            continue
        time.sleep(0.2)
        pyautogui.click(366,595)#点击铸造,下一步返回主页面
        quickreturn()
        return()


    elif pyautogui.pixelMatchesColor(100,480,(236,127,151)) == True:
        print("訓練所開始")
        pyautogui.click(460,516)#点击训练所
        while pyautogui.pixelMatchesColor(51,589,(248,213,135)) == False:
            continue#等待训练所界面
        time.sleep(0.2)

        pyautogui.click(158,461) #dianji diyige touxiang
        while pyautogui.pixelMatchesColor(378,727,(133,6,15)) == False:
            continue#等待训练所挑战界面
        time.sleep(0.2)
        pyautogui.click(165,781) #dianji gaosu tiaozhan
        while pyautogui.pixelMatchesColor(466,486,(198,240,238)) == False:
            continue#等待告诉扫讨界面
        time.sleep(0.2)
        pyautogui.click(441,480)# 点击最大,把次数提升至3
        time.sleep(0.2)
        pyautogui.click(269,679)# 点击扫讨开始
        while pyautogui.pixelMatchesColor(277,654,(219,209,168)) == False:
            continue
        while pyautogui.pixelMatchesColor(188,44,(160,255,255),tolerance=10) == False:
            pyautogui.click(home)
        time.sleep(0.2)
    #クイックホーム戻る
        return
        # xunliansuo wanbi fanhui zhucaidan
    elif pyautogui.pixelMatchesColor(387,602,(251,252,252)) == True:
        pyautogui.click(387,602)
        time.sleep(0.3)
    elif  pyautogui.pixelMatchesColor(79,511,(227,203,39)) == pyautogui.pixelMatchesColor(255,507,(169,100,62))==True: #闘技場と判断しました
        print("闘技場開始（全5回）")
        pyautogui.click(470,519)
        while pyautogui.pixelMatchesColor(467,537,(85,59,39)) == False:
            continue
        time.sleep(0.2)
        pyautogui.click(475,644)#3番人挑戦
        time.sleep(0.5)
        if pyautogui.pixelMatchesColor(122,599,(122,38,38)) == True:
            print("同盟メンバーです・")
            pyautogui.click(122,599)
            time.sleep(0.5)
            pyautogui.click(467,533)
        while pyautogui.pixelMatchesColor(484,966,(255,255,234)) == False:
            continue
        time.sleep(1)
        pyautogui.click(479,958)#スキップ
        time.sleep(1)
        pyautogui.click(290,788)#クリックして閉じる

        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        time.sleep(1)
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        time.sleep(0.5)
    elif  pyautogui.pixelMatchesColor(317,531,(167,97,59)) == True:
        print("Twitter share")
        pyautogui.click(440,512)
        while pyautogui.pixelMatchesColor(136,289,(218,1,12)) == False:
            continue#等待主人物界面
        time.sleep(0.2)
        pyautogui.click(416,291)
        while pyautogui.pixelMatchesColor(179,993,(255,255,255)) == False:
            continue#等待 Twitter 画面
        time.sleep(0.2)
        pyautogui.click(583,921)
        quickreturn()
        return

    else:
        global checkn
        print(checkn)
        print(349)
        if checkn != 1:
            checkn = 1
            pyautogui.click(522,85)
            time.sleep(0.5)
            pyautogui.click(524,69)
            time.sleep(0.2)
            print(checkn)
            print(357)
            return
        else:
            checkn = 0
            print("此账号任务结束,等待10秒切换下一个账号")
            time.sleep(10)
            print("正在切换....等待主窗口")
            pyautogui.click(587,1004)
            while pyautogui.pixelMatchesColor(1136,268,(81, 81, 81)) == False:
                continue
            print("已定位关闭按钮")
            time.sleep(0.5)
            pyautogui.click(1136,268)
            while pyautogui.pixelMatchesColor(292,487,(82,35,68)) == False:
                continue
            print("已定位放置少女图标")
            time.sleep(0.5)
            pyautogui.click(292,489)
            print("已点击程序图标,下一步窗口靠边对齐")
            while pyautogui.pixelMatchesColor(587,15,(36,119,175)) == False:
                continue
            print("已定位NoxPlayer位置")
            time.sleep(0.5)
            pyautogui.moveTo(579,10)
            time.sleep(0.5)
            pyautogui.drag(-556,0,3,button="left") #556还是 557
            while pyautogui.pixelMatchesColor(268,824,(109,92,150)) == False:
                print("等待游戏加载Loading...")
                time.sleep(0.3)
                continue
            time.sleep(0.2)
            pyautogui.click(268,824)#点击关闭
            time.sleep(0.5)
            pyautogui.click(297,830)#点击服务器,进入服务器选择列表
            time.sleep(1)
            pyautogui.click(426,332)#点击最后一个人物
            time.sleep(0.5)
            pyautogui.click(287,884)#点击开始按钮进入游戏
            time.sleep(15)
         #   pyautogui.click(230,964)#关闭挂机结果
          #  time.sleep(5)

            return




def clickMail():
    if pyautogui.pixelMatchesColor(139,158,(255,101,104)) == True:
        pyautogui.click(mail)
        while pyautogui.pixelMatchesColor(401,874,(248,248,249)) == False:
            continue
        pyautogui.sleep(0.3)
        pyautogui.click(401,874)
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        time.sleep(0.2)




  #to click red button




def clickHome():
    pyautogui.click(home)
    time.sleep(0.8)


def muryouButton():
    # if new charactor
    print(344)
    if pyautogui.pixelMatchesColor(432,241,(250,95,110),tolerance=20) == True:#如果新人宝箱可以点
        pyautogui.click(432,241)
        time.sleep(1)
        pyautogui.click(432,241)
        time.sleep(1)
    mianfeianniu()
    if pyautogui.pixelMatchesColor(207,59,(255,72,79)) == True:#如果第二窗口为红色
        pyautogui.click(207,59)
        time.sleep(0.5)
        mianfeianniu()
        if pyautogui.pixelMatchesColor(432,241,(250,95,110),tolerance=20) == True:#如果新人宝箱可以点
            pyautogui.click(432,241)
            time.sleep(1)
            pyautogui.click(432,241)
            time.sleep(1)
    if pyautogui.pixelMatchesColor(311,60,(255,67,74)) == True:
        pyautogui.click(311,60)
        time.sleep(0.5)
        mianfeianniu()
        if pyautogui.pixelMatchesColor(432,241,(250,95,110),tolerance=20) == True:#如果新人宝箱可以点
            pyautogui.click(432,241)
            time.sleep(1)
            pyautogui.click(432,241)
            time.sleep(1)
    if pyautogui.pixelMatchesColor(413,62,(253,44,57)) == True:#如果第四窗口为红色
        pyautogui.click(413,62)
        time.sleep(0.5)
        mianfeianniu()
        if pyautogui.pixelMatchesColor(432,241,(250,95,110),tolerance=20) == True:#如果新人宝箱可以点
            pyautogui.click(432,241)
            time.sleep(1)
            pyautogui.click(432,241)
            time.sleep(1)
    #もし　百科美人の場合

    if pyautogui.pixelMatchesColor(444,885,(94,37,17)) == True:
        print("百花美人362")
        #上段無料
        if pyautogui.pixelMatchesColor(339,565,(81,29,15)) == True:
            pyautogui.click(339,565)
            time.sleep(0.8)
            while pyautogui.pixelMatchesColor(191,870,(45,23,31)) == False:
                pyautogui.click(191,870)
                time.sleep(0.1)
        time.sleep(0.4)
        if pyautogui.pixelMatchesColor(87,820,(81,29,14)) == True:
            pyautogui.click(87,820)
            time.sleep(0.8)
            while pyautogui.pixelMatchesColor(191,870,(45,23,31)) == False:
                pyautogui.click(191,870)
                time.sleep(0.1)
        #下段無料3回
        time.sleep(0.4)
        while pyautogui.pixelMatchesColor(359,818,(91,45,24)) == True:
            pyautogui.click(356,818)#点击无料
            time.sleep(1)
            while pyautogui.pixelMatchesColor(156,643,(80,34,18)) == True:
                #如果无料继续
                pyautogui.click(156,643)
                time.sleep(1)
            quickreturn()
            return
        else:
            while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
                pyautogui.click(54,987)
                time.sleep(0.2)
            return
    else:
        pass

    #もし　特典の場合?这是什么
    if pyautogui.pixelMatchesColor(359-338+37,1007-1010+415,(72,28,40),tolerance=10) == True and\
        pyautogui.pixelMatchesColor(359-338+387,1007-1010+416,(75,33,42),tolerance=10) == True:
        time.sleep(1)
        print(408)
        if pyautogui.pixelMatchesColor(448,60,(255,77,86)) == True:
            pyautogui.click(448,60)
            while pyautogui.pixelMatchesColor(268,872,(95,39,17)) == False:
                continue
            time.sleep(0.2)
            pyautogui.click(268,872)


        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        time.sleep(0.5)
        return

    #もし少女の出会い
    if pyautogui.pixelMatchesColor(465,92,(255,159,188))==True:
        print("少女的邂逅497")
        time.sleep(0.5)
        mianfeianniu()
        quickreturn()
        return

    #兵甲工房
    if pyautogui.pixelMatchesColor(455,55,(211,147,84)) == True:
        time.sleep(0.5)
        if pyautogui.pixelMatchesColor(147,875,(90,37,18)) == True:#如果无料可以点
            pyautogui.click(147,875)
            time.sleep(2)
            pyautogui.click(282,877)
            time.sleep(2)
        if pyautogui.pixelMatchesColor(337,751,(160,119,78)) == False:#如果70级闪红 则点70级按钮
            pyautogui.click(337,751)
            time.sleep(2)
        if pyautogui.pixelMatchesColor(147,875,(90,37,18)) == True:#如果无料可以点
            pyautogui.click(147,875)
            time.sleep(2)
            pyautogui.click(282,877)
            time.sleep(2)
        if pyautogui.pixelMatchesColor(498,750,(166,123,81)) == False:#如果85级闪红 则点85级按钮
            pyautogui.click(498,750)
            time.sleep(2)
        if pyautogui.pixelMatchesColor(147,875,(90,37,18)) == True:#如果无料可以点
            pyautogui.click(147,875)
            time.sleep(0.5)
        quickreturn()
        return
    if pyautogui.pixelMatchesColor(515,418,(78,86,155)) == True:
        print("甄姬的祝福")
        if pyautogui.pixelMatchesColor(155,871,(77,26,14)) == pyautogui.pixelMatchesColor(123,170,(41,31,107)) == True:
            pyautogui.click(149,875)
            time.sleep(1)
            pyautogui.click(291,876)
            time.sleep(1)
            if pyautogui.pixelMatchesColor(155,871,(77,26,14))==pyautogui.pixelMatchesColor(123,170,(41,31,107)) == True:
                pyautogui.click(149,875)
            time.sleep(0.2)
        quickreturn()
        return

    if pyautogui.pixelMatchesColor(437,75,(128,186,28)) == True:#幸運舞込む（土日月）
        if datetime.now().weekday() == 5:
            pyautogui.click(430,501)
        elif datetime.now().weekday() == 6:
            pyautogui.click(437,662)
        elif datetime.now().weekday() == 0:
            pyautogui.click(456,837)
        else:
            print("457幸運舞エラー")
            sys.exit(0)
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)
        print("幸運舞完了")
        return
        
    else:
        print(509)
        pass

###########################



def clickNinmu():
    pyautogui.click(292,723)#点击任务按钮
    while pyautogui.pixelMatchesColor(493,124,(1,1,0)) == False:
        continue
    time.sleep(0.2)
    #如果任务页面是MAIN或者功绩页面 而不在Daily上的话
    if pyautogui.pixelMatchesColor(200,227,(38,30,26)) == False:
        pyautogui.click(198,125)
        time.sleep(0.2)
    
    while pyautogui.pixelMatchesColor(430,406,(37,86,61),tolerance=5) == True:
        time.sleep(0.5)
        pyautogui.click(430,406)
        time.sleep(0.5)
        while pyautogui.pixelMatchesColor(520,125,(1,1,0)) == False:
            pyautogui.click(520,125)
            time.sleep(0.3)
        time.sleep(0.2)
    time.sleep(0.7)



#有领取按钮时循环领取

    #有宝箱达成时,拿取宝箱
    if pyautogui.pixelMatchesColor(83,218,(255,255,150),tolerance=30) == True:
        pyautogui.click(83,218)#宝箱1
        time.sleep(0.5)
        while pyautogui.pixelMatchesColor(520,125,(1,1,0)) == False:
            pyautogui.click(520,125)
            time.sleep(0.3)
        time.sleep(0.2)
    time.sleep(0.7)
    


    #宝箱2需要重写


   # 宝箱3
    if pyautogui.pixelMatchesColor(432,214,(255,245,100),tolerance=40) == True:
        pyautogui.click(455,224)
        time.sleep(0.5)
        while pyautogui.pixelMatchesColor(520,125,(1,1,0)) == False:
            pyautogui.click(520,125)
            time.sleep(0.3)
    return

    #100de baoxiang　もし100活躍度の宝ハコ Here must be fixed.


def Event():
    while pyautogui.pixelMatchesColor(533,236,(255,85,95),tolerance=50) == True:
        pyautogui.click(eventButton)
        time.sleep(1)
        if pyautogui.pixelMatchesColor(132,57,(255,54,65)) == True:
            pyautogui.click(132,57)
            time.sleep(0.5)
            continue
        while pyautogui.pixelMatchesColor(529,90,(219,94,70)) == False:
            continue#等待EVENT页面
        print(593)
        time.sleep(0.5)
        muryouButton()
        while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
            pyautogui.click(54,987)
            time.sleep(0.2)


def checkIconVip():
    if pyautogui.pixelMatchesColor(322,50,(255,65,74)) == True:
        pyautogui.click(322,50)
        while pyautogui.pixelMatchesColor(144,387,(236,21,36))==False:
            continue
        time.sleep(0.2)
        pyautogui.click(112,402)
        while pyautogui.pixelMatchesColor(522,85,(249,234,234))==False:
            continue
        time.sleep(0.2)
        pyautogui.click(90,932)
        while pyautogui.pixelMatchesColor(464,308,(83,63,64)) == False:
            pyautogui.click(524,84)
            time.sleep(0.1)
        time.sleep(0.1)
        while pyautogui.pixelMatchesColor(189,48,(139,244,246)) == False:
            pyautogui.click(49,974)
            time.sleep(0.1)
        time.sleep(0.2)


def RedButtonOnScreen():
    if pyautogui.pixelMatchesColor(359-372+193,1007-999+317,(255,100,100),tolerance=30) == True:
        pyautogui.click(359-372+193,1007-999+317)
        time.sleep(1)#Super pack 如果红色
        pyautogui.click(359-372+88,1007-999+418)
        time.sleep(1)
        pyautogui.click(home)
        time.sleep(1)
    if pyautogui.pixelMatchesColor(40,328,(143,67,81)) == True:
        pyautogui.click(40,328)
        while pyautogui.pixelMatchesColor(356,764,(226,157,2)) == False:
            continue
        time.sleep(0.3)#一朝一夕 如果红色
        pyautogui.click(356,764)
        while pyautogui.pixelMatchesColor(287,333,(140,121,137)) == False:
            continue
        time.sleep(0.3)
        pyautogui.moveTo(205,409)#需要拖拽
        time.sleep(0.5)
        pyautogui.drag(100,0,1,button="left")
        time.sleep(1)
        quickreturn()
        return
    else:
        return
def checkTokuten():
    if pyautogui.pixelMatchesColor(426,750,(255,66,75)) == True:
        pyautogui.click(426,750)
        time.sleep(0.8)
        if pyautogui.pixelMatchesColor(446,62,(255,50,65)) == True:
            pyautogui.click(446,57)
            print("特典月のギフト　585実行")
            while pyautogui.pixelMatchesColor(143,869,(150,101,58)) == False:
                continue
            time.sleep(0.2)
            pyautogui.click(143,869)
            while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
                pyautogui.click(54,987)
            time.sleep(0.2)
            return
        time.sleep(3)
        return
    else:
        return

def checkDOUMEI():
    if pyautogui.pixelMatchesColor(532,946,(255,87,93)) == True:#如果同盟闪红
        pyautogui.click(532,946) #点击同盟
        while pyautogui.pixelMatchesColor(401,179,(223,184,22)) == False:
            continue#等待同盟窗口
        time.sleep(0.4)
        pyautogui.click(412,179)#城堡管理
        time.sleep(0.2)
        if pyautogui.pixelMatchesColor(411,161,(104,53,14)) == True:
            print("同盟无城堡奖励,返回主界面752")
            while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
                pyautogui.click(54,987)
                time.sleep(0.2)
            return
        while pyautogui.pixelMatchesColor(536,906,(27,195,119)) == False:
            continue#等待城堡管理页面
        time.sleep(0.2)
        if pyautogui.pixelMatchesColor(273,859,(158,164,169)) == True:
            
            pyautogui.click(273,859)
        else:
            pyautogui.click(222,126)
            time.sleep(0.4)
            pyautogui.click(273,859)
    while pyautogui.pixelMatchesColor(189,42,(173,255,255)) == False:
        pyautogui.click(54,987)
        time.sleep(0.2)
    return



while True:
#    RedButtonOnScreen()
    Opening()
    Event()
    checkIconVip()
    checkTokuten()
    checkDOUMEI()
    clickMail()
    clickNinmu()
    checkifboss()



