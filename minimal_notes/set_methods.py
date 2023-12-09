# Define sets
my_wallet = {"No money", "only money", 0}
places = {"berlin", "Newyork", "lonavala"}

# Add items to the set
my_wallet.add("money")
print(my_wallet)

# Update set with items from another set
my_wallet.update(places)
print(my_wallet)

# Update set with items from a list
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove items from the set
my_wallet.remove(0)
print(my_wallet)
places.discard("lonavala")
print(places)

# Pop removes a random item
places.pop()
print(places)

# Clear and delete sets
places.clear()
print(places)

# Access set items using a loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# Join sets using union() and update()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1.union(set2))
set1.update(set2)
print(set1)

# Keep only duplicates and find symmetric difference
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

z = x.intersection(y)
print(z)

x.symmetric_difference_update(y)
print(x)

z = x.symmetric_difference(y)
print(z)

# Values True and 1 are considered the same in sets
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)

# Get the length of the set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Methods
# add(), clear(), copy(), difference(), difference_update(), discard(),
# intersection(), intersection_update(), isdisjoint(), issubset(),
# issuperset(), pop(), remove(), symmetric_difference(),
# symmetric_difference_update(), union(), update()
