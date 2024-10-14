from prescription_data import adverse_interactions

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "deer", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(f"all_animals_1 = {all_animals_1}")

all_animals_2 = wild_animals.union(farm_animals)
print(f"all_animals_2 = {all_animals_2}")

all_animals_3 = wild_animals | farm_animals
print(f"all_animals_3 = {all_animals_3}")

print("================================================================================")

print(f"adverse_interactions = {adverse_interactions}")
meds_to_watch = set()
for interaction in adverse_interactions:
    # print(interaction)
    # meds_to_watch = meds_to_watch.union(interaction)
    # meds_to_watch = meds_to_watch | interaction
    # Instead of creating new set each time in the loop, we can use update method
    # meds_to_watch.update(interaction)
    meds_to_watch |= interaction # Using augmented operator

print(f"meds_to_watch = {sorted(meds_to_watch)}")

print("================================================================================")

# Advantages of set operation methods over the operators
# The set operation methods will take any iterable as an argument whereas operators will only take sets as arguments.
print("Advantages of set operation methods over the set operators")
meds_to_watch_new = set()
# Here we are sending the unpacked list to the set variable (meds_to_watch_new) update method
meds_to_watch_new.update(*adverse_interactions)
print(f"meds_to_watch_new = {sorted(meds_to_watch_new)}")

print(*meds_to_watch_new, sep="\n")
