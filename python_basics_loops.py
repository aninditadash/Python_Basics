import random

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
print("================================================================================")

# For loop using range()
for i in range(1, 20):
    print("i = {}".format(i))
print("================================================================================")
for i in range(10):
    print("i = {}".format(i))
print("================================================================================")
for i in range(0, 10, 2):
    print("i = {}".format(i))
print("================================================================================")
for i in range(10, 0, -2):
    print("i = {}".format(i))

print("================================================================================")
print("================================================================================")

# Using continue in for loop
# continue causes remaining code to be skipped and execution will jump back to for statement
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    if day != "Saturday" and day != "Sunday":
        print("Office day {}".format(day))
print("================================================================================")

for day in days:
    if day == "Saturday" or day == "Sunday":
        continue
    print("Office day {}".format(day))

print("================================================================================")
print("================================================================================")

# Using break in for loop
# break statement terminates the for loop when it is encountered
find_day = "Saturday"
day_found_at = None

# Finding item in the list using for loop and break
for index in range(len(days)):
    if days[index] == find_day:
        day_found_at = index
        break

# Finding item in the list using built in method - NOT EFFICIENT
if find_day in days:
    day_found_at = days.index(find_day)

if day_found_at is not None:
    print("Search successful {} at index {}".format(find_day, day_found_at))
else:
    print("{} not found in list".format(find_day))

print("================================================================================")
print("================================================================================")

i = 0
while i < 10:
    print("Number - {}".format(i))
    i += 1

for i in range(0, 21):
    if i == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print("================================================================================")
print("================================================================================")

print("Random number - {}".format(random.randint(1, 10)))

# Guessing game using while loop
highest = 10
answer = random.randint(1, highest)
guess = 0
print("Please enter a number between 1 and {}: ".format(highest))
while True:
    guess = int(input())
    if guess == 0:
        break
    elif guess > answer:
        print("Guess lower")
    elif guess < answer:
        print("Guess higher")
    else:
        print("You guess correctly the number {}".format(guess))
        break

print("================================================================================")
print("================================================================================")

# else in a for loop
# if for loop does not execute normally and if statement runs with break, else block is not run
numbers = [1, 45, 31, 12, 60]   # No numbers are divisible so for loop ends normally and else block is run

for num in numbers:
    if num % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("The numbers are fine")
