# Module is a file containing Python definitions and statements
def is_palindrome(string: str) -> bool:
    backwards = string[::-1]
    return backwards.casefold() == string.casefold()


print(is_palindrome("hello"))
print(is_palindrome("pep"))


def is_sentence_palindrome(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


print(is_sentence_palindrome("Was it a car ,or a cat, I saw?"))
print(is_sentence_palindrome("Do geese see god?"))
print(is_sentence_palindrome("Hello World!!"))
print(is_sentence_palindrome("Python"))
print(is_sentence_palindrome("Radar"))


# Find sum of even or odd numbers in a range using loop
def sum_eo_loop(n: int, t: str) -> int:
    """
    Find sum of even or odd numbers upto but not including n based on the param t

    If t is "e", it will find the sum of all even numbers upto n, else if t is "o" it
    will find sum of all odd numbers upto n. Will send -1 otherwise.
    :param n: number
    :param t: "e"|"o" for even/odd numbers
    :return: integer that is the sum of even or odd numbers upto n
    """
    num_sum = 0
    if t == 'e':
        for i in range(n):
            if i % 2 == 0:
                num_sum += i
    elif t == 'o':
        for i in range(n):
            if i % 2 != 0:
                num_sum += i
    else:
        num_sum = -1
    return num_sum


print(sum_eo_loop(10, 'e'))
print(sum_eo_loop(7, 'o'))
print(sum_eo_loop(11, 'spam'))


# Find sum of even or odd numbers in a range using range function
def sum_eo_range(n, t):
    if t == 'e':
        start = 0
    elif t == 'o':
        start = 1
    else:
        return -1
    return sum(range(start, n, 2))


print(sum_eo_range(10, 'e'))
print(sum_eo_range(7, 'o'))
print(sum_eo_range(11, 'spam'))


def fibonacci(n: int) -> int:
    """
        Return the `n` th Fibonacci number, for positive `n`.
        :param n: number
        :raises ValueError: if the supplied value `n` is negative.
    """
    if n < 0:
        raise ValueError("n = {} is negative. Please provide a positive number".format(n))

    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None

    for f in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


# print(fibonacci(-100))
print("Fibonacci series for n = 5")
for num in range(5):
    print(fibonacci(num))


# Function with default values
def print_text(text="Hello") -> None:
    print("Text is: {}".format(text))


print_text()
print_text("Hello World")


# Function with default values and function annotations
def print_text_fn(text: str = "Hello") -> None:
    print("Text is: {}".format(text))


print_text_fn("Hello World!!!")

# Passing *args to functions (Argument un-packing operator similar to spread operator in Javascript)
# Can use * with any sequence type
numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")      # (0, 1, 2, 3, 4, 5)
# numbers were unpacked and the unpacked numbers were passed to the print function,
# below code was actually executed as print(0, 1, 2, 3, 4, 5)
print(*numbers, sep=";")     # 0 1 2 3 4 5
print(0, 1, 2, 3, 4, 5, sep=";")


# Passing an unpacked sequence parameter to a function (so using *args as function argument)
# *args -> unpacked tuple, args -> tuple
def test_arg_unpacking_operator(*args):
    print(args)
    for x in args:
        print(x)


test_arg_unpacking_operator(0, 1, 2, 3, 4, 5)
print("==================")
test_arg_unpacking_operator()


# Function Parameter Rules
# Any positional-or-keyword arguments that we define MUST come first in the parameter list
# If we have any var-positional parameter (i.e. param starting with *), it must come after any positional-or-
# keyword arguments
# Any parameter defined after a var-positional parameter must be keyword-only arguments ( which includes
# var-keyword arguments )
# Any var-keyword arguments appear last

def func(p1, p2, *args: int, k, **kwargs) -> None:
    """
    Testing function parameter rules

    :param p1: Positional or keyword parameter `p1`
    :param p2: Positional or keyword parameter `p2`
    :param args: var-positional parameter `args`
    :param k: keyword parameter `k`. Should be passed with a keyword,
              else it will be considered as part of `*args` arguments
    :param kwargs: var-keyword parameter `kwargs`, also called keyword arguments.
                   Should be the last parameter
    :return: None
    """
    print("positional-or-keyword:...{},{}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)


