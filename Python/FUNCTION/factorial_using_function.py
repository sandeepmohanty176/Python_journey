a=int(input("enter a number: "))
def fact():
    i=1
    j=1
    while i<=a:
        j=j*i
        i+=1
    print("Factorial of ",a,"is",j)
fact()