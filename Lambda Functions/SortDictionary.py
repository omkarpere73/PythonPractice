data = {
    "A": 50,
    "B": 20,
    "C": 80
}

sorted_data = sorted(data.items(), key = lambda x:x[1])
print(sorted_data)