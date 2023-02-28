import csv

def log_data(entry):
    with open('book.csv', 'a+', newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(entry)