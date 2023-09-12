# 华氏转摄氏和摄氏转华氏
def transformtemerature():
    temp = input("输入带标记温度（例93f）")
    # if temp[-1]=="f"||temp[-1]="F"
    if temp[-1] in ['f','F']:
        c=(eval(temp[:-1])-32)/1.8
        print("相应的摄氏温度是{:.2f}".format(c))
    elif temp[-1] in ['c','C']:
        c=(eval(temp[:-1])*1.8)+32
        print("相应的华氏温度是{:.2f}".format(c))
    else:
        print("输入格式有误")
transformtemerature()