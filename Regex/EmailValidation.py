import re
mail = str(input("enter your mail: "))
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern , mail):
    print("Valid")
else :
    print("Invalid")
