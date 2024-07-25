#create a list of first odd n natural number where n is given by the user
x=int(input("enter a number"))
print([a+1 for a in range(0,x*2,2)])