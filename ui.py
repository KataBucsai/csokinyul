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