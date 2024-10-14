# Serialization is the process of translating a data structure or object state into a format that can be stored
# (e.g., in a file or memory data buffer) or transmitted (for e.g. over a computer network) and re-constructed later
# (possibly in a different computer environment).
import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

languages_tuple = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

# To serialize Python values to a file, we open a text file for writing and use json.dump() function. The dump()
# function serializes the data and then writes the result to the file.

with open('../files/test.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

with open('../files/test_tuple.json', 'w', encoding='utf-8') as testfile:
    # Here we get back a list of lists as same as before when we passed the languages list
    # JSON format does not support tuples.
    json.dump(languages_tuple, testfile)

with open('../files/test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)

print(data)
print(data[2])

# Use JSON when you want to store data, or transmit it, in a format that other systems can use. It is not suitable
# to store the program's data if you need to preserve the exact type. JSON only supports 7 data types and no support
# for things like dates. ISO 8601 is the international standard for storing dates.
# JSON format does not provide any indication for the type of data it contains.
# JSON is less verbose than some other serialisation formats like XML, but due to this, it lacks the ability to
# specify the data type.

