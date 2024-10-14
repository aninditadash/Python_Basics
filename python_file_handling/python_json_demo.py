import json
from urllib.request import urlopen

# Reading from a JSON file
json_data_source = '../files/temperature_anomaly.json'
with open(json_data_source, encoding='utf-8') as temperature_data:
    temp_anomalies = json.load(temperature_data)

print(temp_anomalies['description'])
for year, value in temp_anomalies['data'].items():
    year, value = int(year), float(value)
    print(f"{year} : {value:6.2f}")

print(temp_anomalies['citation'])

print("================================================================================")

# Reading from a URL returning a JSON
json_data_source_url = 'https://dummyjson.com/products'
with urlopen(json_data_source_url) as json_stream:
    # urlopen() function does not allow to specify an encoding, so we decode the data to utf-8 after reading
    json_data = json_stream.read().decode('utf-8')
    products_data = json.loads(json_data)

print(products_data)
print(products_data['products'][0])


