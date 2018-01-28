import csv

individual_dates = []
date_names = dict()

with open ('blog/residenceRecord.csv', newline='') as record_file:
    imported_data = csv.reader(record_file, delimiter=',')

    for entry in imported_data:
        individual_dates.append(entry[0]) # creates list like ['date'] with only one date added per iteration
        individual_names = entry[1].split(', ')  # creates list like ['name', 'name', 'name']
        for name in individual_names:
            if name not in date_names:
                date_names[name] = []
            date_names[name].append(entry[0])

counted_dates = {k:len(v) for k, v in date_names.items()} # items makes dict into list of tuples

for key, value in sorted(counted_dates.items(), key=lambda k,v: v,k):
    print('%s: %d' % (key, value)) # look at print formatting to understand this...^^
