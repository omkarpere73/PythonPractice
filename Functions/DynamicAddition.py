def addition(*numbers):

    total = 0

    for num in numbers:
        total += num

    return total


print(addition(1,2,3,4))