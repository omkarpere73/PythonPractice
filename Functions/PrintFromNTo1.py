def printnumbers(n):
    if n == 0:
        return "Zero"

    print(n)
    printnumbers(n-1)

n = int(input("Enter a number: "))
printnumbers(n)