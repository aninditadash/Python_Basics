# CSV stands for Comma Separated Values. A CSV file contains rows of data, with each row having the same number
# of fields. Each field is separated by some character.
import csv

# When we specify empty string for newline, line endings will be passed untranslated into the strings we read.
# That means csv reader fn will receive the newline characters that were in original file. CSV modules handle the
# newline translation itself. When writing, providing empty string for newline means that open() will not perform
# any translation of newline characters, because CSV module will handle this.
# Instead of open() performing the newline characters translation, CSV reader and writer modules will perform the task.

csv_file_name = '../files/OlympicMedals_2020.csv'

with open(csv_file_name, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')
    countriesByRank = {}
    print(f"Column headers: {headers}")
    # each line in the file will be parsed into fields, and we will get a list for each row
    # OlympicMedals_2020.csv file does not have quotes around strings, so below parameter quoting=csv.QUOTE_NONNUMERIC
    # converts all fields to floats, hence we get ValueError: could not convert string to float: 'United States'.
    # CSV Sniffer Class helps us to visualise the csv data
    # reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    reader = csv.reader(csv_file)
    for row in reader:
        rank, country, goldMedalCount, silverMedalCount, bronzeMedalCount, totalMedalCount = row
        countriesByRank[rank] = {
            'countryName': country,
            'goldMedals': int(goldMedalCount),
            'silverMedals': int(silverMedalCount),
            'bronzeMedals': int(bronzeMedalCount),
            'totalMedals': int(totalMedalCount)
        }

print(countriesByRank)


