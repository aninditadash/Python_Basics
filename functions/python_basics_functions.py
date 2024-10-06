from _functools import reduce
# Arguments in Python can be matched by position or name.
# Positional arguments are required to be mentioned in the same order as in the function definition
# Keyword arguments are referenced by name and may be in any order
# Positional and keyword arguments can be mixed in a function call
# Arbitrary arguments => Python allows passing variable number of arguments by using special symbols.
# *args => Non-keyword arguments
# **kwargs => Keyword arguments
# Python returns None by default

# Python Lambda functions are anonymous functions and can be defined by using the keyword lambda. A lambda function
# can have any no. of arguments but contains only 1 expression. Lambda functions are syntactically restricted to a
# single expression which is evaluated and returned. It is possible to define a lambda function without assigning
# it to a variable or explicitly calling it.

def greetings(name, greeting):
    print(f"{greeting}, {name}!!")

greetings("John", "Hello")              # Positional argument
greetings(greeting="Hi", name="Anna")   # Keyword argument
# greetings(name="Joey", "Hello")       # Gives SyntaxError: positional argument follows keyword argument
# greetings("Hello", name="Joey")       # Gives TypeError: greetings() got multiple values for argument 'name'
greetings("Hello", greeting="Joey")
greetings("Joey", greeting="Hello")

def greetings_default(name, greeting="Hello"):
    print(f"{greeting}, {name}!!")

greetings_default("Jane")

print("================================================================================")

def is_palindrome(word: str) -> bool:
    """
    Check if the word is a palindrome.
    :param word: word to be checked if it is a palindrome
    :return: True or False
    """
    backwards = word[::-1]
    return backwards.casefold() == word.casefold()

print(is_palindrome("hello"))
print(is_palindrome("pep"))

print("================================================================================")

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

print("================================================================================")

print("Using global values inside a function")
var = 10
def foo1():
    square = var ** 2
    print(f"square = {square}")

foo1()

print("================================================================================")

# We should not create local variables with the same name as global variables as it will shadow the global variable
print("Having local and global variables with the same name")
var_2 = 10
def foo2():
    global var_2
    var_2 = 0
    print(f"var_2 = {var_2} global var_2 = {var_2}")

foo2()

print("================================================================================")

# Creating or manipulating global variables inside a function
print("Creating or manipulating global variables inside a function")
var_1 = 15
print(f"Before function call: var = {var_1}")
def foo():
    global var_1      # Not defining global var => giving error in next as var is not defined
    var_1 *= 5
    print(f"Inside function: var = {var_1}")

foo()
print(f"After function call: var = {var_1}")

print("================================================================================")

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

print(f"sum_eo_loop(10, 'e')    {sum_eo_loop(10, 'e')}")
print(f"sum_eo_loop(7, 'o')     {sum_eo_loop(7, 'o')}")
print(f"sum_eo_loop(11, 'spam') {sum_eo_loop(11, 'spam')}")

# Find sum of even or odd numbers in a range using range function
def sum_eo_range(n, t):
    if t == 'e':
        start = 0
    elif t == 'o':
        start = 1
    else:
        return -1
    return sum(range(start, n, 2))

print(f"sum_eo_range(10, 'e')    {sum_eo_range(10, 'e')}")
print(f"sum_eo_range(7, 'o')     {sum_eo_range(7, 'o')}")
print(f"sum_eo_range(11, 'spam') {sum_eo_range(11, 'spam')}")

print("================================================================================")

# Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.
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
for num in range(6):
    print(f"fibonacci({num}) = {fibonacci(num)}")

print("================================================================================")

# Function with default values
print("Function with default values")
def print_text(text="Hello") -> None:
    print("Text is: {}".format(text))

print_text()
print_text("Hello World")

print("================================================================================")

# Function with default values and function annotations
# These expressions are evaluated at compile time and have no life in python’s runtime environment.
# Python does not attach any meaning to these annotations.
def print_text_with_annotation(text: str = "Hello") -> None:
    print("Text is: {}".format(text))


print_text_with_annotation("Hello World!!!")

print("================================================================================")

# Passing *args to functions (Argument un-packing operator similar to spread operator in Javascript)
# Can use * with any sequence type
numbers = (0, 1, 2, 3, 4, 5)
print(numbers, sep=";")      # (0, 1, 2, 3, 4, 5)
# numbers were unpacked and the unpacked numbers were passed to the print function,
# below code was actually executed as print(0, 1, 2, 3, 4, 5)
print(*numbers, sep=" ; ")          # 0 ; 1 ; 2 ; 3 ; 4 ; 5
print(0, 1, 2, 3, 4, 5, sep=" ; ")    # 0 ; 1 ; 2 ; 3 ; 4 ; 5

