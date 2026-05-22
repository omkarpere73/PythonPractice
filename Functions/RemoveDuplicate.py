
def removeduplicate(numbers):
    unique = []

    for num in numbers:
        if num not in unique:
            unique.append(num)

    return unique

print(removeduplicate([1,1,2,3,3,4,5,6,7,7,8]))