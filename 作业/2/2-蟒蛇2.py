from turtle import *

# 设置画布大小和颜色模式
setup(800, 800)
colormode(255)

# 设置画笔大小和速度
pensize(20)
speed(10)


def draw_snake():
    # 抬起画笔，设置初始位置为屏幕中心，放下画笔
    penup()
    setpos(0, 0)
    pendown()

    # 绘制蟒蛇
    for i in range(50):
        forward(2 * i)  # 前进距离随着i的增加而增加
        left(20)  # 左转20度
        # 随着绘制的进度改变颜色
        pencolor((255 - i, 50, i))

    hideturtle()  # 隐藏画笔


draw_snake()  # 调用函数绘制蟒蛇

done()  # 保持窗口不关闭，直到手动关闭
