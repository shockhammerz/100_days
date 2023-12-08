my_wallet = {"No money", "only money", 0}
places = {"berlin", "Newyork", "lonavala"}

# Python - Add Set Items
my_wallet.add("money")
print(my_wallet)
my_wallet.update(places)
print(my_wallet)


# Python - Remove Set Items
my_wallet.remove(0)
print(my_wallet)
places.discard("lonavala")
print(places)

places.pop()
print(places)

places.clear()
print(places)

# del my_wallet
# print(my_wallet)

#loop set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# Python - Join Sets
#Join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

# Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print(z)


# True and 1 is considered the same value:

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z)