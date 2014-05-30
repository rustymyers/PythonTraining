#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- badger.py
#--------------------------------------------------------------------------------------------------
# Program    : badger.py
# To Complie : n/a
#
# Purpose    : Convert all of the occurrences of"rabbit" with "badger" in alice30.txt
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
r = re.compile(r"\brabbit\b",re.I)

with open("alice30.txt","r") as open_file:
        for line in open_file:
            if r.search(line.lower()):
                with open("badger.txt","a") as badger:
                    badger.write(r.sub("badger",line))
                    #print r.sub("badger",line)
                #print line
            else:
                with open("badger.txt","a") as badger:
                    badger.write(line)
                    #print line,