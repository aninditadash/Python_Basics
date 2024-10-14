# Unicode

# In Python 2, we had to explicitly specify that a string is encoded using one of the encodings specified in the
# Unicode standard. In Python 3, all strings are unicode.
# In open(), encoding is platform dependent, so you will get different behaviour on different computers.
# So, when opening a text file, explicitly specify the encoding, applies to both reading and writing operations.
# UTF-8 => Unicode Transformation Format 8-bit (uses 1 to 4 bytes)

# Code point refer to the individual codes that are defined to represent characters. ASCII can represent 127 characters.
# A = 65, first 32 code points are control codes, 9 for tab, 10 for a line feed and 13 for carriage return.

with open('../files/Jabberwocky_utf16.txt', encoding='utf-16') as jabber:
    for line in jabber:
        print(line.rstrip())