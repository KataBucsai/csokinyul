# will handle the first season and other new seasons
# will send every input into the actual season

# data structure:
# id: string Unique
# title: string
# date: string


# importing everything you need
import sys
import os
import main
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# Fieldview module
field = SourceFileLoader("field", current_file_path + "/../fieldview/field.py").load_module()
# Data_read_write module
data_read_write = SourceFileLoader("data_read_write", current_file_path + "/../data_read_write.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module(season):
    actualseason_file_name = current_file_path + "/actualseason.csv"
    actual_table = data_read_write.get_datatable_from_file(actualseason_file_name)

    if not actual_table:  # first season here
        actual_table = new_season(actual_table)
    while actual_table:
        if season == "new":
            # future: export actual season to history and clear it
            actual_table = new_season(actual_table)
            data_read_write.write_datatable_to_file("actualseason.csv", actual_table)
        elif actual_table or season == "actual":
            actual_table = actual_season(actual_table)
        else:
            main.main()


# handle new season
#
# @season list of list
def new_season(season_table):
    field = []
    season_date = ""
    field_size = ""
    if not season_table:
        ui.print_result("", "This is your first season")
        season_date = ui.get_inputs(["Year", "Month"], "What is the year and the month of your first season?")
        field_size = ui.get_inputs(["Field size (m)"], "Insert your Farm size")
        field.append(["".join([date for date in season_date]), ",".join([str(int(field_size[0]) ** 2), field_size[0]])])
        for i in range(4):
            field.append(["0", "0", "0"])
    ui.print_field(field, 2, season_date[0])
    return field


def actual_season(season_table):
    while True:
        field_plant = get_field_plant()
        return 1


def get_field_plant():
    part_field = ui.get_inputs(["Field number", "Plant name"], "Select a field number and a plant")
    if part_field == "1":
        part_field.append("F2+F3")
    elif part_field == "2":
        part_field.append("F1+F4")
    elif part_field == "3":
        part_field.append("F1+F4")
    else:
        part_field.append("F2+F3")
    return part_field


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    os.system("clear")
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    return ui.print_table(table, title_list)