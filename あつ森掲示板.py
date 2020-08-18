import requests,bs4,os

f1 = requests.get("https://game8.jp/atsumare-doubutsunomori/330769")
f2 = bs4.BeautifulSoup(f1.text,"html.parser")
f3 = f2.find_all("div",class_="c-commentItem__body")
with open("commet.txt","w",encoding="UTF-8")as file1:
    for i in f3:
        file1.write("""
-------------------------\n\n\n\n\n\n{}
""".format(i.text))
os.system("commet.txt")