# Binary Search algorithm => most efficient way of finding an item in an ordered list

# Guessing game using Binary Search algorithm (Hi Lo Game), also calculate no. of guesses.
low = 1
high = 1000
print("Please think of a number between {} and {}".format(low, high))
input("Please ENTER to start: ")
guesses = 1

while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     "Enter h or l, or c if my guess was correct: "
                     .format(guess))

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess higher. The high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses += 1
else:
    print("You thought of the number {} and guessed it in {} attempts".format(low, guesses))
