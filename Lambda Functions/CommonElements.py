list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

common = list(filter(lambda x:x in list1 , list2))
print(common)