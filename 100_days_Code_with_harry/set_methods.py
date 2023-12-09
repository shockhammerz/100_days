my_wallet = {"No money", "only money", 0}
places = {"berlin", "Newyork", "lonavala"}
# Once a set is created, you cannot change its items, but you can add new items.

# Add Set Items:
# Once a set is created, you cannot change its items, but you can add new items.
my_wallet.add("money")
print(my_wallet)
# Add Sets:
# To add items from another set into the current set, use the update() method.
my_wallet.update(places)
print(my_wallet)

#Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"} #set
mylist = ["kiwi", "orange"] #list
thisset.update(mylist)
print(thisset)

# Python - Remove Set Items:
# To remove an item in a set, use the remove(), or the discard() method.
my_wallet.remove(0) #remving number zero
print(my_wallet)
places.discard("lonavala")
print(places)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

#You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
places.pop()
print(places)
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
places.clear()
print(places)

# The del keyword will delete the set completely:
# del my_wallet
# print(my_wallet) #will through error: NameError: name 'my_wallet' is not defined as the sets gets deleted 

#Access Set items:You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# Python - Join Sets
# Join two sets: You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
print(set1.union(set2)) #union
# set3 = set1.union(set2)
# print(set3)
set1.update(set2) #update
print(set1)
# Note: Both union() and update() will exclude any duplicate items

# Keep ONLY the Duplicates: The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) #a new set will be created which we need to store in a variable.
print(z)

# Keep All, But NOT the Duplicates: The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# a new set will be created which we need to store in a variable.
z = x.symmetric_difference(y)
print(z)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates: True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

#To get the length of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


# Set Methods: Python has a set of built-in methods that you can use on sets.

# Method	              Description:
# add()             Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others