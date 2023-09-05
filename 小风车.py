import turtle
arraolor=["red","pink","green","yellow"]
turtle.pensize(0)
turtle.setup(1080,720)
turtle.delay(0)
turtle.speed(0)
turtle.hideturtle()
def draw():
    turtle.clear()
    for i in range(4):
        turtle.tracer(False)
        turtle.color(arraolor[i],arraolor[i])
        turtle.begin_fill()
        turtle.rt(45)
        turtle.fd(200)
        turtle.lt(90)
        turtle.circle(200,45)
        turtle.goto(0,0)
        turtle.end_fill()
    turtle.lt(10)   
    turtle.ontimer(draw,50)
draw()
input()