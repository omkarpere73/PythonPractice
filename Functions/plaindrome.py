def palindrome(text):
    if text == text[::-1]:
        return "PALINDROME"
    else :
        return "NOT PALINDROME"

print(palindrome("Omkar"))