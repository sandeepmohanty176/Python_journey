#FACTORIAL OF A GIVEN NUMBER
a=int(input("entera number: "))
i=1
s=1
print("Factorial of the given number",a,"is")
while i<=a:
    s=s*i
    i=i+1
print(s)