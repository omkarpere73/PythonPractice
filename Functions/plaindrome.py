def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = str(input("Enter a text: "))
res = palindrome(text)
print(res)
