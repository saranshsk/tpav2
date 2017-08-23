import os
import subprocess
import cx_Oracle
#import logging framework goes here
class CreateDbConnection:
    def __init__(self):
        print("Program purpose: Create database connection")
    def fn_connect_to_db(self):
        try:
            connection = cx_Oracle.connect( 'metadata/METADATA@orcl' )
            return connection
        except cx_Oracle.DatabaseError as dberror:
            error,=dberror.args
            if error.code==1017:
                print("Credentials are wrong")
            else:
                print("Database connection error. Description:{0}".format(dberror))
            raise