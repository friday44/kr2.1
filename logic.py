import ui
import book_save as bs
import book_find as bf
import book_show as bsh
import book_del as bd
import book_edit as be


def button_click():
    operation = 0
    while operation != 6:
        try:
            operation = ui.get_comand()
            if operation == 1:
                bs.log_data(ui.get_data())
            elif operation == 2:
                ui.print_data(bf.find_data(ui.get_find_string()))
            elif operation == 3:
                ui.print_data(bsh.show_data())
            elif operation == 4:
                ui.print_data(be.edit_data(ui.get_find_string()))
            elif operation == 5:
                bd.del_data(ui.get_find_string())
                ui.rez_del_note()
            else:
                operation = 6
        except:
            print("Ошибка ввода. Введите число от 1 до 6")


def enter_first_menu() -> int:
   
    while True:
        try:
            answer = int(input("Please enter that do you want to do. \n" +
                               "enter 1: to add a new note,\nenter 2: to read one note,\n" +
                               "enter 3: to read all notes that you have,\nenter 4: to update an existing note,\n" +
                               "enter 5: to delete an existing note,\nenter 6: to exit the application\n"))
            if 0 <= answer <= 6:
                return answer
            else:
                print("You entered wrong number")
        except:
            print("You're wrong. Try again")


