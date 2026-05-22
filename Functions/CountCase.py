def countcase(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1

        elif char.islower():
            lower += 1

    print("Total number of uppercase letters: ", upper)
    print("Total number of lowercase letters: ", lower)

text = str(input("Enter a text: "))
countcase(text)