c=0
for a in range(1,5000):
    temp=a
    x=len(str(a))
    while a!=0:
        rem=a%10
        c=c+(rem**x)
        a=a//10
    if temp==c:
        print(c,end=",")
    
    c=0