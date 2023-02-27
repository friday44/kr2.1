import ui
import book_save as bs
import book_find as bf
import book_show as bsh


def button_click():
    operation = 0
    while operation != '4':
        operation = ui.get_comand()
        if operation == '1':
            bs.log_data(ui.get_data())
            
        elif operation == '2':
            ui.print_data(bf.find_data(ui.get_find_string()))
            
        elif operation == '3':
            ui.print_data(bsh.show_data())
            
        else:
            operation = '4'