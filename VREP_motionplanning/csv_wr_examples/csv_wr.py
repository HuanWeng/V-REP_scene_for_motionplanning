import csv

#Write csv file.
A = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]]
with open('test.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    for row in A:
        csvwriter.writerow(row)

#Read csv file.
B = []
with open('test.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',', quoting = csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        B.append(row)
