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
