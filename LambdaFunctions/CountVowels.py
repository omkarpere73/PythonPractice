countvowels = lambda s : sum(1 for ch in s.lower() if ch in "aeiou")
print(countvowels("omkar"))