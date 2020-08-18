i = 0
x = 19+1
while i < 20:
    i+=1
    c = i/x*100
    print("已完成{}/{},进度{:.2f}%".format(i,x,c))
