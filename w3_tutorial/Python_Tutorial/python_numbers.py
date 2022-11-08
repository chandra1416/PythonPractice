# There are three numeric types in python
print("(1). int")
print("(2). float")
print("(3). complex")

print("<--------int type--------->")
x = 56
print(x)
print(type(x))
x = -390
print(x)
print(type(x))
x = 489558958484848429898885122876913498722
print(x)
print(type(x))

print("<--------float type--------->")
y = 23.0
print(y)
print(type(y))
y = -98.048
print(y)
print(type(y))
y = 3.09
print(y)
print(type(y))
print('float can also be scientific numbers with an "e" to indicate the power of 10.')
y = 102e4
print(y)
print(type(y))
y = 7E3
print(y)
print(type(y))
y = -87.7e100
print(y)
print(type(y))
print("<--------complex type--------->")
z = 5j
print(z)
print(type(z))
z = 4+5j
print(z)
print(type(z))
z = -5j
print(z)
print(type(z))
# Type conversion
print("<--------Type conversion--------->")
a = 9
b = -84.2
c = 5+4j
# convert from int to float:
print(a, 'is', type(a))
x = float(a)
print(x)
print(type(x))
# convert from float to int:
print(b, 'is', type(b))
x = int(b)
print(x)
print(type(x))
# convert from int to complex:
x = complex(a)
print(x)
print(type(x))
# Note: You cannot convert complex numbers into another number type.
print('Random Numbers')
import random
print(random.randrange(1, 89))
print('Python does not have a random() function to make a random number, '
      'but Python has a built-in module called random that can be used to make random numbers:')
