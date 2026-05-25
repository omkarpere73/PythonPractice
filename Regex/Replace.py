import re

text = "I love Python"

res = re.sub("Python" , "Java" , text)

print(res)