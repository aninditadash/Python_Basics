# Key in a dictionary must be hashable. an object is hashable if it has hash value which never changes
# during its lifetime.
# Hashing function produces fixed-size hash values from its input. Hashes are usually integers but don't have to be.
# Hash function produces values that can be used to index a fixed-size datastructure e.g. hash table.
# Hash code doesn't have to be unique, 2 different strings can have same hash, it's called collision.
# If we can calculate the hash value
# then finding that entry in the hash table becomes fast, that's why dictionaries are faster.
# Accessing an item in dictionary will be slightly slower than indexing a list, because of time taken to calculate
# the hash, but it will not be dependent on no. of items in dictionary, whereas longer list means more indexing time.

# Closest datastructure to the computer's memory is a one-dimensional array, where memory addresses are similar to
# indexes into an array. Each memory address can access 1 memory location.

# ord(<string>) function is used to convert a single Unicode character into its integer representation
print(f'ord("a") = {ord("a")}')
print(f'ord("A") = {ord("A")}')
print(f'ord("b") = {ord("b")}')

print("================================================================================")

print("Python built-in hash function")
data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# Python3 built-in hash function
for key, value in data:
    h = hash(key)
    print(f"key = {key}, hash = {h}")

print("================================================================================")

def simple_hash_function(s: str) -> int:
    """
    A simple hash function to demonstrate hashing, not to be used for any development work
    :param s: string whose hash is to be created
    :return: the hash which is an integer
    """
    basic_hash = ord(s[0])
    return basic_hash % 10

def get(k: str) -> str:
    """
    Return the value for the key, or '' if key does not exist
    """
    hash_code = simple_hash_function(k)
    if values[hash_code]:
        return values[hash_code]
    return ''


keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash_function(key)       # h = hash(key)
    print(key, h)
    keys[h] = key
    values[h] = value

print(f"keys {keys} \nvalues {values}\n")
print(f"lemon - {get('lemon')}")
print(f"grape - {get('grape')}")
print(f"tomato - {get('tomato')}")
print(f"banana - {get('banana')}")

# hashlib module implements common interface to many different secure hash and message digest algorithms.
# message digest is another name for hash

