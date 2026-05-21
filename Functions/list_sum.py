def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

print(list_sum([1,2,3,4,5,6,7]))