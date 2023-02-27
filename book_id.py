import csv

def get_id():
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        for row in reader:
            max_id = max(int(row[0]))
    
    return max_id
