# Parsing the country_info.txt using CSV DictReader module
import csv

countries_dataset = '../files/country_info.txt'
countries = {}

with open(countries_dataset, encoding='utf-8', newline='') as countries_file:
    reader = csv.DictReader(countries_file, delimiter='|')
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

print(countries)

while True:
    chosen_country = input("Please enter a country name or code: ")
    country_key = chosen_country.casefold()
    if country_key in countries:
        print(f"Capital of {chosen_country} is {countries[country_key]['Capital']}")
        break
    elif country_key == 'q':
        break
    else:
        print("Wrong country name!!, please try again.")
