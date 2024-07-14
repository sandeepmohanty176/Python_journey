# python script to calculate the lcm of the given number
a=int(input("Enter a number: "))
b=2
c=1
while a>1 and b<=a:
    if a%b==0:
        a=a//b
        c=c*b
    else:
        b+=1
print(c)