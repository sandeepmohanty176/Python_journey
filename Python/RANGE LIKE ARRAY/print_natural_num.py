#print n natural num
a=int(input("enter a number: "))
for e in range(1,a+1): #bydefault if range is(1,9) then it will print 1 to 8 last value is excluded.
    print(e**2,end=",")
    