# Processing the prescriptions of the patients
from prescription_data import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    patient = trial_patients.pop()
    print(f"{patient}: {patients[patient]}")
