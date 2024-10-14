from primes_and_squares import squares_generator, primes_generator

even_num_set = set(range(0, 50, 2))
odd_num_set = set(range(1, 50, 2))

print(f"even_num_set = {even_num_set}")
print(f"odd_num_set = {odd_num_set}")

primes = set(primes_generator(100))
print(f"primes = {primes}")

perfect_squares = set(squares_generator(100))
print(f"squares = {perfect_squares}")

# Find set of odd numbers that are not prime, we have to take difference of odd numbers set and prime numbers
print(f"odd_num_set.difference(primes) = {odd_num_set.difference(primes)}")
print(f"odd_num_set - primes = {odd_num_set - primes}")
print(f"primes - odd_num_set = {primes - odd_num_set}")

