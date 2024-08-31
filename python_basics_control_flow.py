# Arithmetic operators => +, -, *, /, %..
# Assignment operators => =, +=, -=, /=, //=..

name = input("Please enter your name: ")
age = int(input("How old are you {0}?: ".format(name)))     # Prompt, asking input from user
print("Your age is:", age)

# if, else and elif statements
if age < 10:
    print("Age is less than 10")
elif age == 10:
    print("Correct age")
else:
    print("Age is more than 10")

# Comparison operators =>  <, <=, >, >=, ==, !=
# Logical Operators => and, or and not (used to reverse a Boolean value (not True => False, not False => True))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:         # Simplify chained comparison
    print("Correct age")
else:
    print("Incorrect age")

print("=" * 80)

if age < 16 or age > 65:
    print("Incorrect age")
else:
    print("Correct age")

# Simplify Chained comparisons
# When comparing conditions using and, Python will stop checking when it finds a False condition
# When comparing conditions using or, Python will stop checking when it finds a True condition

# Falsy values in Python - 0, '', []

# Membership operators (test if a sequence is presented in an object) => in and not in

fruits = ["apple", "banana"]
print("banana" in fruits)
print("pineapple" not in fruits)

# String methods
print(fruits[0].capitalize())
print(fruits[0].casefold())
print(fruits[0].lower())
print(fruits[0].upper())
print(fruits[0][0].isupper())