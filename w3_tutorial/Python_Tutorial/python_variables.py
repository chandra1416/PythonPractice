# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = 10
print(x)
print(y)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
a = 50  # a is type of int
print(a)
a = 'chandra'  # a is type of str
print(a)
# Casting : If you want to specify the data type of a variable, this can be done with casting.
print("<------------Casting---------->")
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)
print("<------------Type of variable---------->")
x = 5
y = "john"
print(type(x))
print(type(y))

print("<------------Variable names are case-sensitive.---------->")
a = 4
A = 'SALLY'
print(a)
print(A)
# Variable Names
myvar = 'chandra'
my_var = 'chandra'
_my_var = 'chandra'
myVar = 'chandra'
MYVAR = 'chandra'
myvar2 = 'chandra'

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Illegal variable names:
# 2myvar = 'chandra'
# my-var = 'chandra'
# my var = 'chandra'
print("<------------Multi Words Variable Names---------->")
# Camel Case : Each word, except the first, starts with a capital letter
myVariableName = 'chandra'
print(type(myVariableName))
# Pascal Case : Each word starts with a capital letter
MyVariableName = 'andhra'
print(type(MyVariableName))
# Snake Case : Each word is separated by an underscore character
my_variable_name = 'Indra'
print(type(my_variable_name))
print("<------------Python variables assign multiple values---------->")
p, q, r = 'Orange', 'Banana', 'Cherry'
print(p)
print(q)
print(r)

# number of variables matches to number of values , else will get an error
a, b = 2, 5
print(a, b)

print("<------------one value to multiple variables---------->")
c = d = e = f = 10
print(c)
print(d)
print(e)
print(f)

print("<------------Unpack a Collection---------->")
fruits = ['Grape', 'Mango', 'papaya']
s, t, u = fruits
print(s)
print(t)
print(u)

print("<------------Python - Output Variables---------->")
# The Python print() function is often used to output variables.
j = 'Chandra is program developer'
print(j)
# In the print() function, you output multiple variables, separated by a comma:
o = 'Chandra'
p = 'is'
q = 'an'
r = 'Analyst'
print(o, p, q, r)
# You can also use the + operator to output multiple variables:
f = 'Chandra '
g = 'is '
h = 'an '
i = 'Expert'
print(f + g + h + i)

# For numbers, the + character works as a mathematical operator:
j = 10
k = 40
print(j + k)

# In the print() function, when you try to combine a string and a number with the + operator,
# Python will give you an error:
_a = 'chandra'
_b = 1416
print('Error details >> TypeError: can only concatenate str (not "int") to str')
# print(_a + _b)

# The best way to output multiple variables in the print() function is to separate them with commas,
# which even support different data types:
_c = 'w'
_d = 3
_e = 'schools'
print('support different type variables by separating with comma ,')
print(_c, _d, _e)
print("<------------ Python - Global Variables---------->")
print('Variables that are created outside of a function (as in all of the examples above) are known as global '
      'variables.')
print('Global variables can be used by everyone, both inside of functions and outside.')
# Global variables can be used by everyone, both inside of functions and outside.
_f = 'global'


def myfunc():
    print('It is a ' + _f + ' variable')


myfunc()
print('If you create a variable with the same name inside a function, this variable will be local,'
      ' and can only be used inside the function.')
print('If you create a variable with the same name inside a function, this variable will be local, and can only be '
      'used inside the function.')
v = "awesome"


def myfunc():
    v = "fantastic"
    print("Python is " + v)


myfunc()
print("Python is " + v)
print("<------------ The global Keyword---------->")
print('Normally, when you create a variable inside a function, that variable is local, and can only be used inside '
      'that function.')
print('To create a global variable inside a function, you can use the global keyword.')


# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
    global _i
    _i = "fantastic"


myfunc()
print("Python is " + _i)

