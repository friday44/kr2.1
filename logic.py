import ui
import book_save as bs
import book_find as bf
import book_show as bsh
import book_del as bd


def button_click():
    operation = 0
    while operation != '6':
        operation = ui.get_comand()
        if operation == '1':
            bs.log_data(ui.get_data())
            
        elif operation == '2':
            ui.print_data(bf.find_data(ui.get_find_string()))
            
        elif operation == '3':
            ui.print_data(bsh.show_data())

        elif operation == '4':
            ui.print_data(bf.find_data(ui.get_find_string())) # + принять новую запись и перезаписать файл без старой заметки, но с новой

        elif operation == '5':
            bd.del_data(ui.get_find_string())
            print('Заметка удалена')
            
        else:
            operation = '6'