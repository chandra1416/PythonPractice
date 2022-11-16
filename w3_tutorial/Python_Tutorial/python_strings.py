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
print('<----------------------------<<Python - Modify Strings>>--------------------------->')
print('Python has a set of built-in methods that you can use on strings.')
print('(1). Upper Case:The "upper()" method returns the string in upper case:')
o = "Hello, Chandra!"
print(o.upper())
print('(2). Lower Case:The "lower()" method returns the string in lower case:')
p = "Hello, Chandra!"
print(p.lower())
print('(3). Remove Whitespace:The strip() method removes any whitespace from the beginning or the end:')
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
q = " Hello, Chandra!"
print(q)
print(q.strip())
print('(4). Replace String:The replace() method replaces a string with another string:')
r = "Hello, Chandra!"
print(r.replace('Cha', 'A'))
print('(5). RSplit String:TThe split() method returns a list where the text between the specified separator becomes '
      'the list items.')
s = "Hello, Chandra!"
s_test = "Hello Python Developer!"
print(s.split(","))
print(s_test.split(" "))
print('<----------------------------<<(more)Python String Methods>>--------------------------->')
# Python has a set of built-in methods that you can use on strings.
print('Note: All string methods returns new values. They do not change the original string.')
print('(1). Python String capitalize() Method')
# Upper case the first letter in this sentence:
t = "hello Chandra, and welcome to my python world."
t_rslt = t.capitalize()
print(t_rslt)
# The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
# syntax : string.capitalize()
t_1 = "hello Chandra, and welcome to my PYTHON world."
t_1_rslt = t_1.capitalize()
print(t_1_rslt)
# See what happens if the first character is a number:
t_2 = '10th June is Chandra Birthday'
t_2_rslt = t_2.capitalize()
print(t_2_rslt)
print('(2). Python String casefold() Method')
u = ">>Hello Chandra, and Welcome to My PYTHON World."
u_rslt = u.casefold()
print(u_rslt)
# syntax : string.casefold()
print('(3). Python String center() Method')
# The center() method will center align the string, using a specified character
# (space is default) as the fill character.
v = "Chandra"
v_rslt = v.center(50)
print(v_rslt)
# syntax : string.center(length, character)
# length	Required. The length of the returned string
# character	Optional. The character to fill the missing space on each side. Default is " " (space)
v_1 = "Chandra"
v_1_rslt = v_1.center(50, "*")
print(v_1_rslt)
print('(4). Python String count() Method')
# Return the number of times the value "apple" appears in the string:
# syntax : string.count(value, start, end)
# value	Required. A String. The string to value to search for
# start	Optional. An Integer. The position to start the search. Default is 0
# end	Optional. An Integer. The position to end the search. Default is the end of the string
w = "I love India. India ais my birth place"
w_rslt = w.count("India")
print(w_rslt)
w_1 = "I love India. India ais my birth place"
w_1_rslt = w_1.count("India", 5, 18)
print(w_1_rslt)
print('(5). Python String encode() Method')
# syntax : string.encode(encoding=encoding, errors=errors)
# The encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
print('UTF-8 encode the string:')
x = "My name is Chandra"
x_rslt = x.encode()
print(x_rslt)
print('UTF-8 encode the string:')
y = "My name is Chåndra"
txt = "My name is Ståle"
print(y.encode(encoding="ascii", errors="backslashreplace"))
print(y.encode(encoding="ascii", errors="ignore"))
print(y.encode(encoding="ascii", errors="namereplace"))
print(y.encode(encoding="ascii", errors="replace"))
print(y.encode(encoding="ascii", errors="xmlcharrefreplace"))
print('(6). Python String () Method')
# Check if the string ends with a punctuation sign (.):
z = "My name is Chandra. "
z_rslt = z.endswith(". ")
print(z_rslt)
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# syntax : string.endswith(value, start, end)
# value	: Required. The value to check if the string ends with
# start : Optional. An Integer specifying at which position to start the search
# end	: Optional. An Integer specifying at which position to end the search
z_1 = "My name is Chandra. "
z_1_rslt = z_1.endswith("dra. ", 10, 20)
print(z_1_rslt)
print('(7). Python String expandtabs() Method')
# The expandtabs() method sets the tab size to the specified number of whitespaces.
# syntax : string.expandtabs(tabsize)
# tabsize	Optional. A number specifying the tabsize. Default tabsize is 8
_a = "H\te\tl\tl\to"
print(_a)
print(_a.expandtabs())
print(_a.expandtabs(2))
print(_a.expandtabs(4))
print(_a.expandtabs(10))

print('(8). Python String find() Method')
# The find() method finds the first occurrence of the specified value. The find() method returns -1 if the value is
# not found. The find() method is almost the same as the index() method, the only difference is that the index()
# method raises an exception if the value is not found. (See example below)
# syntax : string.find(value, start, end)
_b = "Indian Love poets are from Telugu and one  Love Poet is Chandra"
_b_rslt = _b.find("Love")
print(_b_rslt)
_b_1 = "Indian Love poets are from Telugu and one  Love Poet is Chandra"
_b_1_rslt = _b_1.find("Love", 30, 50)
print(_b_1_rslt)
print(_b_1.find("q"))
print('(9). PPython String format() Method')
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# Read more about the placeholders in the Placeholder section below.
# The format() method returns the formatted string.
# syntax : string.format(value1, value2...)
_c1 = "My name is {fname}, I'm {age}".format(fname="Chandra", age=25)
_c2 = "My name is {0}, I'm {1}".format("Chandra", 25)
_c3 = "My name is {}, I'm {}".format("Chandra", 25)
print(_c1)
print(_c2)
print(_c3)
print('(10). Python String index() Method')
# The index() method finds the first occurrence of the specified value. The index() method raises an exception if the
# value is not found. The index() method is almost the same as the find() method, the only difference is that the
# find() method returns -1 if the value is not found. (See example below)
# syntax : string.index(value, start, end)
# value	: Required. The value to search for
# start : 	Optional. Where to start the search. Default is 0
# end	: Optional. Where to end the search. Default is to the end of the string
# Where in the text is the first occurrence of the letter "e"?:
_d = "Hello, My name is Chandra."
_d_rslt = _d.index("d")
print(_d_rslt)
print('(11). Python String isalnum() Method')
# Check if all the characters in the text are alphanumeric:
# syntax : string.isalnum()
_e = "Chandra1416"
_e_rslt = _e.isalnum()
print(_e_rslt)
print('(12). Python String isalpha() Method')
# Check if all the characters in the text are letters:
_f = "Chandra1"
_f_rslt = _f.isalpha()
print(_f_rslt)
print('(13). Python String isascii() Method')
# Check if all the characters in the text are ascii characters:
_g = "Chandra1"
_g_rslt = _g.isascii()
print(_g_rslt)
print('We need to try more string methods , later on subject revise')

print('<----------------------------<<Python - String Concatenation >>--------------------------->')
# To concatenate, or combine, two strings you can use the + operator
_a_ = "chandra"
_b_ = "mukanagari"
_c_ = _a_  + _b_
_d_ = _a_ + "_" + _b_
print(_c_)
print(_d_)
print('<----------------------------<<Python - Format - Strings>>--------------------------->')
# As we learned in the Python Variables chapter, we cannot combine strings and numbers
age = 25
#bio = "My name is Chandra, I am " + age
#print(bio)
# we can combine strings and numbers by using the format() method
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {}
age = 25
bio = "My name is Chandra, I am {}"
print(bio.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
myorder_1 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print(myorder_1.format(quantity, itemno, price))
