import csv


with open("us-counties.csv", newline = '') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ",")
    for row in reader:
        print (row['date'], '|', row ['county'], '|', row ['state'],'|', row ['fips'],'|', row ['cases'],'|', row ['deaths'] )