#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- shellusers.py
#--------------------------------------------------------------------------------------------------
# Program    : shellusers.py
# To Complie : n/a
#
# Purpose    : 
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

users_dict = {}
counts = {}

with open("passwd","Ur") as f:
    for line in f:
        (username,password,uid,gid,full_name,home,shell) = line[:-1].split(":")
        if shell == "":
            shell = "NONE"
        users_dict[username] = [password,uid,gid,full_name,home,shell]

for name,info_list in users_dict.iteritems():
    shell = info_list[5]
    counts[shell] = counts.get(shell,0) + 1

for shell,count in counts.iteritems():
    print("{0:<15}    {1:>}".format(shell,count))