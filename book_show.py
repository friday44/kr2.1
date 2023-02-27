import csv

def show_data():
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result_all = []
        for row in reader:
            result_all.append(row)
    return result_all