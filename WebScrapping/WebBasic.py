# web scraping using regex
import re
import urllib.request

# open the html file using urlopen() method
f = urllib.request.urlopen(r'file:////Users/omkar/PycharmProjects/PythonPractice/WebScrapping/Index.html')

# read data from the file object into text string
text = f.read()

# convert the byte string into normal string
str = text.decode()

# apply regular expression on the string
# here /s is for space
result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>', str)

# display result
print(result)

# display the items of the result
for item, price in result:
    print('Item= %-15s Price= %-10s' %(item, price))

# close the file
f.close()