import csv

def get_id():
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        print('hello')
        for row in reader:
            #print(f'row0={row[0]}')
            max_id = max((row[0]))
            print(f'max_id={max_id}')
    
    return max_id
