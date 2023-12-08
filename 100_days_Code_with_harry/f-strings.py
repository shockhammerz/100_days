#  F-strings, also known as formatted string literals, provide a concise and readable way to embed expressions inside string literals.

name = "vaibs"
country = "India"
# F-string to combine variables in a string
print(f'Hey my name is {name} and I am from {country}')

Height = 167.85960
print(f"This is my height in 2 decimals: {Height:.2f}")

print(f"The multiplication is {20*30}")

print(f"The f-string can also be written as: Hey my name is {{name}} and I am from {{country}}")