import requests,urllib.request,os,sys,winsound,pyperclip,re,json
from bs4 import BeautifulSoup
from plyer import notification


print("\n\n\n\n\n\n")
# 引用requests模块
urlll = pyperclip.paste()#input("请粘贴网址:\n")
res_comments = requests.get(urlll)
f2 = BeautifulSoup(res_comments.text,"html.parser")

#params相关
f3 = f2.findAll("h2",class_="text-ellipsis")
f5=f3[0].findAll("a")
title=f5[0].text
title2=f5[1].text
titleepisode=f5[2]["data-pid"]
full_title0 = title+" "+title2+" "+titleepisode
full_title = full_title0.replace(" ","")
print("下载影片标题为"+full_title)

#params相关
f10 = f2.find("div",class_="embed-responsive embed-responsive-4by3")
f11 = f10.find("script")
f12 = f11.text

#f13 = (f12[74:90])
#url = "https://videos7.jsyunbf.com/share/"+f13
#print(url)

s = f12
a = r'"url":"(.*?)","copyright"'
slotList = re.findall(a, s)
#print(type(slotList[0]))
url2 = slotList[0].replace("\\","")
print("提取到的初始第一播放地址")
print(url2)

res_f20 = requests.get(url2)
f20_soup = BeautifulSoup(res_f20.text,"html.parser")
f21 = f20_soup.find_all("script")
f22 = f21[-1]
f23=f22.text
print("什么的长度")
print(len(f23))
b = r'url":"(.*?)"}]'

slotList2url2 = re.findall(b, f23)
if len(slotList2url2) == 0:
    print("播放总地址后半段第二方案")
    b = r'var main = "(.*?)\?sign='
    slotList2url2 = re.findall(b, f23)
else:
    print("播放总地后半段第一方案")
    pass
print("播放地址后半段为:")
print(slotList2url2)



c = r'var redirecturl = "(.*?)"'
slotList2url1 = re.findall(c,f23)
print(slotList2url1)    #主要地址(列表格式)
main_url = slotList2url1[0] #提取主要地址
FINALurl = (slotList2url1[0])+(slotList2url2[0])
print("合成后的主要播放地址 (总)")
print(FINALurl)    #合成后的主要播放地址 (总)

f30 = requests.get(FINALurl)
f31 = f30.text
print("解析response字符长度(str)")
print(type(f31))
print(len(f31))

listbbb = []
f32 = f31.split("\n")
print("下载地址的前10行")
print(f32[:10])
print("解析行数")
print(len(f32))
if len(f32) < 10:
    print("长度不符,更深层地址解析开始")
    f32 = slotList2url1[0] + f32[2]
    print("深层地址为")
    print(f32)
    f40 = requests.get(f32)
    f41 = f40.text
    f32 = f41.split("\n")
    print("下载地址的前10行")
    print(f32[:10])
    print("解析行数(整理前)")
    print(len(f32))
else:
    print("失败")
count = 0
for line in f32:
    while count > 999:
        break
    else:
        if "#" in line or len(line) == 0:
            #print(line)
            #print("continue")
            continue
        else:
            linee = main_url+line
            listbbb.append(linee)
            #print(linee)
            #print("已打印第{}行".format(count))
        count += 1
print("解析行数(整理后)")
print(len(listbbb))
print("下载首链接")
print(listbbb[0])
print("下载尾链接")
print(listbbb[-1])
print('''
#以上下载地址解析完毕


#以下开始写入文件
''')
#以上下载地址解析完毕



#以下开始写入文件
taskall = len(listbbb)+1
def save(string):
    i=0

    for Read_download_line in listbbb:

        index = str(listbbb.index(Read_download_line))
        indexx = index.zfill(4)
        saveDIR = "G:\\迅雷下载\\☆python下载\\"+indexx+'.ts'

        f = urllib.request.urlopen(Read_download_line)
        with open(saveDIR,'wb') as code:
            code.write(f.read())
        i = i+1
        taskpercentage = i/taskall * 100
        messageX = ("\r已下载{}/{},完成度{:.2f}%".format(i,taskall,taskpercentage))
        sys.stdout.write(messageX)
        sys.stdout.flush()
        notification.notify(
    title='进度通知',
    message=messageX,
    app_name='アプリ名だよ',
    timeout=1.1
 #   app_icon='./icon.jpg'
)


#合并ts为一个mp4 
def trans(name):
    cmd = 'copy /b G:\\迅雷下载\\☆python下载\\*.ts G:\\迅雷下载\\☆python下载\\'+name+'.mp4'
    os.system(cmd)
    os.system('del G:\\迅雷下载\\☆python下载\\*.ts')#删除所有ts
    os.system("start explorer G:\\迅雷下载\\☆python下载\\")


if __name__ == '__main__':
    os.system("start explorer G:\\迅雷下载\\☆python下载\\")
    save("1442")
    trans(full_title)
    print("\n----------------finish")
#os.system('shutdown -s -f -t 30') #需要关机的话---



