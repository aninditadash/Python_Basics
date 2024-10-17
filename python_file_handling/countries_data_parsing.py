# Making sense of data is called parsing, parsing data/code means splitting it up to logical components
countries_dataset = '../files/country_info.txt'
countries = {}
all_countries = {}

with open(countries_dataset) as countries_data:
    countries_data.readline()
    for row in countries_data:
        data = row.strip('\n').split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country-code-2': code,
            'country-code-3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        print(country_dict)
        countries[country.casefold()] = country_dict
        all_countries[country.casefold()] = country_dict
        # We can also make the country code as the key and assign it the country object
        # In this way, we can access the country using country name or the 2-digit country code
        countries[code.casefold()] = country_dict

def check_country():
    while True:
        chosen_country = input("Please enter a country name or code: ")
        country_key = chosen_country.casefold()
        if country_key in countries:
            print(f"Capital of {chosen_country} is {countries[country_key]['capital']}")
            break
        elif country_key == 'q':
            break
        else:
            print("Wrong country name!!, please try again.")

# check_country()

# Print all countries which don't have a capital city
for country_name, country_obj in all_countries.items():
    if country_obj['capital'] == "":
        print(f"{country_name.capitalize()}")

