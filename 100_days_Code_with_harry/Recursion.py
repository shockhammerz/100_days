# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. 
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# for i in range(0,11):
#     print(factorial(i+1))

def random_series(n):
    if(n>0 and n<10):
        result = n + random_series(n)
        print(result)
    
    else:
        result = 0
    return result

def random_series(n):
    if(n>0 and n<10):
        result = n + random_series(n+2)
        print(result)

    else:
        result = 0
    return result

print(random_series(1))