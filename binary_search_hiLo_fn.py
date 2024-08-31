# Binary Search Hi Lo Game using functions
def guess_binary(answer, low, high):
    num_guesses = 1
    while True:
        guess = low + (high - low) // 2

        if guess < answer:
            # Guess higher. The low end of the range becomes 1 greater than the guess
            low = guess + 1
        elif guess > answer:
            # Guess higher. The high end of the range becomes 1 less than the guess
            high = guess - 1
        elif guess == answer:
            return num_guesses

        num_guesses += 1


LOW = 1
HIGH = 1000
max_guesses = 0
correct_count = 0
for number in range(LOW, HIGH + 1):
    guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {} guesses".format(number, guesses))

    if guesses > max_guesses:
        max_guesses, correct_count = guesses, 1
    elif guesses == max_guesses:
        correct_count += 1

print("I guessed it {} times in maximum {} guesses".format(correct_count, max_guesses))