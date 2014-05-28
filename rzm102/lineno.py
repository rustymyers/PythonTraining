#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- lineno.py
#--------------------------------------------------------------------------------------------------
# Program    : lineno.py
# To Complie : n/a
#
# Purpose    : display each line of a file preceded by line number. Process multiple files from CLI.
#
# Called By  :
# Calls      :
#
# Author     : Rusty Myers <rzm102@psu.edu>
# Based Upon :
#
# Note       : 
#
# Revisions  : 
#           2014-05-28 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------


import sys

# Make sure we've got a file to read
if len(sys.argv) == 1:
    print("Please provide a text file argument.")
    quit(0)

# Find out how many files we've got
number_o_files = len(sys.argv) - 1
print("You have provided {0} argument(s)".format(number_o_files))

# Create list of files passed
files_provided = enumerate(sys.argv[1:])

# For each file, print each line with a number
for file_name in files_provided:
    # Create counter starting at one
    line_count = 1
    print("Processing {0}".format(file_name[1]))
    open_file = open(file_name[1])
    for line in open_file:
        print("{0}  {1}".format(line_count,line)),
        line_count += 1
    open_file.close()
    print("")
