# Sets are faster than lists when testing for membership, because sets use hash codes similar to keys in a dictionary.
# In case of a list, Python has to search the entire list to find the item.
# In case of set, Python uses hash code to find out where the item should be.

choice = "-"
valid_choices = {"1", "2", "3", "4", "5"}
while choice != "0":
    # if choice in list("12345"):
    # if choice in set("12345"):
    # if choice in {"1", "2", "3", "4", "5"}:
    if choice in valid_choices:
        print(f"You chose {choice}")
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

