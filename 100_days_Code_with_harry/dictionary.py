# # Dictionary
# # Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Note: As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

my_dict = {10689040: "29,00,000", "vaibs": 2900000 }
print(my_dict)
print(my_dict.keys()) #give just key values
print(my_dict.values()) #give just values

# print(my_dict.clear())

z = my_dict.copy() #copies the dictionary
print(z)
#or
z = dict(my_dict)
print(f"z is euqal to {z}")
# print(my_dict.pop(10689040))
# print(my_dict.popitem()) #will print key-value pair which it popped, it pops  the last value
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# print(my_dict)

print(my_dict["vaibs"]) #use square bracket to access key value
print(my_dict.get("vaibs"))
print(my_dict.get(9000000))
print(my_dict.get(10689040)) #get only gets the values corresponding to the keys

# #Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
print(my_dict.items()) #item means key-value pair both

print(my_dict.setdefault("gondu", "pro")) #setting default vlaue, Note: it is comma seprated key and values
print(my_dict.get("gondu"))

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
print(my_dict.update({"gondu": "pro"})) #updating the dictionary Note: Defined a dictionary to update the existing dictionary
print(my_dict.items()) 
# Example: Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

#Example
# Make a change in the original dictionary, and see that the values list gets updated as well:?
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

#  Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
# Example :Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year1": 2020
}
print(thisdict)

# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
# Example: Print the number of items in the dictionary:
print(len(thisdict.values())) #changed year to year 1, so it's showing 4 or else it will print 3 as year and year is same

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
# Example: String, int, boolean, and list data types:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
for values in thisdict.values():
    print(type(values))

for keys in thisdict.values():
    print(type(keys))


#The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
# Example: Using the dict() method to make a dictionary:
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Example:  Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# The del keyword removes the item with the specified key name:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
del thisdict["model"]
print(thisdict)

# del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

# Loop Through a Dictionary:
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# ExampleGet your own Python ServerPrint all key names in the dictionary, one by one:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
  print(x)
  #or
for x in thisdict.keys():
  print(x)

# Example: Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
#or
for x in thisdict.values():
  print(x)

# Example: Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)


# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

# Or, if you want to add three dictionaries into a new dictionary:
# Example: Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

#Access Items in Nested Dictionaries: To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"])

# Dictionary Methods: Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

