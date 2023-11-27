# z-jarvis-z
def gcd(a,b):
    if a<b:
        c=a
        a=b
        b=c
    while(True):
        c=a%b
        d=a/b
        if c==0:
            return b
        a=b
        b=c
def theinput():
    a=eval(input())
    b=eval(input())
    print("{0:.2f} {1:.2f}".format(gcd(a,b),a*b/gcd(a,b)))
theinput()

