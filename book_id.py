import csv

def get_id():
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        max_id = max(int(row[0]) for row in reader)
        next_id = max_id + 1
    
    return next_id
