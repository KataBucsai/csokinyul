# this will be the main part of your FRP
import sys
import os
import ui  # User Interface
import general
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# Store module
fieldview = SourceFileLoader("fieldview", main_path + "/fieldview/field.py").load_module()


def choose():
    inputs = ui.get_inputs(["Please enter a number"], "")
    option = inputs[0]
    if option == "1":
        .actual_season()
    elif option == "2":
        .new_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    os.system("clear")
    options = ["Actual season",
               "New season"]

    ui.print_menu("Main menu", options, "Exit program")


def main():
    while True:
            handle_menu()
            try:
                choose()
            except KeyError as err:
                ui.print_error_message(err)

if __name__ == '__main__':
    main()