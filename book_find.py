import csv

def find_data(find_str):
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            if find_str in row:
                result.append(row)
        # else:
        #     result.append('Не найдено')
    
    return result

