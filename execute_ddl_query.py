import os
import subprocess
import cx_Oracle
#import logging framework goes here

class ExecuteDdlQuery:
    def __init__(self):
        print("Executing the ddl query being called")

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