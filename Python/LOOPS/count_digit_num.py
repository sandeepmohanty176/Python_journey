#python scrip to count the digit of a given nuber
#logic hela b ra value 0 initialy num jetebele divided by 10 haba Quotient ra digit num ra digit ru 1- haba jete time divide haba setethara value jaiki b re +1 haba
num=int(input("Enter a number: "))
b=0
while num>0:
    num//=10
    b+=1
print("No of digit is:",b) #here if we write the print statement under b+=1 then in he o/p will show step by step means every time the value will store in b that will show here.
