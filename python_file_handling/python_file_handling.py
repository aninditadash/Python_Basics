# The open() function is used to open internally stored files. It returns the contents of the file as Python objects.
# We have to explicitly close the file after completing the necessary operation as it can lead to resource leaks.

jabber = open('../files/Jabberwocky.txt', 'r')

for line in jabber:
    # Here, after each line, we get another new line (blank), because each line in .txt file has a '\n' as the
    # line break and print statement also adds a new line.
    # print(line, end="")
    print(line.strip())     # strip() method removes the newline character at the end of each line

jabber.close()

# strip() removes both leading and trailing spaces or characters, we can use lstrip() or rstrip() methods
# to remove leading or trailing spaces respectively.
# Whitespace is any character that represents horizontal or vertical spacing, these characters are not visible.
# e.g. space, tab, newline

# As disk drives are slow, compared to computer's memory, data is read in large chunks into an area of memory
# called a buffer, so data retrieval is faster. A disk buffer is also called a disk cache.
# When writing data to disk, data is put into buffer first. That allows the program to move on, without waiting
# for the actual transfer to complete. Write to disk can happen in the background, while the code continues with
# other things. It's another reason to close the file while writing, because if file is not closed and program is
# terminated, the cache data might not be written to the disk, resulting in data loss.
