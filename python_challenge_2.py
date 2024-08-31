# Remove all entries of spam from the below nested lists

menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    if "spam" in meal:
        top_index = len(meal) - 1
        for index, item in enumerate(reversed(meal)):
            if item == "spam":
                del meal[top_index - index]
    print(", ".join(meal))


# Convert the below list of strings to list of ints
strings_list = ['9', '223', '372', '036', '854', '775', '807']
print(strings_list)

# Approach 1
# for index, item in enumerate(strings_list):
#     strings_list[index] = int(item)

# Approach 2
numbers_list = []
for item in strings_list:
    numbers_list.append(int(item))

print(numbers_list)

# Take input from the user
user_input = input("Please enter three numbers, separated by commas: ")
# Split the given input string into 3 parts
string_tokens = user_input.split(",")
# Convert the tokens into integers
int_tokens = []
for st in string_tokens:
    int_tokens.append(int(st))
# Calculate the result: a + b - c
a, b, c = int_tokens
result = a + b - c
# Output the result
print(result)


