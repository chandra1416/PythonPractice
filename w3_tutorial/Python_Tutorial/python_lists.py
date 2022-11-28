print("############################################")
print('<-------------Python Lists----------------->')
print("############################################")
print('Lists : Lists are used to store multiple items in a single variable')
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set,
# and Dictionary, all with different qualities and usage. Lists are created using square brackets:
# Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)
print('List items are ordered, changeable, and allow duplicate values.')
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
print('Ordered :When we say that lists are ordered, it means that the items have a defined order, and that order will '
      'not change.')
print('When we say that lists are ordered, it means that the items have a defined order, and that order will not '
      'change.')
# Note :Note: There are some list methods that will change the order, but in general: the order of the items will not
# change.
print('<<<----------------Python - List Methods---------------------->>>')
print('------------------->>> append()<<---------------------')
# -------->>> append()->Adds an element at the end of the list
# syntax : list.append(elmnt)
# parameter : elmnt	-> Required. An element of any type (string, number, object etc.)
a = ["apple", "banana", "cherry"]
print(a)
a.append('orange')
print(a)
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
print('------------------->>> clear()<<---------------------')
# -------->>> clear()->Removes all the elements from the list
# syntax : list.clear()
a.clear()
print(a)
print('------------------->>> copy()<<---------------------')
# -------->>> copy()->Returns a copy of the list
# syntax : list.copy()
fruits = ['apple', 'banana', 'mango']
fav_fruits = fruits.copy()
print(fav_fruits)
print('------------------->>> count()<<---------------------')
# -------->>> count()->Returns the number of elements with the specified value
# Return the number of times the value/element appears in the list:
# syntax : list.count(value)
# Parameter : value->Required. Any type (string, number, list, tuple, etc.).
# The value to search for.
fruits = ['apple', 'mango', 'banana', 'mango']
fav = ['mango', 'pineapple', 'mango']
fruits.append(fav)
print(fruits)
frts_cnt = fruits.count('mango')
print(frts_cnt)
print('------------------->>> extend()<<---------------------')
# -------->>> extend()->Add the elements of a list (or any iterable), to the end of the current list
# syntax : list.extend(iterable)
# Parameter : iterable ->Required. Any iterable (list, set, tuple, etc.)
fruits = ['mango', 'banana', 'cherry']
print(fruits)
# cars = ['Ford', 'BMW', 'Volvo']
# print(cars)
market = ['mango', 'apple', 'mango']
print(market)
fruits.append(market)
print(fruits)
print(fruits.count('mango'))
fruits.extend(market)
print(fruits)
print(fruits.count('mango'))
print('------------------->>> index()<<---------------------')
# -------->>> index()->Returns the index of the first element with the specified value
# syntax : list.index(elmnt)
# Parameter : elmnt ->RRequired. Any type (string, number, list, etc.). The element to search for
print(fruits)
ind = fruits.index('apple')
print(ind)
print('------------------->>> insert()<<---------------------')
# -------->>> insert()->Adds an element at the specified position
# syntax : list.insert(pos, elmnt)
# Parameter : pos ->Required. A number specifying in which position to insert the value
# Parameter : elmnt ->Required. An element of any type (string, number, object etc.)
print(fruits)
ind = fruits.insert(4, 'papaya')
print(fruits)
print('------------------->>> pop()<<---------------------')
# -------->>> pop()->This method removes the element at the specified position.
# syntax : list.pop(pos)
# Parameter : pos ->Optional. A number specifying the position of the element you want to remove,
# default value is -1, which returns the last item Parameter : elmnt ->Required. An element of any type (string,
# number, object etc.)
print(fruits)
ind = fruits.pop(4)
print(fruits)
print(ind)
print('------------------->>> remove()<<---------------------')
# -------->>> remove()->This method removes the first occurrence of the element with the specified value.
# syntax : list.remove(elmnt)
# Parameter : elmnt ->Required. Required. Any type (string, number, list etc.) The element you want to remove
print(fruits)
ind = fruits.remove('apple')
print(fruits)
print('------------------->>> reverse() & reversed()<<---------------------')
# -------->>> reverse()->This method reverses the sorting order of the elements.
# syntax : list.reverse()
print('original : ', fruits)
fruits.reverse()
print('reverse() : ', fruits)
fruits = reversed(fruits)
print('reversed() :')
for i in fruits:
    print(i)
print('------------------->>> sort() <<---------------------')
# -------->>> sort()->This method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# syntax : list.sort(reverse=True|False, key=myFunc)
# Parameter : reverse ->Optional. reverse=True will sort the list descending. Default is reverse=False
# Parameter : key ->Optional. A function to specify the sorting criteria(s)
# Sort the list descending:
# ascending order : reverse=False, descending order : reverse=True
fruits = ['mango', 'banana', 'cherry']
print('original : ', fruits)
fruits.sort(reverse=False)
print(fruits)
fruits.sort(reverse=True)
print(fruits)


# Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


# Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
    return e['year']


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

# Sort the list by the length of the values and reversed:

# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
