# 定义一个函数，用于判断一个字符串是否是回文字符串
def is_palindrome(string):
    # 判断字符串是否和其反向拷贝相等，如果相等，则说明字符串是回文字符串，返回 True；否则返回 False
    return string == string[::-1]


# 获取用户输入的字符串
string = input("请输入一个字符串：")

# 调用函数判断字符串是否是回文字符串
palindrome = is_palindrome(string)

# 根据判断结果输出相应的信息
if palindrome:
    print(string, "是一个回文树！")
else:
    print(string, "不是一个回文数！")
