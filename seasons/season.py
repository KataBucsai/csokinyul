# Seasons handle the actual and the new season
# Here you can interract with the Farm Field
#
# Field data structure:
# date_year+month come with input as string
# field_size input as string
# 3 field part data in one bracket:
# first: Field ID
# second: Plant name
# third: neighborhood


# importing everything you need here. Beware from recursive import call!
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


# start this module checking actual season data
# user will go back to main manu if finished with the season field
#
# @season: string with two state "new" or "actual"
def start_module(season):
    actualseason_file_name = current_file_path + "/actualseason.csv"
    actual_table = data_read_write.get_datatable_from_file("actualseason.csv")

    if not actual_table:  # first season here
        actual_table = new_season(actual_table)
        data_read_write.write_datatable_to_file("actualseason.csv", actual_table)
        season = "actual"
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
# @season: list of list
def new_season(season_table):
    field = []
    season_date = season_table[0] if season_table else []
    field_size = ''
    if not season_table:
        ui.print_result("", "This is your first season")
        season_date = ui.get_inputs(["Year", "Month"], "What is the year and the month of your first season?")
        field_size = ui.get_inputs(["Field size (m)"], "Insert your Farm size")
        field.append(["".join([date for date in season_date]), ",".join([str(int(field_size[0])**2), field_size[0]])])
        for i in range(4):
            field.append(['0', str(i+1), '0'])
    ui.print_field(field, 2, season_date[0])
    return field


# handle actual season
#
# @season_table list of list
def actual_season(season_table):
    while True:
        ui.print_field(season_table, 2, season_table[0][0])
        field_plant = [get_field(), get_plant()]
        planting_finished = ui.get_inputs(["Yes(Y) or No(N)"], "Are you done with the planting?")
        if planting_finished == 'Y' or planting_finished == 'y'


# setting up field part atributes
#
def get_field():
    part_field = ui.get_inputs(["Field number"], "Select a field number")
    if part_field == '1':
        part_field.append("F2+F3")
    elif part_field == '2':
        part_field.append("F1+F4")
    elif part_field == '3':
        part_field.append("F1+F4")
    else:
        part_field.append("F2+F3")
    return part_field


# adding plant id to field part as second attribute
#
def get_plant():
    plants_table = data_read_write.get_datatable_from_file("data/plants.csv")
    ui.print_table(plants_table)
    part_field = ui.get_inputs(["Plant name"], "Select a plant")
    return part_field
