from primes_and_squares import squares_generator, primes_generator

even_num_set = set(range(0, 50, 2))
odd_num_set = set(range(1, 50, 2))

print(f"even_num_set = {even_num_set}")
print(f"odd_num_set = {odd_num_set}")

primes = set(primes_generator(100))
print(f"primes = {primes}")

perfect_squares = set(squares_generator(100))
print(f"squares = {perfect_squares}")

print("================================================================================")

print("Intersection of odd_num_set and perfect_squares")
print(odd_num_set.intersection(perfect_squares))
print("Intersection of even_num_set and perfect_squares")
print(even_num_set & perfect_squares)

print("================================================================================")

# Pass an iterable to a method
even_squares = even_num_set.intersection(squares_generator(100))
print(f"even_squares = {even_squares}")

print("================================================================================")

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "deer", "horse"}
potential_rides = {"donkey", "horse", "camel"}

intersection = farm_animals & wild_animals & potential_rides
print(f"farm_animals & wild_animals & potential_rides = {farm_animals & wild_animals & potential_rides}")