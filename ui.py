import datetime
from constants import *
import book_id
import csv

def get_comand():
    print('1 - добавление заметки')
    print('2 - поиск заметки')
    print('3 - показать все заметки')
    print('4 - редактировать заметку')
    print('5 - удалить заметку')
    print('6 - выход из программы')
    return input('Введите номер операции: ')

def get_data():
    now = datetime.datetime.now()
    book_entry = []
    book_entry.append(book_id.get_id())
    book_entry.append(input('Введите заголовок заметки: '))
    book_entry.append(input('Введите текст заметки: '))
    book_entry.append(now.strftime("%d-%m-%Y %H:%M"))
    return book_entry

def get_find_string():
    return input('Введите слово для поиска: ')

def get_edit_note():
    return input('Введите номер заметки для редактирования: ')

def get_del_note():
    return input('Введите номер заметки для удаления: ')

def print_data(data):
    print(data)
    # for i in data:
    #     for j in i:
    #         print(j)
