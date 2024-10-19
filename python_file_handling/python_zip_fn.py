# zip() function. Pass iterables to it, and it returns an iterable containing tuples. e.g. if you provide 2 lists
# then the tuple will contain 2 items, one from each list, in turn.
import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']

for row in albums:
    zip_obj = zip(keys, row)
    albums_dict = dict(zip_obj)
    print(albums_dict)
    for thing in zip(keys, row):
        print("\t", thing)

albums_outfile_name = '../files/albums.csv'

with open(albums_outfile_name, 'w', encoding='utf-8', newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keys, quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in albums:
        zip_obj = zip(keys, row)
        albums_dict = dict(zip_obj)
        writer.writerow(albums_dict)
