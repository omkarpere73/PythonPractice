import re

text = " Python is Good"

result = re.match("Python" , text)

if result:
    print("Matched")
else:
    print("Not Matched")