def a():
    b,c=int(input("enter 1st number: ")),int(input("enter 2nd number: "))
    d=b+c #suppose b=2,c=8 then d=10
    return d #here d value will return where u will call the function name a()
s=a() #here that d value is return and store in s variable THE MAIN ADVANTAGE IS U CAN USE THE VALUE OF D ANYWHERE IN THE CODE //CODE REUSABILITY
print("sum is :",s)