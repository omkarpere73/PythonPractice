import re

text = "apple,banana;orange,grape"

res = re.split("[,;]" , text)

print(res)