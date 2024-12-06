a=int(input("neter a number: "))
def natural(a):
    if a==0:
        return 0
    return a+natural(a-1)
print(natural(a))