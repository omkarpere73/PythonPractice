import re

number = "9090909090"
pattern = r"^[6-9]\d{9}$"

if re.match( pattern , number):
    print("valid")

else:
    print("Invalid")