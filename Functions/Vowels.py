def vowels(text):
    count = 0

    for char in text:
        if char.lower() in 'ieaou':
            count += 1

    return count

text = input("Enter a string: ")
print(vowels(text))

