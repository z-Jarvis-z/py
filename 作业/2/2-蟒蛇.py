import turtle

# 设置画布大小和位置
turtle.setup(650, 350, 200, 200)

# 抬起画笔，移动到起始位置
turtle.penup()
turtle.fd(-250)

# 落下画笔，设置画笔宽度和颜色，调整方向
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)

# 循环绘制蟒蛇的每一段
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(4):
    turtle.pencolor(colors[i % len(colors)])  # 设置画笔颜色
    turtle.circle(40, 80)  # 绘制大圆弧
    turtle.circle(-40, 80)  # 绘制小圆弧

# 绘制蟒蛇头部
turtle.pencolor(colors[4 % len(colors)])  # 设置画笔颜色
turtle.circle(40, 80 / 2)  # 绘制半个大圆弧
turtle.fd(40)  # 前进一段距离
turtle.circle(16, 180)  # 绘制半个小圆弧
turtle.fd(40 * 2 / 3)  # 前进一段距离

# 关闭窗口
turtle.done()
