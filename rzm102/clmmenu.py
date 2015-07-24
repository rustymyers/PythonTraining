#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- clmmenu.py
#--------------------------------------------------------------------------------------------------
# Program    : clmmenu.py
# To Complie : n/a
#
# Purpose    : Download CLMMenu 
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



import urllib2 as url

clmmenu = url.urlopen("https://clc.its.psu.edu/SystemBuildWS/CLMMenu.aspx?Platform=M&OU=Mac%20Labs%202012%2d2013")
print clmmenu.info()

for line in clmmenu:
    print line,
    
clmmenu.close()