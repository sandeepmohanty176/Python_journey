#wap to reverse a string by word wise
a=input("enter a string: ")
x=a.split() #split function used
y=x[::-1] #slicing operator used
print("After reverse the string: "," ".join(y)) #join function used