#1st 10 odd natural number
def odd(n, current=1):
    if n > 0:
        print(current)
        odd(n - 1, current + 2)

# Example usage:
n = 5
odd(n)