n=[50,75,34,68,77,96,45,569]
x=[]
def even(n):
    for a in n:
        if a%2==0:
            x.append(a)
    return x

    
print(even(n))