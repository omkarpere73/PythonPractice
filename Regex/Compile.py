import re

pattern = re.compile(r"\d+")

result = pattern.findall("Age 20 and 30")

print(result)