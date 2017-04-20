# this is the main part
import sys
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/ui.py").load_module()
# Fieldview module
field = SourceFileLoader("field", current_file_path + "/fieldview/field.py").load_module()
# Seasons module
season = SourceFileLoader("season", current_file_path + "/seasons/season.py").load_module() 
# General module
general = SourceFileLoader("general", current_file_path + "/general.py").load_module() 
# Data_read_write module
data_read_write = SourceFileLoader("data_read_write", current_file_path + "/data_read_write.py").load_module()
# Menu module
menu = SourceFileLoader("menu", current_file_path + "/menu.py").load_module() 


def main():
    while True:
        menu.handle_menu()
        try:
            menu.choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()