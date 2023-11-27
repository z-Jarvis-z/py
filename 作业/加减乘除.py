# 郑健祥 z-jarvis-z
def multiple(a,b):
    return a*b
def div(a,b):
    return a/b
def plus(a,b):
    return a+b
minus = lambda a,b: a-b
while True:
    c=int(input("选择菜单\n1乘法2除法\n3加法4减法\n0退出\n"))
    if c==1:
        a,b= map(int, input("用空格隔开俩个数").split())
        print(multiple(a,b))
    elif c==2:
        a,b= map(int, input("用空格隔开俩个数").split())
        while b==0:
            b=int(input("除数不能为0请重新输入"))
        print(div(a,b))
    elif c==3:
        a,b= map(int, input("用空格隔开俩个数").split())
        print(plus(a,b))
    elif c==4:
        a,b= map(int, input("用空格隔开俩个数").split())
        print(minus(a,b))
    else:
        break