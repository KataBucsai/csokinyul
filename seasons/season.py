# will handle the first season and other new seasons
# will send every input into the actual season

# data structure:
# id: string Unique
# title: string
# date: string


# importing everything you need
import os
import main
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
field = SourceFileLoader("common", current_file_path + "/../field/field.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module(season):
    actualseason_file_name = current_file_path + "/actualseason.csv"
    actual_table = data_manager.get_table_from_file(file_name)

    if not actual_table and season == "new": # first season here
        actual_table = new_season(actual_table)
    if season == "new":
        # future: export actual season to history and clear it 
        actual_table = new_season(actual_table)
    if actual_table or season == "actual":
        actual_table = actual_season()
        

    while True:
        os.system("clear")
        ui.print_menu("Selling", options, "Back to Main menu")

        ui.get_inputs(["Press a key to continue"], "")


# handle new season
#
# @season list of list
def new_season(season_table):
    field = []
    if not season:
        ui.print_result("This is your first season")
        season_date = ui.get_inputs(["Year", "Month"], "What is the year and the month of your first season?")
        field.append("".join(date for date in season_date))
        field_size = ui.get_inputs(["Field Width (m)", "Field Length (m)"], "Insert your Farm size")
        field.append(",".join([int(field_size[0]) * int(field_size[1]), field_size[0], field_size[1]]))
    ui.print_field()

    return field


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    os.system("clear")
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    return ui.print_table(table, title_list)