#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- president_sort.py
#--------------------------------------------------------------------------------------------------
# Program    : president_sort.py
# To Complie : n/a
#
# Purpose    : print presidents fname,lname,state,birth sorted by 
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
#           2014-05-29 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

import operator

presidents = []

with open("presidents.txt","r+") as pres_txt:
    for line in pres_txt:
        presidents.append(line[:-1].split(":"))

# Print Fname, lname, Bstate.
for president in sorted(presidents,key=operator.itemgetter(1,2)):
    print("{0}, {1} - Home State: {2}".format(president[1],president[2],president[10]))

# Pres#:LastName:FirstMiddle:BY:BM:BD:DY:DM:DD:BirthTown:BirthState:SOY:SOM:SOD:EOY:EOM:EOD:Party
# 40:Reagan:Ronald Wilson:1911:Feb:06:2004:Jun:05:Tampico:Illinois:1981:Jan:20:1989:Jan:20:Republican
