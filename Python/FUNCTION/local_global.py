y=7 # it is global variable because it is outside of any function and it can be acessible in any position of a given code
def a():
    x=9 #it is local variable because it is inside of any function and it can't be acessible in any position of a given code
    print(x+6)
def b():
    print(y)  # here u can't acess the value of x because it is a global variable
    
b()
a()