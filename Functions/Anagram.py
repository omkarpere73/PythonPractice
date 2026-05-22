def anagram(text1 , text2):
    text1 = text1.lower()
    text2 = text2.lower()

    if sorted(text1) == sorted(text2):
        print("Anagram")
    else:
        print("Not Anagram")

text1 = str(input("Enter a text 1: "))
text2 = str(input("Enter a text 2: "))
print = anagram(text1,text2)