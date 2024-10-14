# We have a set of trial patients for whom Warfarin should be substituted with Edoxaban
# For other patients not taking Warfarin, Edoxaban should NOT be prescribed as it will be damaging to patients.

from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
# for patient in trial_patients:
#     prescription = patients[patient]
#     # Instead of using below condition, we can use Exceptions and handle them when we get error using remove()
#     if warfarin in prescription:
#         prescription.remove(warfarin)
#         prescription.add(edoxaban)
#     else:
#         print(f"Patient {patient} is not taking Warfarin. Please remove Kenny from the trial")
#     print(f"{patient}'s prescriptions = {prescription}")

# Remove Warfarin and add Edoxaban by handling Exception
for patient in trial_patients:
    prescription = patients[patient]
    print(f"{patient}'s prescriptions : {prescription}")
    # Instead of using below condition, we can use Exceptions and handle them when we get error using remove()
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin. Please remove Kenny from the trial.\n")
    print(f"{patient}'s prescriptions = {prescription}\n")
