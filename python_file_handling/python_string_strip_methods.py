def removeprefix(string: str, prefix: str) -> str:
    """
    Legacy method to remove the prefix from the passed string (before Python 3.9)
    :param string: text whose prefix is to removed
    :param prefix: prefix text
    :return: updated string
    """
    if string.startswith(prefix):
        return string[len(prefix):]
    return string[:]

def removesuffix(string: str, suffix: str) -> str:
    """
    Legacy method to remove the suffix from the passed string (before Python 3.9)
    :param string: text whose suffix is to removed
    :param suffix: suffix text
    :return: updated string
    """
    # Without suffix condition, is suffix is "", then we are returning string[:-0]
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    return string[:]

# strip() method is mainly used in processing text files
filename = '../files/Jabberwocky.txt'
with open(filename) as jabber:
    first_line = jabber.readline().rstrip()

print(f"first_line    = {first_line}")      # 'Twas brillig, and the slithy toves

# Remove characters from above line using Python strip() method
chars_to_remove = "'"
modified_line = first_line.strip(chars_to_remove)
print(f"modified_line = {modified_line}")   # Twas brillig, and the slithy toves

chars_to_remove = "'Twas"
modified_line = first_line.strip(chars_to_remove)
print(f"modified_line = {modified_line}")   # brillig, and the slithy tove

chars_to_remove = "'Twasebv"
modified_line = first_line.strip(chars_to_remove)
print(f"modified_line = {modified_line}")   # brillig, and the slithy tove

chars_to_remove = "'Twasebv "
modified_line = first_line.strip(chars_to_remove)
print(f"modified_line = {modified_line}")   # rillig, and the slithy to

# strip() methods don't remove the string that is passed as argument, they take each of the characters in the string
# and keep removing them until a non-matching character is found. So, strip() method will remove the characters from
# both the sides of the string.

print("================================================================================")

print("Using for loop to demonstrate the strip() by processing the start and end of the string")
chars_to_remove = "'Twasebv "

print("Processing the start of the string")
for character in first_line:
    if character in chars_to_remove:
        print(f'Removing "{character}"')
    else:
        break

print("\nProcessing the end of the string")
for character in first_line[::-1]:
    if character in chars_to_remove:
        print(f'Removing "{character}"')
    else:
        break

print("================================================================================")

# Python 3.9 added removeprefix() and removesuffix() methods
print("Using removeprefix() and removesuffix() built-in methods (from Python 3.9)")
twas_removed = first_line.removeprefix("'Twas")
print(f"twas_removed = {twas_removed}")

toves_removed = first_line.removesuffix("toves")
print(f"toves_removed = {toves_removed}")

# Before 3.9, following methods were used to perform the same operation
print("removeprefix and removesuffix legacy methods before Python 3.9")
twas_removed_legacy = removeprefix(first_line, "'Twas")
print(f"twas_removed = {twas_removed_legacy}")

toves_removed_legacy = removesuffix(first_line, "toves")
print(f"toves_removed = {toves_removed_legacy}")
