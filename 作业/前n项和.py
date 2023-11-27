value =eval(input())
a=1
b=1
result=1
if value < 2 :
    result=1
else:
    for i in range (1,value):
        x=i
        y=a+b
        a=b
        b=y
        result +=x/y*pow(-1,i)
print("{:.6f}".format(result))