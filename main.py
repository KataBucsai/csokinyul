# this is the main part
import sys
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
print(current_file_path)
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/ui.py").load_module()
# Menu module
menu = SourceFileLoader("menu", current_file_path + "/menu.py").load_module() 


def main():
    while True:
        options_list = ["Actual season", "New season", "Show plants"]
        menu.handle_menu("Main menu", options_list, "Exit program")
        try:
            menu_list = ["season.start_module(actual)", "season.start_module(new)"]
            menu.choose(menu_list)
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()