n = int(input("Enter a num : "))
gen = (x * 2 for x in range(n))

for value in gen:
    print(value)
