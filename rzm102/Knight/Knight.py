#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- Knight.py
#--------------------------------------------------------------------------------------------------
# Program    : Knight.py
# To Complie : n/a
#
# Purpose    : Knight class for creating objects name,title,fav color,quest,comment
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

class UnknownKnightError(Exception):
    pass

class Knight:
    def __init__(self,name):
        self._name = name
        K = None
        try:
            K = open('../knights.txt')
            found = False
            for line in K:
                (name,title,color,quest,cmt) = line[:-1].split(":")
                if name == self._name:
                    self._title = title
                    self._color = color
                    self._quest = quest
                    self._comment = cmt
                    found = True
                    break
            if not found:
                raise UnknownKnightError("No such knight as '" + self._name + "'")   
        except IOError,e:
            print "ERROR!",e
        finally:
            if K:
                K.close()
    @property
    def Name(self):
        return self._name
            
    @property
    def Title(self):
        return self._title
            
    @property
    def FavoriteColor(self):
        return self._color
            
    @property
    def Quest(self):
        return self._quest
            
    @property
    def Comment(self):
        return self._comment

    def get_color(self,name):
        
if __name__ == '__main__':
    k = Knight('Arthur')
    print k.get_color