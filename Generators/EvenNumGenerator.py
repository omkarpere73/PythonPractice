def evengen(n):
    i = 1
    while i <= n:
        if i % 2 == 0:
            print(i)
        i += 1

n = int(input("Enter value of n  : "))
evengen(n)
