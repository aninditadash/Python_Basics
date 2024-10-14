import copy

def deep_copy(d: dict) -> dict:
    """
    Create a deep copy of the dictionary, also copies `list` and `dict` values.
    :param d: dictionary to copy
    :return: A deep copy of `d`
    """
    deep_copy_dict = {}
    for key, value in d.items():
        deep_copy_dict[key] = value.copy()

    return deep_copy_dict

original = {
    "Anne": ["Software engineer", [32, "Bangalore"]],
    "Ashmita": ["Student", [6, "Cyprus"]]
}

copy_1 = copy.deepcopy(original)
copy_2 = deep_copy(original)

original["Anne"].append("54")
original["Ashmita"].append("21")

original["Anne"][1].append("India")
original["Ashmita"][1].append("Europe")

print(f"original {original}")
print(f"copy_1   {copy_1}")
print(f"copy_2   {copy_2}")

