palindrome = lambda s: "Palindrome" if s == s[::-1] else "Not Palindrome"

print(palindrome("python"))
print(palindrome("madam"))