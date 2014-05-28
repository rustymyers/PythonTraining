#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- countalice.py
#--------------------------------------------------------------------------------------------------
# Program    : countalice.py
# To Complie : n/a
#
# Purpose    : count number of lines in alice30.txt that contain Alice. (Should be 392).
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

number_of_arguments = len(sys.argv)
if number_of_arguments <= 1:
    print("Provide the word to search as the first argument and the files to search as the next arguments")
    quit()
elif number_of_arguments <=2:
    print("Provide the files to search as the final arguments")
    quit()
word_to_find = sys.argv[1]
number_of_files_to_search = len(sys.argv) - 2
files_to_search = sys.argv[2:]
print(files_to_search)
for a_file in files_to_search:
    open_file = open(a_file,"r")
    line_counter = 0
    for lines in open_file:
        if lines.find(word_to_find) >= 0:
            line_counter += 1
    open_file.close()
    print("{1} is found on {0} lines".format(line_counter,word_to_find))