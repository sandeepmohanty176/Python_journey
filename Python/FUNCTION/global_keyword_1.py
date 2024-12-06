x=89
def a():
    global x
    x=6
    print(x)

print(x)
#here if we call the function a() first then x=6 will be the global variable in the next when u want to print the value of global variable i.e 89 then it will also print x=6. But if you write print(x) first then call the function a() then it will print first x=89 and then will print value of x=6 which is inside the function. Aftre the function call the x value inside the function will be the global variable

# overally if u used the global key word inside the function then, when you acess the x value after that function call then that x value bacomes the global value insteade of local variable.
a()
print(x)