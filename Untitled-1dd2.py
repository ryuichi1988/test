from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    dot(5,"red")
    if abs(pos()) < 1:
        break
end_fill()
done()