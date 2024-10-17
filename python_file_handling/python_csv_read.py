import csv

csv_filename = '../files/cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    # We are telling the reader() function that the data has been quoted
    # QUOTE_NONNUMERIC tells that all non-numeric values have been quoted
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
