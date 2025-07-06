#Functions - Reusable block of code (like a program)

def who_am_i(name,age):
    print(f"My name is {name} and I am {age} years old")

who_am_i("Heath",35)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

result1 = multiply(7,7)
result2 = multiply(8,8)
print(result1 + result2)

def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #new line
    print('\n')

nl()

x = 5
y = 10


# Relational operators
print(x == y)   # Output: False
print(x < y)    # Output: True


# Boolean expressions
print(x < y and y > 0)    # Output: True
print(x < y or y < 0)     # Output: True
print(not (x == y))       # Output: True
