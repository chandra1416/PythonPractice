print('<----------------------------<<Python Strings>>--------------------------->')
# Python Strings
print('Strings in python are surrounded by either single quotation marks, or double quotation marks.')
# 'hello' is same as "hello"
print("Hello")
print('Hello')
# Assign String to a Variable
a = 'Chandra'
print(a)
print('<--------Multiline Strings-------->')
# You can assign a multiline string to a variable by using three quotes:
# three double quotes:
b = """Chandra is a python developer ,
and he has 3 years of experience in IT field.
At present Chandra is working as System Engineer at TCS in Chennai Location."""
print(b)
print('<------------->')
# three single quotes:
c = """Chandra is a python developer ,
and he has 3 years of experience in IT field.
At present Chandra is working as System Engineer at TCS in Chennai Location."""
print(c)

print('Note: in the result, the line breaks are inserted at the same position as in the code.')
# Strings are Arrays
# Like many other popular programming languages,
# strings in Python are arrays of bytes representing unicode characters.
print('Python does not have a character data type, a single character is simply a string with a length of 1.')
# Square brackets can be used to access elements of the string.
d = "Hello, Chandra!"
print(d[1])
print('<------------>')
# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "Chandra":
    print(x)
print('String Length : Use the len() function.')
# To get the length of a string, use the len() function.
# The len() function returns the length of a string:
e = "Chandra is a Python Developer"
print(len(e))
print('<----Check String----->')
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "Python" is present in the following text:
f = "Chandra is a Python Developer"
print('Python' in f)
# Use it in an if statement:
g = "Chandra is a Python Devel"
if 'Python' in g:
    print('Yes, the word Python identified in text g')
print('<----Check if NOT----->')
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
h = "Chandra is a Python Developer"
print('python' not in h)
# Use it in an if statement:
i = "Chandra is a Python Devel"
if 'python' not in i:
    print('No, the word python not identified in text g')
print('<----------------------------<<Slicing Strings>>--------------------------->')
# Slicing : You can return a range of characters by using the slice syntax.
print('Specify the start index and the end index, separated by a colon, to return a part of the string.')
# Get the characters from position 2 to position 5 (not included):
j = "Hello, Chandra!"
print(j[2:5])
print('Note: The first character has index 0.')
print('Slice From the Start:')
# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):"
k = "Hello, Chandra!"
print(k[:5])
print('Slice To the End:')
# By leaving out the end index, the range will go to the end:
# Get the characters from the start to position 5 (not included):"
m = "Hello, Chandra!"
print(m[2:])
print('Negative Indexing:')
# Use negative indexes to start the slice from the end of the string:
# Get the characters:- From: "o" in "Chandra!" (position -5)
# To, but not included: "d" in "Chandra!" (position -2):
n = "Hello, Chandra!"
print(n[-8:-4])
