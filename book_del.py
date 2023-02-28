import csv

def del_data(find_str):
    open('book.csv','a+')
    with open('book.csv', "r", newline = '') as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str not in row:
                result.append(row)
       
    with open('book.csv', "w", newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerows(result)