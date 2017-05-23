#!/usr/bin/python
# This Python file uses the following encoding: utf-8
import os, sys
import MySQLdb
hostname = 'localhost'
username = '#'
password = '#'
database = '#'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT team_name, home FROM TABLE3" )

    for team_name, home in cur.fetchall() :
        print team_name, home


print "Using MySQLdb…"

myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()

# print "Using pymysql…"
# import pymysql
# myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
# myConnection.close()

# print "Using mysql.connector…"
# import mysql.connector
# myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
# doQuery( myConnection )
# myConnection.close()
