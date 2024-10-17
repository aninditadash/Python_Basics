# CSV module provides DictReader which produces rows of dictionaries, we can pass the same format options
# like delimiter also Dialect, to specify all the options in a single object.
import csv

cereals_filename = '../files/cereal_grains.csv'

with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)

# DictReader automatically reads the column names from the CSV file its reading and uses those names for the
# individual dictionary keys. However, in case there is no header row in the file or when creating a CSV file using
# DictWriter, we can pass a list containing the keys, to these objects, in the fieldnames argument.

print("================================================================================")

countries_dataset = '../files/country_info.txt'
countries = {}

dialect = csv.excel
dialect.delimiter = '|'

with open(countries_dataset, encoding='utf-8', newline='') as countries_file:
    # Get the column headings from the first line of the file
    headings = countries_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    reader = csv.DictReader(countries_file, dialect=dialect, fieldnames=headings)
    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries['afghanistan'])
