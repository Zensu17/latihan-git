import csv

with open('inputfile.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('outputfile.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            if int(row[0]) > 50: 
                writer.writerow(row)