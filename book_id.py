import csv
import os

def get_id():
    open('book.csv','a+')
    if os.stat("book.csv").st_size == 0:
        next_id = 1
    else:
        with open('book.csv', "r", newline = '') as data:
            reader = csv.reader(data, delimiter = ';')
            max_id = max(int(row[0]) for row in reader)
            next_id = max_id + 1
    return next_id
