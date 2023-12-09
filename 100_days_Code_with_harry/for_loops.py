# Python For Loops:
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

#Learning
fruits = "Banana", "Mango", "Sitafal"
print(type(fruits)) #tuple

#Example: Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# The for loop does not require an indexing variable to set beforehand.
# In Python, you can use the for loop without explicitly defining an indexing variable. 
# The loop will iterate over the elements of an iterable directly. Here's an example:
fruits = ["apple", "banana", "cherry"]

# Using for loop without an indexing variable
for fruit in fruits:
    print(fruit)

#Looping through STRING
my_string = "Hello, World!"

# Loop through each character in the string
for char in my_string:
    print(char)
# or 
for x in "banana":
  print(x)

#Break Statement: The break statement in Python is used to exit a loop prematurely, before its normal completion. 
# When the break statement is encountered inside a loop, the loop is terminated immediately, and 
# the program control moves to the next statement after the loop.

# Here's a simple example using a for loop to iterate over a list and using the break statement:
fruits = ["apple", "banana", "cherry", "date", "fig"]

# Loop through the list and break when the element is "cherry"
for fruit in fruits:
    print(fruit)
    if fruit == "cherry":
        print("Found cherry, breaking the loop")
        break

fruits = ["apple", "banana", "cherry", "date", "fig"]

# Loop through the list and break before the print when the element is "banana"
for fruit in fruits:
    if fruit == "banana":
        print("Found banana, breaking the loop before the print")
        break
    print(fruit)

#The continue statement in Python is used to skip the rest of the code inside a loop for the current iteration and jump to the next iteration. 
# It allows you to bypass the remaining code inside the loop block and move to the next iteration without terminating the entire loop.
# Here's an example using a for loop and the continue statement to skip printing a message when the fruit is "banana":

fruits = ["Mosambi", "Nariyal", "Avla", "Kela", "Santra"] #Mera example

for fruits in fruits:
    if fruits == "Kela":
        print("kele ko skip krke aage bhado")
        continue
    print("kele ko skip krke aage badh gaya")

fruits = ["apple", "banana", "cherry", "date", "fig"]

# Loop through the list and continue to the next iteration when the element is "banana"
for fruit in fruits:
    if fruit == "banana":
        print("Skipping banana, continuing to the next iteration")
        continue
    print(fruit)

#Tha Range Function:
# The range() function in Python is used to generate a sequence of numbers. 
# It is commonly used in for loops to iterate over a sequence of numbers. The basic syntax of the range() function is:

# range(stop)
# range(start, stop)
# range(start, stop, step)

# Print numbers from 0 to 4
for i in range(5):  # range(stop)
    print(i)

for i in range(10, 100):  # range(start, stop)
    print(i)

# range(start, stop, step) specifying the increment value by adding a third parameter:
for i in range(10, 100, 10):
    print(f"This is my output {i}")

# Else in For Loop
fruits = ["apple", "banana", "cherry", "date", "fig"]
# Loop through the list of fruits
for fruit in fruits:
    if fruit == "fig":
        print("Found fig, breaking the loop")
        break
    print(fruit)
else:
    print("Loop completed successfully, no more fruits to iterate")

# In this example, if the loop is not terminated by the break statement (i.e., if it completes iterating over all the fruits), the else block is executed, 
# printing the message "Loop completed successfully, no more fruits to iterate."
# If the loop is terminated by the break statement (for example, when the fruit is "banana"), the else block will be skipped.

for x in range(6):
  print(x)
else:
  print("Finally finished!")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.


#Nested Loops in Python:

# Nested loops in Python refer to placing one loop inside another. 
# This allows you to iterate over multiple sequences or perform more complex iterations. Here's an example of nested loops:
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop index: {i}, Inner loop index: {j}")

# In this example, the outer loop runs three times (for i values 0, 1, and 2), and for each iteration of the outer loop, the inner loop runs twice 
# (for j values 0 and 1). This results in a total of six iterations, and the print statement inside the inner loop is executed accordingly.

# Nested loops are often used when dealing with 2D data structures like matrices or grids. Here's a simple example:
matrix = [2, 3, 4], [6, 9, 3], {8, 9, 10} #self example
print(type(matrix[1]))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Nested loops to iterate over each element in the matrix
for row in matrix:
    # print(row) #prints eacg row [1, 2, 3] [4, 5, 6] [7, 8, 9]
    for element in row:
        print(element)
# In this example, the outer loop iterates over each row in the matrix, 
# and the inner loop iterates over each element in the current row.

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement:In Python, the pass statement is a null operation or a no-op statement. 
# It serves as a placeholder where syntactically some code is required but where no action is desired or necessary. 
# The pass statement does nothing and allows the program to proceed without raising any errors.
# Here's a simple example using pass:
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)

# In this example, when i is equal to 3, the pass statement is executed, essentially doing nothing. For all other values of i, it prints the value.
# The pass statement is commonly used in situations where code is required syntactically but where no action is needed, 
# for example, in empty functions or loops that are intended to be filled in later.

for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error without the pass statement
