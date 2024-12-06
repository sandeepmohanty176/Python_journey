def power(base,powerr):
    if powerr==0:
        return 1
    return base*power(base,powerr-1)
print(power(2,5))    