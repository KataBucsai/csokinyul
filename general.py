# Here will be the general function
import ui
import sys


# @option_list a list of string
def choose(option_list):
    inputs = ui.get_inputs(["Please chose an options"], "")
    option = inputs[0]
    for i, opts in enumerate(option_list):
        if option == str(i+1):
            opts
    if option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")