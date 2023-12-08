# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

# my_bag = {"Wallet", "tiffin", 10, 10.5,}
# print(type(my_bag))
# print(my_bag)

# for value in my_bag:
#     print(type(value))
#     print(value)


#How to create an empty set in Python
empty_set = set()
print(type(empty_set))

#empty set can take upto one value
empty_set = set("tiffin")
print(type(empty_set))
for value in empty_set:
    print(value)

#set doesn't take repeated values