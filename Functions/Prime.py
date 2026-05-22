def prime(num):
    if num <= 1:
        return 'not prime'

    for i in range(2 , num ):
        if num % 2 == 0:
            return 'not prime'

    return 'prime'

num = int(input("Enter a number: "))
print(prime(num))