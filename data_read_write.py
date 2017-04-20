import csv
import os.path
main_path = os.path.dirname(os.path.abspath(__file__))


# read file into a @table
#
# @file_name: string
# @table: list of lists of strings
def get_datatable_from_file(file_name):
    try:
        filerout = (main_path + '/' + file_name)
        if os.stat(filerout).st_size > 0:
            datatable = []
            with open(filerout, 'r') as datafile:
                datafile_reader = csv.reader(datafile, delimiter=';', skipinitialspace=True, lineterminator='\n')
                for row in datafile_reader:
                    datatable.append(row)
            return datatable
        else:
            print("Empty file")
            return None
    except OSError:
        return 1


# write a @table into a file
#
# @file_name: string
# @table: list of lists of strings
def write_datatable_to_file(file_name, datatable):
    try:
        with open((main_path + '/' + file_name), 'w') as csvfile:
            datafile_writer = csv.writer(csvfile, delimiter=';', skipinitialspace=True, lineterminator='\n')
            datafile_writer.writerow([line for line in datatable])
            print("write is done")
    except:
        print("Something")