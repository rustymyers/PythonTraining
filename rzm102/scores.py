#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- scores.py
#--------------------------------------------------------------------------------------------------
# Program    : scores.py
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


import sys

students_scores = {}
score_sum = 0
num_score = 0

with open("testscores.dat") as f:
    for line in f:
        (name,test_score) = line[:-1].split(":")
        students_scores[name] = int(test_score)
        score_sum += int(test_score)
        num_score += 1

for name,score in students_scores.iteritems():
    grade = None
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    #print name,score,grade
    print("{0:<20s} | {1:<} = {2:}".format(name,score,grade))
print("")
print("Average Score: {0:.2f}".format(float(score_sum)/num_score))    