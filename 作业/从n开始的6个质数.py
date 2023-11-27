def prime(m):
    print('\n')
    cnt=0
    check=True
    while cnt<6:
        m +=1
        for i in range(2,int(m**0.5),1):
            if m%i == 0 :
                check=False
                break
        if check==True :
            cnt+=1
            print(m)
        else:
            check=True
    return
n = eval(input())
prime(n)