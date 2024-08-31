print("Welcome to Python basics")

# Using escape characters like \n or """ quotes for adding " or ' in the strings
print('This a sentence with a \'single quote\' in between and \nhas a new line')
print('This a sentence with a \'single quote\' in between')
print("This a sentence with a \"double quote\" in between")
print('This a sentence with a \"double quote\" in between')

# This is a multi line print statement
print("""This a sentence with a double 
quote in between and it starts and ends with 
3 double quotes""")
# Here backslash removes the new line from the string, so below string prints in 1 line
print("""This a sentence with a double \
quote in between and it starts and ends with \
3 double quotes""")

# Escaping backslash character for strings containing backslash or using raw strings (r'<string>)
print(r'C:\Users\Desktop\Screenshots\figure.jpg')
print('C:\\Users\\Desktop\\Screenshots\\figure.jpg')

# Printing Data types of variables in Python using type(), Python is dynamically typed like JS, but it is strongly typed
name = 'Annu'
print(type(name))
age = 10
print('print(type(age)):: ', type(age))
age_in_words = '10 years'
age = '10'
print('print(type(age)):: ', type(age))
# Printing both string and int using concatenation gives error
# print(name + " is " + age + " years old.")
print(name, "is", age, "years old.")
print("================================================================================")
print("================================================================================")

# Python built-in datatypes - numeric (int, float), iterator, sequence, mapping, file, class, exception
a = 12
b = 3
print(a / b)
print(a // b)  # Integer Division
print(a % b)  # Modulo after Integer Division
# for i in range(1, a/b):    # => Gives error as it returns a floating point value
for i in range(1, a // b):
    print(i)
print("================================================================================")
print("================================================================================")

# str String Datatype
parrot = 'Norwegian Blue'
print(parrot)
print('parrot[3]:: ', parrot[3])
# Negative indexing in strings, index the string from the end
print('parrot[-1]:: ', parrot[-1])
print("================================================================================")

# Python sequence types lets us create a slice, e.g. string is a sequence type
# Strings slicing  - string[start:stop:step]
slice_num = 6
print(parrot[0:6])  # slice string from index 0 upto 5, not including index 6
print(parrot[3:5])  # slice string from index 3 upto 4, not including index 5
print(parrot[:9])  # slice string from index 0 upto 8, not including index 9, start defaults to beginning of sequence
print(parrot[10:])  # slice string from index 10 upto end of the sequence
print(parrot[:slice_num] + parrot[slice_num:])  # This is equal to original string
# Also creates a copy of original string
print(parrot[
      :])
# This is also equal to original string as no start value means beginning of sequence and no stop value means end of
# sequence

print("================================================================================")
# Strings slicing with negative start and stop numbers  - - string[(+/-)start:(+/-)stop:step]
print(parrot[-4:-2])  # slice string from backwards from -4 upto -3 not including -2 (Bl)
print(parrot[-4:12])
print(parrot[-14:-8])
print("================================================================================")
# Using step in Slicing
print(parrot[0:6:2])
# Practical example of using step in slicing
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)
values = "".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])
print("================================================================================")
# Strings slicing with negative step (Slicing backwards)  - string[(+/-)start:(+/-)stop:(+/-)step]
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:-1:-1]  # Returns no value as 25 and -1 refer to same character here
print(backwards)
backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1]  # Reversing a string
print(backwards)
print(letters[16:13:-1])  # qpo
print(letters[4::-1])  # edcba
print(letters[:-9:-1])  # slice the string to produce last 8 characters in reverse order
print("================================================================================")

# Python idioms
# Reversing a string
backwards = letters[::-1]
print('Reversing a string:: ', backwards)
# Return last n items in a sequence (from end of sequence), e.g. last 4 items from letters
print('Return last 4 items:: ', letters[-4:])
# Return last character through slice
print(letters[-1:])
# Return first character through slice
print(letters[:1])
print(letters[0])  # This will give same result as above statement, but it gives error when string is empty
print("================================================================================")

# Python 3 Sequence types - string, list, tuple, range, bytes and bytearray (sequence is an ordered list of items)
# e.g. list of strings, in which each item (string) is also a sequence
# Most string operations applicable to other sequence types, except for range which cant be concatenated or multiplied
# Operators for the sequence types
string1 = "Hello"
string2 = "World"
print(string1 + string2)  # Concatenation
print(string1 * 5)  # Multiplication, which prints string1 5 times
print(string1 * (5 + 4))
print(string1 * 5 + "4")
print("================================================================================")

# Check substring
today = "sunday"
print("sun" in today)  # True
print("day" in today)  # True
print("sat" in today)  # False
print("================================================================================")

# Strings cant be concatenated with number using +, it gives error
# stringInt = "Hello" + 2
# print(stringInt)      # Gives error when printing
# Approach 1
# We can coerce the numbers into a string using str function (every datatype can be coerced into string representation)
my_age = 25
print("Age is " + str(my_age) + " years")
# Approach 2
# Python 3 allows strings to be formatted using replacement fields and dot format method
print("Age is {0} years".format(my_age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# String formatting by specifying width {n:<width>}
# To align the values => left {n:<<width>}, right {n:><width>}, center {n:^<width>}
for i in range(1, 13):
    print("No. {0:2} squared {1:4} cubed {2:4}".format(i, i ** 2, i ** 3))
for i in range(1, 13):
    print("No. {0:>2} squared {1:<4} cubed {2:^4}".format(i, i ** 2, i ** 3))

# For decimal numbers - width and precision (no. of digits after decimal point)
print("Pi is approximately {0:50.50f}".format(22 / 7))
print("Pi is approximately {0:60.50f}".format(22 / 7))

# String formatting using f-strings in Python 3.6
my_name = "Anne"
my_age = 25
print(f"{my_name} is {my_age} years old")
print(f"Pi is approximately {22 / 7:60.50f}")

# String formatting using String interpolation (was used in Python 2, going to be deprecated)
print("My age is %d " % my_age)
print("My age is %d %s, %d %s" % (my_age, "years", 6, "months"))
print("Pi is approximately %f" % (22 / 7))
print("Pi is approximately %55.50f" % (22 / 7))


