import requests,bs4,webbrowser
#hjtv5 韩剧TV 连接
## searchword = input("请输入查询关键字")

url = "https://www.993dy.com/index.php?m=vod-search&wd=%E4%B8%9C%E4%BA%AC%E5%A4%A7%E9%A5%AD%E5%BA%97&submit=%E6%90%9C%E7%B4%A2%E5%BD%B1%E7%89%87"
f1 = requests.get(url)
f2 = bs4.BeautifulSoup(f1.text,"html.parser")
#以上固定

#寻找题目和连接信息
f3 = f2.find_all("h5")

#制作空列表
movietitles = []
links = []
n = 0
#查找各项
for i in f3:
    t1 = i.text #这是题目
    l1 = i.find("a") ######################连接查找 此处是关键
    l2=l1["href"] #######################定位连接 关键
    movieurl = ("https://www.993dy.com"+l2) #组合连接
    movietitles.append(t1) #写入题目列表
    links.append(movieurl) #写入连接列表
    print(movietitles)
    print(links)

#打印出结果
for i in movietitles:

    print("\n题目{}: [{}]".format(n,i))
    n+=1 


choise=input("输入需要查看的序列\n")


webbrowser.open(links[int(choise)])

