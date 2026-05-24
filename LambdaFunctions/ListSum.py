from functools import reduce

numbers = [1, 2, 3, 4]

reduced = reduce(lambda a , b : a + b , numbers)
print(reduced)