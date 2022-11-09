print('<---------Specify a Variable Type-------------->')
# Casting in python is therefore done using constructor functions:
print('This can be done with casting. Python is an object-orientated language, and as such it uses classes to define '
      'data types, including its primitive types.')
print('1. int()')
print('2. float()')
print('3. str()')
print('<---------int()-------------->')
# 1. int() - constructs an integer number from an integer literal, a float literal (by removing all decimals),
# or a string literal (providing the string represents a whole number
a = int(2)
b = int(34.6)
c = int('67')
print(a)
print(b)
print(c)
print('<---------float()-------------->')
# 2. float() - constructs a float number from an integer literal, a float literal
# or a string literal (providing the string represents a float or an integer)
i = float(2)
j = float(34.6)
k = float('8')
_l = float('67.9')
print(i)
print(j)
print(k)
print(_l)
print('<---------str()-------------->')
# 3. str() - constructs a string from a wide variety of data types, including strings,
# integer literals and float literals
x = str(2)
y = str(34.6)
z = str('67')
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))
