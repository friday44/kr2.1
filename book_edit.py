import csv
import ui

def edit_data(find_str):
    open('book.csv','a+')
    with open('book.csv', "r", newline = '') as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str in row:
                result.append(ui.get_edit_data(find_str))
            else:
                result.append(row)
       
    with open('book.csv', "w", newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerows(result)