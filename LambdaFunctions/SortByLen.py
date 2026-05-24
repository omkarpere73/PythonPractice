words = ["apple", "banana", "watermelon", "kiwi"]

sorted = list(sorted(words , key = lambda x: len(x) ,))
print(sorted)