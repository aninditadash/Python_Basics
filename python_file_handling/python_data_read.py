# File handles (File descriptors on Mac and Linux) are used by the OS to keep track of the files that have been opened.
# These file handles are shared by every process in the computer.
# Another consequence of failing to close a file, when writing data to it, is that data might be lost.

with open('../files/Jabberwocky.txt', 'r') as jabber:
    print(type(jabber))
    for line in jabber:
        print(line.rstrip())

print("================================================================================")

# Using readlines() method
with open('../files/Jabberwocky.txt', 'r') as jabber:
    # readlines() method returns a list of strings for each line in the file
    lines = jabber.readlines()

print(lines)
print(lines[-1:])

print("================================================================================")

# Processing the lines in reverse order
for line in reversed(lines):
    print(line, end='')

print("================================================================================")

# Using read() method
with open('../files/Jabberwocky.txt') as jabber:
    # read() method returns the entire file content as a string
    text = jabber.read()

# print(text)
for character in reversed(text):
    print(character, end='')

print("\n================================================================================")

# Using readLine() method
with open('../files/Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print("================================================================================")

# The above operation can also be performed by iterating over the file object
with open('../files/Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break

print("================================================================================")

with open('../files/Jabberwocky.txt') as jabber:
    # readline() reads one line from a file at a time
    line = jabber.readline().rstrip()
    print(line)

