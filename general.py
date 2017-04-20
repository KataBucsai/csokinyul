# Here will be the general function
import os
import sys
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))


# return the max length of the longest element from every column
#
# @table: list of list
def get_table_elements_length(table):
    colum_max_lens = []
    for i in range(len(table[0])):
        colum_max_lens.append(len(max(table, key=lambda x: len(x[i]))[i]))
    return colum_max_lens
