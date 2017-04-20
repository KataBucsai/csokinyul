# Here will be the general function
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
# Menu module
menu = SourceFileLoader("menu", current_file_path + "/menu.py").load_module()
# Data_read_write module
data_read_write = SourceFileLoader("data_read_write", current_file_path + "/data_read_write.py").load_module()

