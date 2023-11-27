from turtle import *

# 设置画布大小为 500*500
setup(500, 500)

for i in range(4):
    # 提笔，向前移动20像素
    up()
    fd(20)
    # 下笔，向前移动160像素
    pd()
    fd(160)
    # 提笔，向前移动20像素
    up()
    fd(20)
    # 向右旋转90度
    right(90)

done()
