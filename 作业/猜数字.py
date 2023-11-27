import random
value = random.randint(0,100)
a = eval(input("猜")) 
while 1:
    if a == value :
        print("对了")
        break
    elif a<value :
        print("小了")
    elif a>value :
        print("大了")
    a = eval(input("猜")) 