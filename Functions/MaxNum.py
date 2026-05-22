def maxnum(numbers):
    max_num = numbers[0]

    for num in numbers:
        if num > max_num :
            max_num = num

    return max_num

res = maxnum([4,7,1,22,4,33,98])
print(res)