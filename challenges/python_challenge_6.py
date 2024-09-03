# Count the number of times each character occurs in the given `text` string

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
for letter in text.casefold():
    if letter.isalnum():
        word_count[letter.lower()] = word_count.setdefault(letter.lower(), 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)