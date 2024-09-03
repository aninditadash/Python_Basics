# Calculate factorial of a number
def factorial(num: int) -> int:
    """
    Calculate the factorial of the number `n`
    :param num: number whose factorial is to be calculated
    :return: the factorial
    """
    if num <= 1:
        return 1

    return num * factorial(num - 1)


for number in range(0, 36):
    print("{} {}".format(number, factorial(number)))
