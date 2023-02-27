import csv

def del_data(find_str):
    with open('book.csv', "r") as data:
        reader = csv.reader(data, delimiter = ';')
        result = []
        for row in reader:
            count = 0
            if find_str in row:
                count +=1
            else:    
                result.append(row)
    #print(result)    
    with open('book.csv', "w") as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerows(result)