str = input("请输入字符串：")
eng, chin, num, space, other = 0, 0, 0, 0, 0
for i in str:
    if '\u4E00' <= i <= '\u9FFF':
        chin += 1
    elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        eng += 1
    elif '0' <= i <= '9':
        num += 1
    elif i == " ":
        space += 1
    else:
        other += 1
print("中文字符有{}个\n英文字符有{}个\n数字有{}个\n空格有{}个\n其他字符有{}个".format(chin, eng, num, space, other))
