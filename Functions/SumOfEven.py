def sumofeven(numbers):
    sum = 0

    for num in numbers:
        if num % 2 == 0:
            sum += num

    return sum

res = sumofeven([1,2,3,4,5,6,7,8])
print(res)
