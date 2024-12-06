# lambda is nothing but a function without name
# factorial of any number using almbda
# lambda is only used for reduce function
f=lambda n:1 if n==0 or n==1 else n*f(n-1)
print(f(5))