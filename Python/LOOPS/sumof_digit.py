# python script to calculate the sum of the digit of a guven number
a=int(input("Enter a number: "))
b=0
while a>0:
    lstdgt=a%10
    b=b+lstdgt
    a=a//10
print("Sum of digit of the given number",b)