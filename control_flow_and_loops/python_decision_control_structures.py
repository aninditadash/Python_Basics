# Arithmetic operators  => +, -, *, /, %..
# Assignment operators  => =, +=, -=, /=, //=..
# Comparison operators  => <, <=, >, >=, ==, !=
# Logical Operators     => and, or and not ( used to reverse a Boolean value (not True => False, not False => True) )
# Membership operators  => in and not in ( test if a sequence is presented in an object )
# Identity operators    => is and is not ( compare variables to see whether they are the same object at the same
# memory address )

# Falsy values in Python => 0, '', [], {}, None

print("Getting input from the user")
name = input("Please enter your name: ")
age = int(input("How old are you {0}?: ".format(name)))     # Prompt, asking input from user
print(f"{name} is {age} years old.")

print("================================================================================")

# if, else and elif statements
if age < 10:
    print("Age is less than 10")
elif age == 10:
    print("Correct age")
else:
    print("Age is more than 10")

# if age >= 16 and age <= 65:
# Simplify chained comparison
if 16 <= age <= 65:
    print("Correct age")
else:
    print("Incorrect age")

if age < 16 or age > 65:
    print("Incorrect age")
else:
    print("Correct age")

# Simplify Chained comparisons
# When comparing conditions using and, Python will stop checking when it finds a False condition
# When comparing conditions using or, Python will stop checking when it finds a True condition

print("================================================================================")

print("Testing Membership operators")
fruits = ["apple", "banana"]
print("banana" in fruits)
print("pineapple" not in fruits)

print("================================================================================")

# String methods
print("String methods")
print(fruits[0].capitalize())
print(fruits[0].casefold())
print(fruits[0].lower())
print(fruits[0].upper())
print(fruits[0][0].isupper())

print("================================================================================")

print("Testing Identity operators")
a = ['a', 'b', 'c']
b = ['a', 'b', 'c']
c = b
print(f"a is b = {a is b}")
print(f"a is not b = {a is not b}")
print(f"b is c = {b is c}")
