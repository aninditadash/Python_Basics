import csv

countries_dataset = '../files/country_info.txt'

# In case we are fetching files from different sources, it is not feasible to examine the files to check the type
# of separators being used. CSV module Sniffer class examines a sample of the file and works out the separators,
# characters used to delimit the strings, etc. It uses that sample to create a dialect.
# A Dialect is a way to group all CSV settings together into a single object. We can specify delimiter, escapechar,
# quotechar, etc. when calling the reader function.

with open(countries_dataset, encoding='utf-8', newline='') as countries_data:
    # create a sample for the sniffer class
    sample = countries_data.read()
    # read() method read the complete file, the below code would not give any output, so reposition the file pointer
    # pass the sample to the object of the Sniffer class
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    print(f"country_dialect = {country_dialect}")
    # seek() is used to position the file pointer to another position in the file, here passing 0 tells the file
    # pointer to start reading from the beginning of the file
    countries_data.seek(0)
    # Sniffer worked out the fields are delimited by the | character and reader used the dialect that sniff created
    # to correctly parse the data. However, examine data files in editor whenever possible.
    reader = csv.reader(countries_data, dialect=country_dialect)
    for row in reader:
        print(row)

print("================================================================================")

# Above method reads the file twice, hence it is not a efficient solution especially in case of large files.
# sniff() only needs a sample of the file (2 or 3 lines are sufficient)
with open(countries_dataset, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)
    reader = csv.reader(countries_data, dialect=country_dialect)
    for row in reader:
        print(row)

print("================================================================================")

attributes = [
    'delimiter',
    'doublequote',
    'escapechar',
    'lineterminator',
    'quotechar',
    'quoting',
    'skipinitialspace'
]

for attribute in attributes:
    print(f"{attribute}: {getattr(country_dialect, attribute)}")

print("================================================================================")

# Python repr() function returns a printable representation of the object by converting that object to a string.
# \r - carriage return
# \n - line feed
for attribute in attributes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
