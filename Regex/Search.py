import re

text = "Python Java C"

result = re.search("Java" , text)

if result:
    print("Found")
else:
    print("Not Found")