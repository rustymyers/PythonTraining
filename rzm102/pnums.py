#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- pnums.py
#--------------------------------------------------------------------------------------------------
# Program    : pnums.py
# To Complie : n/a
#
# Purpose    : Print all lines in custinfo.dat that contain phone numbers
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

r_pnum = re.compile(r"\b([0-9]{3}[-]){1,2}([0-9]{4})\b")

with open("custinfo.dat","Ur") as cust_dat:
    for line in cust_dat:
        if r_pnum.search(line):
            print line