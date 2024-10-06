# Generators are special type of function in Python that return an iterator object with a sequence of values
# A generator uses a yield statement instead of return statement
# A generator object can be iterated only once
# A function with a yield statement is termed as generator

# Difference between return and yield statement
# return statement implies that the function is returning control of execution to the point from where the function
# is called. This process destroys the local variable and values generated.
# yield statement implies that the transfer of control is temporary. Hence, it does not destroy the state of local
# variables of the function.

def myGenerator():
    n = 1
    print("First iteration")
    yield "Number 1: n = " + str(n)

    n += 2
    print("Second iteration")
    yield "Number 2: n = " + str(n)

    n += 3
    print("Third iteration")
    yield "Number 3: n = " + str(n)

# Approach 1 using next()
gen = myGenerator()
print(gen)
print(next(gen), '\n')
print(next(gen), '\n')
print(next(gen), '\n')

print("================================================================================")

# Approach 2 using for loop
def myGenerator_forLoop():
    m = 1
    print("First iteration")
    yield "Number 1: n = " + str(m)

    m += 2
    print("Second iteration")
    yield "Number 2: n = " + str(m)

    m += 3
    print("Third iteration")
    yield "Number 3: n = " + str(m)

gen_for_loop = myGenerator_forLoop()
for value in gen_for_loop:
    print(value, '\n')