# Passing an unpacked sequence parameter to a function (so using *args as function argument)
# *args -> unpacked tuple, args -> tuple
def test_arg_unpacking_operator(*args):
    print(args)
    for x in args:
        print(x)

test_arg_unpacking_operator(0, 1, 2, 3, 4, 5)
test_arg_unpacking_operator()

print("================================================================================")

# Arbitrary arguments
def find_sum(*args):                    # Non-Keyword arbitrary arguments
    total = 0
    for i in args:
        total += i
    print(f"Sum = {total}")


find_sum(10, 20)
find_sum(100, 30, 45, 78, 100)

print("================================================================================")

def get_information(**kwargs):          # Keyword arbitrary arguments
    for key, value in kwargs.items():
        print(f"{key} = {value}")

get_information(name="John Doe", age=34)
get_information(name="Jane Doe", age=30, location="Philadelphia", country="USA", jobTitle="Software Engineer")

print("================================================================================")

# Function Parameter Rules
# Any p
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
    print("\npositional-or-keyword:...{},{}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword: k.................{}".format(k))
    print("var-keyword: (**kwargs).............{}".format(kwargs))

func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)
func(1, 2, 3, 4, 5, 9, 6, 7, key1=7, key2=8, k=3)

print("================================================================================")

# Built-in functions in Python
# Built-in functions facilitate functional programming in Python
print(dir(__builtins__))

print("================================================================================")

print("Lambda functions")

adder = lambda x, y: x + y
print(f"adder(5, 5) = {adder(5, 5)}")

adderWithArgs = lambda *args: sum(args)
print(f"adderWithArgs(5, 5) = {adderWithArgs(5, 4, 10, 57, 89, 100, 34)}")

evenOdd = lambda n: "EVEN" if (n % 2 == 0) else "ODD"
print(f"evenOdd(9) = {evenOdd(9)}")
print(f"evenOdd(8) = {evenOdd(8)}")

print("================================================================================")

# map function => used to apply a function to each element of an iteration object
# map function => 2 arguments => a function and an iterable object
# it generates an iterator which can be converted to a list or iterated using a loop
# Can use a lambda function for its implementation
def squared(n):
    return n * n

num_list = [10, 3, 18, 30, 89, 11, 13]
num_list_squared = list(map(squared, num_list))
num_list_squared_lambda = list(map(lambda x: x * x, num_list))
print(f"num_list_squared = {num_list_squared} num_list_squared_lambda = {num_list_squared_lambda}")

words = ["Apple", "Banana", "Cherry"]
words_first_char = list(map(lambda x: x[0], words))
print(f"words_first_char = {words_first_char}")

words_1 = ["Python", "PYTHON", "PYThon", "pYThon"]
words_1_upper = list(map(lambda x: x.upper(), words_1))
print(f"words_1_upper = {words_1_upper}")

print("================================================================================")

# filter function => used to filter data based on a condition defined in a function
# filter function => 2 arguments => a function and an iterable object and applies to
# each element of the iteration object and returns a boolean value.
def find_odd(n):
    return n % 2

numbers_tuple = {37, 90, 56, 43, 67, 89, 90, 35, 39}
numbers_list_odd = list(filter(find_odd, numbers_tuple))
numbers_list_odd_lambda = list(filter(lambda x: x % 2, numbers_tuple))
print(f"numbers_list_odd = {numbers_list_odd} numbers_list_odd_lambda = {numbers_list_odd_lambda}")

print("================================================================================")

# reduce function => used to implement the mathematical technique of folding on an iteration object.
# reduce function => 2 arguments => a function and an iterable object
# it applies the function continually to each element of the iterable object and produces a single
# cumulative value. reduce function is imported from _functools.
num_list_reduce = [2, 4, 6, 8, 10]
res = reduce(lambda x, y: x + y, num_list_reduce)
print(f"res of reduce function = {res}")

num_list_find_largest = [37, 190, 56, 43, 67, 189, 90, 3500, 3501]
find_largest = reduce(lambda x, y: x if x > y else y, num_list_find_largest)
print(f"find_largest = {find_largest}")
