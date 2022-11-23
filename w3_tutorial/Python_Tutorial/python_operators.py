print("Operators are used to perform operations on variables and values.")
# Python divides the operators in the following groups:
# 1.Arithmetic operators
# 2.Assignment operators
# 3.Comparison operators
# 4.Logical operators
# 5.Identity operators
# 6.Membership operators
# 7.Bitwise operators
print("#######################################")
print("<--------Arithmetic operators--------->")
print("#######################################")
x = 5
y = 3
print("first value is 5 and second value is 3")
print("1.Addition:", x + y)
print("2.Subtraction:", x - y)
print("3.Multiplication:", x * y)
print("4.Division:", x / y)
print("5.Modules:", x % y)
print("6.Exponentiation:", x ** y)
print("7.Floor division:", x // y)

print("#######################################")
print("<--------Assignment operators--------->")
print("#######################################")
print("a = 5")
print('operator : =, example a = 5, same as : a = 5')
a = 5
print(a)
#print("a = 5")
print('operator : +=, example a += 3, same as : a = a + 3')
a += 3
print('>> Results : ', a)
a = 5
print('operator : -=, example a -= 3, same as : a = a - 3')
a -= 3
print('>> Results : ', a)
a = 5
print('operator : *=, example a *= 3, same as : a = a * 3')
a *= 3
print('>> Results : ', a)
a = 5
print('operator : /=, example a /= 3, same as : a = a / 3')
a /= 3
print('>> Results : ', a)
a = 5
print('operator : %=, example a %= 3, same as : a = a % 3')
a %= 3
print('>> Results : ', a)
a = 5
print('operator : **=, example a **= 3, same as : a = a ** 3')
a **= 3
print('>> Results : ', a)
a = 5
print('operator : //=, example a //= 3, same as : a = a // 3')
a //= 3
print('>> Results : ', a)
a = 5
print('operator : &=, example a &= 3, same as : a = a & 3')
a &= 3
print('>> Results : ', a)
a = 5
print('operator : |=, example a |= 3, same as : a = a | 3')
a |= 3
print('>> Results : ', a)
a = 5
print('operator : ^=, example a ^= 3, same as : a = a ^ 3')
a ^= 3
print('>> Results : ', a)
a = 5
print('operator : <<=, example a <<= 3, same as : a = a << 3')
a <<= 3
print('>> Results : ', a)
a = 5
print('operator : >>=, example a >> 3, same as : a >> 3')
a >>= 3
print('>> Results : ', a)

print("#######################################")
print("<--------Comparison operators--------->")
print("#######################################")
m, n = 5, 3
print('m = 5 , n = 3')
print('1. Equal(m == n):', m == n)
print('2. Not Equal(m != n):', m != n)
print('3. Greater than(m > n):', m > n)
print('4. Less then:(m < n)', m < n)
print('5. Greater than or Equal to(m >= n):', m >= n)
print('6. Less then or Equal to(m <= n):', m <= n)

print("#######################################")
print("<---------Logical operators----------->")
print("#######################################")
x = 5
print('x = 5')
print('1. "and": Returns True if both statements are true')
print('x > 3 and x < 10 :', x > 3 and x < 10)
print('2. "or": Returns True if one of the statements is true')
print('x > 3 or x < 4 :', x > 3 or x < 4)
print('3. "not": Reverse the result, returns False if the result is true')
print('not(x > 3 and x < 10) :', not(x > 3 and x < 10))

print("#######################################")
print("<--------Identity operators----------->")
print("#######################################")
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same
# object, with the same memory location:
print('1. "is ": Returns True if both variables are the same object ')
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print('x : ', x)
print('y : ', y)
print('x is z :', x is z)
# returns True because z is the same object as x
print('x is y :', x is y)
# returns False because x is not the same object as y, even if they have the same content
print('x == y: ', x == y)
# to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y
print('2. "is not": Returns True if both variables are not the same object')
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print('x : ', x)
print('y : ', y)
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print("#######################################")
print("<--------Membership operators--------->")
print("#######################################")
print('1. "in ": Returns True if a sequence with the specified value is present in the object ')
x = ["apple", "banana"]
print('x :', x)
print('Example : "banana" in x :', "banana" in x)
# returns True because a sequence with the value "banana" is in the list
print('2. "not in ": Returns True if a sequence with the specified value is present in the object')
x = ["apple", "banana"]
print('x :', x)
print('Example : "pineapple" not in x :', "pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

print("#######################################")
print("<--------Bitwise operators------------>")
print("#######################################")
print('operator : &, name : AND , Description:Sets each bit to 1 if both bits are 1')
print('operator : |, name : OR ,Description:Sets each bit to 1 if one of two bits is 1')
print('operator : ^, name : XOR ,Description:Sets each bit to 1 if only one of two bits is 1')
print('operator : ~, name : NOT ,Description:Inverts all the bits')
print('operator : <<, name : Zero fill left shift,Description:Shift left by pushing zeros in from the right and let '
      'the leftmost bits fall off')
print('operator : >>, name : Signed right shift , Description:Shift right by pushing copies of the leftmost bit in '
      'from the left, and let the rightmost bits fall off')

