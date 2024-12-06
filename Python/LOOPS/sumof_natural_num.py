#Sum of first N natural numbers
a=int(input('Enter any natural number:'))
i=1
s=0
print("natural numers are: ")
while i<=a:
    print(i,end=",")
    s=s+i
    i=i+1
print()
print("Sum is:",s)