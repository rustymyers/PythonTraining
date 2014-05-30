#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- pyfind.py
#--------------------------------------------------------------------------------------------------
# Program    : pyfind.py
# To Complie : n/a
#
# Purpose    : Take first argument as pattern and remiaining arguemnts are files. Search files and
#               print lines
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
#           2014-05-30 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

import sys
import re

number_of_arguments = len(sys.argv)
if number_of_arguments <= 1:
    print("Provide the word to search as the first argument and the files to search as the next arguments")
    quit()
elif number_of_arguments <=2:
    print("Provide the files to search as the final arguments")
    quit()
word_to_find = sys.argv[1]

r = re.compile(word_to_find)

number_of_files_to_search = len(sys.argv) - 2
files_to_search = sys.argv[2:]
# print("Files to search: ",files_to_search)

# For each file, print each line with a number
for file_name in files_to_search:
    print "Searching File {0} for pattern {1}".format(file_name,word_to_find)
    with open(file_name,"r+") as open_file:
        for line in open_file:
            if r.search(line):
                print line,
                