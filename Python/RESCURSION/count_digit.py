a=int(input("enter a nmber: "))
def count(a):
    if a==0:
        return 0
    return 1+count(a//10)

print(count(a))
    