import random

# Types of Loops
# Count controlled loop => A method of repeating a loop a predefined number of times
# Condition controlled loop => A loop will be repeated until a given condition changes True to False or False to True
# depending on the type of loop
# Collection controlled loop => This is a special construct that allows looping through the elements of a "collection"
# which can be an array, list or other ordered sequences.

# For loop in Python is an example of Collection controlled loop.
# Loop control statements change the flow of execution in loops => break and continue
# Loop Else statement => Python allows else statement for while/for loops. This else Statement is executed after all
# iterations are completed. However, it's not executed if break statement is encountered.
# Range function => used with loops to iterate over sequence of numbers. It generates an iterator of arithmetic
# progressions.

# For loop
number_string = "9,223;372:036 854,775;807"
separators = ""
for char in number_string:
    if not char.isnumeric():
        separators += char
print(separators)
values = "".join(char if char not in separators else " " for char in number_string).split()
print(values)
print([int(val) for val in values])

print("================================================================================")

# For loop using range()
print("For loop using range(1, 20)")
for i in range(1, 20):
    print("i = {}".format(i))
print("For loop using range(10)")
for i in range(10):
    print("i = {}".format(i))
print("For loop using range(0, 10, 2)")
for i in range(0, 10, 2):
    print("i = {}".format(i))
print("For loop using range(10, 0, -2)")
for i in range(10, 0, -2):
    print("i = {}".format(i))

print("================================================================================")

# Using continue in for loop
# continue causes remaining code to be skipped and execution will jump back to for statement
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("For loop using and condition")
for day in days:
    if day != "Saturday" and day != "Sunday":
        print("Office day {}".format(day))
print("For loop using continue")
for day in days:
    if day == "Saturday" or day == "Sunday":
        continue
    print("Office day {}".format(day))

print("================================================================================")

# Using break in for loop
# break statement terminates the for loop when it is encountered
print("For loop using break")
for day in days:
    if day == "Saturday" or day == "Sunday":
        break
    print("Office day {}".format(day))

print("================================================================================")

days_list = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
find_day = "Sat"
day_found_at = None

# Finding item in the list using for loop and break
print("Finding item in the list using for loop and break")
for index in range(len(days_list)):
    if days_list[index] == find_day:
        day_found_at = index
        break

# Finding item in the list using built in method - NOT EFFICIENT
print("Finding item in the list using built-in method .index()")
if find_day in days:
    day_found_at = days_list.index(find_day)

if day_found_at is not None:
    print("Search successful {} at index {}".format(find_day, day_found_at))
else:
    print("{} not found in list".format(find_day))

print("================================================================================")

print("Find numbers from 1 upto 20 which are neither divisible by 3 or 5")
for i in range(0, 21):
    if i == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print("================================================================================")

print("Random number - {}".format(random.randint(1, 10)))

# Guessing game using while loop
print("Guessing game using while loop with True condition")
highest = 10
answer = random.randint(1, highest)
guess = 0
print("Please enter a number between 1 and {}: ".format(highest))
while True:
    guess = int(input())
    if guess == 0:
        print("You quit the game!!")
        break
    elif guess > answer:
        print("Guess lower")
    elif guess < answer:
        print("Guess higher")
    else:
        print("You guess correctly the number {}".format(guess))
        break

print("================================================================================")

# Guessing game using while loop
print("Guessing game using while loop and else condition")
highest_num = 25
answer_new = random.randint(10, highest_num)
guess_num = 0
print("Please enter a number between 10 and {}: ".format(highest_num))
while guess_num != answer_new:
    guess_num = int(input("Number: "))
    if guess_num > 0:
        if guess_num > answer_new:
            print("Guess lower")
        elif guess_num < answer_new:
            print("Guess higher")
    else:
        print("Sorry you lost!!")
else:
    print("You guess correctly the number {}".format(guess_num))

print("================================================================================")

print("For loop else statement")
numbers = [1, 45, 31, 12, 60]
# No numbers are divisible so for loop ends normally and else block is run
for num in numbers:
    if num % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("The numbers are fine")
