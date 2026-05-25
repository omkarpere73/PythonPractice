import re
# remove star
print(re.findall(r"ab*", "ab abb abbb a"))

print(re.findall(r"ab+", "ab abb abbb a"))

print(re.findall(r"colou?r", "color colour"))