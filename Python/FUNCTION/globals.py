x=89
y=4
def a():
    x=6
    g=globals() #here value of global variable i.e 89 will store in g in the form of key value (used in dict e.g 'a':76,'b':90,'c':34,) 
    print(x) #here the the value of local variable i.e 6 will print
    print(g['x']) #here the value of global variable 89 will print again whn u call the function

print(x)
a()