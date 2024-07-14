#check prime number or not
a=int(input("Enter a number:"))
i=2
while i<a:
    if a%i==0:
        print("NOT PRIME")
        break
    i=i+1
    
else:
    print("PRIME")