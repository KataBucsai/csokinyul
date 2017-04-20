from terminaltables import AsciiTable


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
# (1) Field View
# (2) Plants manager
# (3) Disease manager
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):  # ready to use
    numbers = [str(i+1) for i in range(len(list_options))]
    print(title + ":")
    for pos, option in enumerate(list_options):
        print("(" + numbers[pos] + ")" + option)
    print("(0)" + exit_message)


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


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print("Error: " + str(message))