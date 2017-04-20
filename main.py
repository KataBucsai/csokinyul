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
# Seasons module
season = SourceFileLoader("season", current_file_path + "/seasons/season.py").load_module()
# Data_read_write module
data_read_write = SourceFileLoader("data_read_write", current_file_path + "/data_read_write.py").load_module()


def choose():
    inputs = ui.get_inputs(["Please choose an options"], "")
    option = inputs[0]
    if option == "1":
        season.start_module("actual")
    if option == "2":
        season.start_module("new")
    if option == "3":
        plants_table = data_read_write.get_datatable_from_file("data/plants.csv")
        ui.print_table(plants_table)
        ui.get_inputs(["Press a key to continue"], "")
    if option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def main():
    while True:
        options_list = ["Actual season", "New season", "Show plants"]
        menu.handle_menu("Main menu", options_list, "Exit program")
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()