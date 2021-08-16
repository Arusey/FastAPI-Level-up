import csv


with open('newcvs.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # get the fields names through the first row
    fields = next(csv_reader)
    for row in csv_reader:
        row.append(row)

    print("total number of rows: %d"(csv_reader.line_num))

