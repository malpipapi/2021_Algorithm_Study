n = int(input())
def factorial(n):
    if n == 0:#n = 0 일 때 주의.
        return 1
    if (n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(n))