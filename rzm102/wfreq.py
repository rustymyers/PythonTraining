#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- wfreq.py
#--------------------------------------------------------------------------------------------------
# Program    : wfreq.py
# To Complie : n/a
#
# Purpose    : read a text file and print out a list of all words in file, lower case & number 
#                of times occurred
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

import re
import sys

r = re.compile(r"[^\w']+")

number_of_arguments = len(sys.argv)
if number_of_arguments <= 1:
    print("Provide the files to search")
    quit()
number_of_files_to_search = len(sys.argv) - 1
files_to_search = sys.argv[1:]
print(files_to_search)
for a_file in files_to_search:
    with open(a_file,"r") as open_file:
        word_list = {}
        for line in open_file:
            words = r.split(line)
            for x in words:
                if x == "": continue
                if x == "'": continue
                x = x.lower()
                if x in word_list:
                    word_list[x] += 1
                else:
                    word_list[x] = 1            
        words = word_list.keys()
        for w in sorted(words,key=word_list.__getitem__):
            print "{0:<16s} {1:4d}".format(w,word_list[w])