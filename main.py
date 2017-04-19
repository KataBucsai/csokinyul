# this will be the main part of your FRP
import sys
import os
import ui  # User Interface
import general
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# Store module
fieldview = SourceFileLoader("fieldview", main_path + "/fieldview/field.py").load_module()


def handle_menu():
    os.system("clear")
    options = ["Store manager",
               "Human resources manager",
               "Tool manager",
               "Accounting manager",
               "Selling manager",
               "Customer Relationship Management (CRM)"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
            handle_menu()
            try:
                general.choose()
            except KeyError as err:
                ui.print_error_message(err)

if __name__ == '__main__':
    main()