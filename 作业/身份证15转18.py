sfz=list(map(int,input("输入十五位的身份证")))
if sfz[7]==1:
    sfz.insert(6,1)
    sfz.insert(7,9)
else:
    sfz.insert(6,2)
    sfz.insert(7,0)
wi=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
xy=[1,0,'x',9,8,7,6,5,4,3,2]
s=sum(wi[i]*sfz[i] for i in range(17) )
sfz.append(xy[s%11])
print(sfz)
