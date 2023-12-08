# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. 
# It is used to provide documentation about the code. In Python, triple double-quoted strings are commonly used for docstrings. 
# Here's an example of a simple docstring for a Python function:

def maths_table():
    '''This table is used to get table for any number'''
    number = int(input('Enter table you want:'))
    print(type(number))

    for i in range(0,21):
        result = number * i
        print(f"{number} * {i} = {result}")
        
print(maths_table.__doc__) # Accessing the docstring using __doc__
maths_table()

# In Python, the __doc__ attribute is used to access the docstring associated with a module, function, class, or method. 
# It returns the docstring as a string or None if the object does not have a docstring. 

def maths_table():
    # '''This function is used to print the table for any number'''
    number = int(input('Enter table you want: '))

    for i in range(1, 11):
        result = number * i
        print(f'{number} * {i} = {result}')

print(maths_table.__doc__) ## Accessing the docstring using __doc__ (will return None as we haven't defined the doc string)
maths_table()


# The docstring is enclosed in triple double-quotes.
# It includes a brief description of what the function does.
# Parameters and their types are listed along with descriptions.
# The return type and what the function returns are documented.