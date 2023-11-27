from turtle import *

# 将画笔抬起，移动到起始位置，再将画笔放下
up()
setpos(-150, 20)
down()

# 旋转画笔方向，开始画第一个等边三角形
left(30)
fd(100)
left(60)
for i in range(5):
    fd(100)
    right(120)
    fd(100)
    left(60)

# 画出最后一个等边三角形和最后的线段
fd(100)
right(120)
fd(100)
for n in range(6):
    fd(100)
    right(60)

done()