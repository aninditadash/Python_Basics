# Function should return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if it's
# not divisible by either 3 or 5.
# number is divisible by 3, return "fizz", if divisible by 5, return "buzz"#
# If it's divisible by both 3 and 5, return "fizz buzz".

def fizz_buzz(n: int) -> str:
    """
    Return "fizz" if `n` divisible by 3, "buzz" divisible by 5, "fizz buzz" if divisible by 3 and 5.
    Return the `n` if not divisible by 3 or 5.
    :param n: number to test if divisible by 3 or 5
    """
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"

    return str(n)


# for num in range(1, 101):
#     print(fizz_buzz(num))

# Playing fizz buzz
input("Playing fizz buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Please enter your answer: ")
    if player_answer != correct_answer:
        print("You lose, correct answer was {}".format(correct_answer))
        break
else:
    print("Congrats, you have reached the number {}".format(next_number))
