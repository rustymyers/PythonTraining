#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- hello.py
#--------------------------------------------------------------------------------------------------
# Program    : hello.py
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
#           2014-07-02 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------


import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)
label = QLabel("Hello World")
label.show()
app.exec_()
sys.exit()
