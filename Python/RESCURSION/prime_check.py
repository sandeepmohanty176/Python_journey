a=int(input("enter any number: "))
def prime(a,i):
    if i==1:
        return 1
    if a%i==0:
        return 0
    return prime(a,i-1)
x=prime(a,a-1)
if x==0:
    print("not prime")
if x==1:
    print("prime")