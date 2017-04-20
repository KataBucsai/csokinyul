'''
# importing everything you need
import sys
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    file_name = current_file_path + "/sellings.csv"
    table = data_manager.get_table_from_file(file_name)

    # menu options
    options = ["Show table",
               "Add new record",
               "Remove a record",
               "Update an existing record",
               "Extra: Lowest priced item ID",
               "Extra: Items sold between two dates"]

    while True:
        os.system("clear")
        ui.print_menu("Selling", options, "Back to Main menu")

        # choose
        inputs = ui.get_inputs(["Please enter a number"], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            table = add(table)
            data_manager.write_table_to_file(file_name, table)
        elif option == "3":
            id_ = common.get_id()
            table = remove(table, id_)
            data_manager.write_table_to_file(file_name, table)
        elif option == "4":
            id_ = common.get_id()
            table = update(table, id_)
            data_manager.write_table_to_file(file_name, table)
        elif option == "5":
            lowest_price = get_lowest_price_item_id(table)
            ui.print_result(lowest_price, "ID with the lowest price:")
        elif option == "6":
            dates = ui.get_inputs(dates_table, "Please insert the dates")
            between_table = get_items_sold_between(table, dates[0], dates[1], dates[2],
                                                   dates[3], dates[4], dates[5])
            show_table(between_table)
        elif option == "0":
            main.main()
        else:
            raise KeyError("There is no such option.")
        ui.get_inputs(["Press a key to continue"], "")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    os.system("clear")
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    return ui.print_table(table, title_list)
'''