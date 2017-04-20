import os
import sys
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


def handle_menu(title, options_list, exit_message):
    os.system("clear")
    ui.print_menu(title, options_list, exit_message)


def choose(option_list):
    inputs = ui.get_inputs(["Please choose an options"], "")
    option = inputs[0]
    for i, opts in enumerate(option_list):
        if option == str(i+1):
            opts()
    if option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")