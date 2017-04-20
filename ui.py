from terminaltables import AsciiTable
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# general module
general = SourceFileLoader("general", current_file_path + "/general.py").load_module()


# This function needs to print outputs like this:
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    table_items = [title_list]
    for item in table:
        table_items.append(item)
    table = AsciiTable(table_items)
    table.inner_heading_row_border = True
    table.inner_row_border = True
    print(table.table)


# This function needs to generate outputs like this:
# Main menu:
# (1) Actual Season
# (2) New Season
# (3) Plants
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):  # ready to use
    numbers = [str(i+1) for i in range(len(list_options))]
    print(title + ":")
    for pos, option in enumerate(list_options):
        print("(" + numbers[pos] + ") " + option)
    print("(0) " + exit_message)


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print("\n" + label)
    print(result)
    print("\n")

    
# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    print(title)
    if len(list_labels) < 2:
        return input(list_labels[0] + ": ")
    else:
        inputs = []
        for items in list_labels:
            inputs.append(input(items + ": "))
        return inputs


# This function needs to print outputs like this:
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_field(field, size, season_date):
    os.system('clear')
    field_spot = [[field[i][1], field[i+1][1]] for i in range(1, len(field), size)]
    len_row = sum(general.get_table_elements_length(field_spot))
    print_first_row = []
    print_rows = []
    print("\n")
    print("Season " + season_date + "\n")
    for i in range(size):
        for j in range(size):
            if j == 0:
                print_rows.append("  " + field_spot[i][j])
            else:
                print_rows.append(" | " + field_spot[i][j])
        print("".join(print_rows))
        print_rows = []
        if i <= (size-2):
            print("  " + "-" * (len_row + size*2))


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print("Error: " + str(message))