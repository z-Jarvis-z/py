import turtle

# 设置初始值
length = 5
angle = 90
increment = 2

# 创建画布
turtle.setup(600, 600)

# 创建画笔
pen = turtle.Pen()
pen.speed(0)

# 绘制正方形螺旋线
for i in range(100):
    pen.forward(length)
    pen.left(angle)
    length += increment

turtle.done()
