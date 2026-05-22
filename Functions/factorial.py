def factorial(n):

    if n == 0:
        return 1
    else :
        res = n * factorial(n - 1)
        return res

n = int(input("Enter a number: "))
res = factorial(n)
print(res)

