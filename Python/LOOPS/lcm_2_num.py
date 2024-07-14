# python script to calculate the lcm of the given number
a,b=int(input("Enter a number: ")),int(input("Enter second number: "))
c=2
d=1
while (a,b)>=1 and b<=(a,b):
    if a%c==0 and b%c==0:
        d*=c
        a=a//c
        b=b//c
    else:
        c+=1
print(c)