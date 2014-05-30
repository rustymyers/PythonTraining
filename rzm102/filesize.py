#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- filesize.py
#--------------------------------------------------------------------------------------------------
# Program    : filesize.py
# To Complie : n/a
#
# Purpose    : accept arguments from CLI and print out size of file, print error for DIR
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
import os

number_of_arguments = len(sys.argv)
if number_of_arguments < 2:
    print("Provide the files to search as arguments")
    quit()
number_of_files_to_search = len(sys.argv) - 1
files_to_search = sys.argv[1:]
#print "{0} = {1}".format(number_of_files_to_search,files_to_search)
for files in files_to_search:
    if os.path.isfile(files):
        print files," = ",os.path.getsize(files),"bytes"
    elif os.path.isdir(files):
        print "Error. {0} is not a file.".format(files)