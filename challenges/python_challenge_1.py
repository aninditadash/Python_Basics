choice = None
while choice != 0:
    if choice in range(1,6):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:\n"
              "1.\tLearn Python\n"
              "2.\tLearn Java\n"
              "3.\tGo swimming\n"
              "4.\tHave dinner\n"
              "5.\tGo to bed\n"
              "0.\tExit\n")
    choice = int(input())
