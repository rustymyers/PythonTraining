#!/usr/local/bin/python
#--------------------------------------------------------------------------------------------------
#-- sysmanClass
#--------------------------------------------------------------------------------------------------
# Program    : sysmanClass
# To Complie : n/a
#
# Purpose    : # Check LDAP for users names
#               "/usr/bin/ldapsearch -o nettimeout=10 -l 60 -z 100 -LLL -H ldap://dirapps.aset.psu.edu -b dc=psu,dc=edu -x '(&(sn=*MYERS*)(cn=*RUSSELL*))'",,,
#               Return psAdminArea
#               Return psCampus
#
# Called By  :
# Calls      :
#
# Author     : Rusty Myers <rzm102@psu.edu>
# Based Upon : http://everythingisgray.com/2014/06/01/complex-ldap-queries-with-ldapsearch-and-python-ldap
#
# Note       : 
#
# Revisions  : 
#           2015-07-24 <rzm102>   Initial Version
#
# Version    : 1.0
#--------------------------------------------------------------------------------------------------

import os
import csv
import ldap
import sys

LDAP_URI = 'ldap://dirapps.aset.psu.edu'
SEARCH_BASE = 'dc=psu,dc=edu'
QUERY = ""
RESULTS = []

def ldap_search(ldap_uri, base, query):
    '''
    Perform an LDAP query.
    '''
    psAdminArea = []
    psCampus = []
    emails = []
    try:
        l = ldap.initialize(ldap_uri)
        l.protocol_version = ldap.VERSION3
    
        search_scope = ldap.SCOPE_SUBTREE
        retrieve_attributes = None
    
        ldap_result_id = l.search(
            base,
            search_scope,
            query,
            retrieve_attributes
        )
        result_set = []
        while 1:
            result_type, result_data = l.result(ldap_result_id, 0)
            if (result_data == []):
                break
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
    
        if len(result_set) == 0:
            print('No results found. Remove the header line and try again.')
            return

        emailcount = 0
        for i in range(len(result_set)):
            for entry in result_set[i]:
                try:
                    email = entry[1]['mail'][0]
                    emailcount += 1
                    emails.append(email)
                except:
                    pass    
        psAdminAreacount = 0
        for i in range(len(result_set)):
            for entry in result_set[i]:
                try:
                    psAdminArea = entry[1]['psAdminArea'][0]
                    psAdminAreacount += 1
                    psAdminArea.append(psAdminArea)
                except:
                    pass
        psCampuscount = 0
        for i in range(len(result_set)):
            for entry in result_set[i]:
                try:
                    psCampus = entry[1]['psCampus'][0]
                    psCampuscount += 1
                    psAdminArea.append(psCampus)
                except:
                    pass
    
    except ldap.LDAPError, e:
        print('LDAPError: %s.' % e)
    
    finally:
        l.unbind_s()
        # print("Admin Area: " + psAdminArea)
        # print("Campus: " + psCampus)
        # print("Email: " + email)
        print("{0},{1},'{2}','{3}',{4}").format(fName,lName,email,psAdminArea,psCampus)
        inputData = fName,lName,email,psAdminArea,psCampus
        RESULTS.append(inputData)

# def main():
#     ldap_search(LDAP_URI, SEARCH_BASE, QUERY)
# 
# 
# if __name__ == '__main__':
#     sys.exit(main())


# Open our File, Later turn this into a web text box
with open('ClassList.csv', 'rU') as classList:
    csvData = csv.reader(classList, dialect=csv.excel_tab)
    for row in csvData:
        name = row[0].split(",")
        fName = name[1].split(' ', 1)[0]
        lName = name[0]
        print( "Name: " + fName + " " + lName)
        QUERY = "(&(sn=*" + name[0] + "*)(cn=*" + name[1].split(' ', 1)[0] + "*))"
        ldap_search(LDAP_URI, SEARCH_BASE, QUERY)
        print ""
classList.closed

# Write our results to a csv file
with open('ClassListUpdated.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'email', 'area', 'campus']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for p in RESULTS: 
        writer.writerow({'first_name': p[0], 'last_name': p[1], 'email': p[2], 'area': p[3], 'campus': p[4]})
csvfile.closed
