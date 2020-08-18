import requests,urllib.request,os,sys,winsound,pyperclip
from bs4 import BeautifulSoup
from plyer import notification



# 引用requests模块
urlll = pyperclip.paste()#获取剪切板地址
if len(urlll) == 33:
    ftitle = urlll[28:32]
elif len(urlll) == 32:
    ftitle = urlll[28:31]
else:
    ftitle = urlll[28:30]
print("movie title"+ftitle)
res_comments = requests.get(urlll)
f2 = BeautifulSoup(res_comments.text,"html.parser")

#params相关
f3 = f2.findAll("source")
key=(f3[0]["src"][28:260])
hash=(f3[0]["src"][267:-9])
vid=(f3[0]["src"][-4:])
params = {
        'key': key,
        'hash': hash,
        'vid': str(vid),        
    }

#得到params解密后全文
res_music = requests.get("http://m3u8.361lu.com/us.php", params=params)

#下载地址通用部分
urll=(res_music.text)[186:268]

#链接总数
taskall = int(res_music.text[-22:-19])+1

def save(string):
    i=0
    while True:
        indexx = str(i).zfill(3)
        index = indexx+'.ts' #补0
        saveDIR = "G:\\迅雷下载\\514151646\\"+index
        try: #不知道有多少ts文件，若存取失败则说明完成
            url = urll+index
            f = urllib.request.urlopen(url)
            with open(saveDIR,'wb') as code:
                code.write(f.read())
        except:
            break

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

def trans(name):
    cmd = 'copy /b G:\\迅雷下载\\514151646\\*.ts G:\\迅雷下载\\514151646\\'+name+'.mp4'#合并ts为一个mp4 
    os.system(cmd)
    os.system('del G:\\迅雷下载\\514151646\\*.ts')#删除所有ts
    os.system("start explorer G:\\迅雷下载\\514151646\\")


if __name__ == '__main__':
    os.system("start explorer G:\\迅雷下载\\514151646\\")
    save("1442")
    trans("600avs"+str(ftitle))
    print("\n----------------finish")
#os.system('shutdown -s -f -t 30')

