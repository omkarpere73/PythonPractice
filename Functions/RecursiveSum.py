def recursivesum(num):
    if num == 1:
        return 1

    return num + recursivesum(num - 1)

num = int(input("Enter a num :"))
print(recursivesum(num))