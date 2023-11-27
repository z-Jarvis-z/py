# 人民币和美元互相转换 郑健祥
def transformmoney():
    temp = input("输入带标记货币数量例100usd或100rmb")
    # if temp[-1]=="f"||temp[-1]="F"
    if temp[len(temp)-3:len(temp)] in ["usd","USD"]:
        c=(eval(temp[:-3]))*7.2894
        print("相应的人民币是{:.2f}".format(c))
    elif temp[len(temp)-3:len(temp)] in ["rmb","RMB"]:
        c=(eval(temp[:-3]))*0.1372
        print("相应的美元是{:.2f}".format(c))
    else:
        print("输入格式有误")
transformmoney()