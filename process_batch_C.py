"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv

input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"

# Create a file object for input (r = read access)
input_file = open(input_file_name, "r")

# Create a file object for output (w = write access)
# On Windows, without newline='', 
# we'll get an extra line after each record
output_file = open(output_file_name, "w", newline='')

# Create a csv reader for a comma delimited file
reader = csv.reader(input_file, delimiter=",")

# Create a csv writer for a comma delimited file
writer = csv.writer(output_file, delimiter=",")

# Our file has a header row, move to next to get to data
header = next(reader)

# Write the header row to the output file
header_list = ["Year","Month","Day","Time","TempC"]
writer.writerow(header_list)

# Then, for each data row in the reader
for row in reader:

    # set local variables for each column in the row
    # note: the order of the columns is important
    #       and must match the order in the input file
    # We really only care about the temperature column
    Year, Month, Day, Time, TempK = row

    # convert the temperature from K to F
    # use the built-in round() function to round to 2 decimal places
    # use the built-in float() function to 
    # convert the string (as read) 
    # to a float (a floating point number) or decimal
    TempF = round(1.8 * (float(TempK) - 273.0) + 32.0)

    # put the values in a list (see the square brackets)
    # and write the list of values to the output file
    writer.writerow([Year, Month, Day, Time, TempF])

# close the file objects to release the resources
# this is important
# if not closed from this process, 
# you may not be able to move or delete the file 
output_file.close()
input_file.close()