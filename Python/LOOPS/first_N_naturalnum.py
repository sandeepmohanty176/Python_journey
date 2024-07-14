#to print first n natural numbers means if we put 5 then it will print first 5 natual numbers if 10 then 1st 10 natural number
a=int(input("Enter a natual number:"))
i=1
print("The first",a,"Natural nubers are:")
while i<=a:
    print(i,end=",")      # End is used to show in a single line
    i+=1