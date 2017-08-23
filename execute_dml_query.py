import os
import subprocess
import cx_Oracle
#import logging framework goes here
class ExecuteDmlQuery:
    def __init__(self):
        print("Program purpose: Executing the sql query being called")
    def fn_fire_query_master(self,inp_db_connection,inp_dml_stmt,inp_bind_value):
        try:
            #Creating the cursor object
            v_connection = inp_db_connection
            v_cursor = v_connection.cursor()
            if inp_bind_value:
                v_cursor.execute(inp_dml_stmt,inp_bind_value=inp_bind_value)
            else:
                v_cursor.execute(inp_sql_stmt)
            v_rows_fetched = v_cursor.fetchall()
            for i in v_rows_fetched:
                v_sql_result = str(i[0])
            return v_sql_result
            #Exception handling
        except Exception as ex:
            print("Fetch error. Description:{0}")
            raise
        finally:
            v_cursor.close()
    def fn_fire_query_slave(self,inp_db_connection,inp_dml_stmt,inp_bind_value,inp_column_required_flag=None):
        try:
            print inp_dml_stmt
            print inp_db_connection
            print inp_bind_value
            print inp_column_required_flag
            #Creating the cursor object
            v_connection = inp_db_connection
            v_cursor = v_connection.cursor()
            if inp_bind_value:
                v_cursor.execute(inp_dml_stmt,inp_bind_value=inp_bind_value)
            else:
                v_cursor.execute(inp_sql_stmt)
            #Initializing the result set to store the values fetched
            v_ddl_result = list()
            #Initializing the array size for the cursor
            v_cursor.arraysize = 10000
            #Fetching the dataset
            while True:
                v_rows_fetched = v_cursor.fetchmany()
                if v_rows_fetched == []:
                    break;#this means no more rows to return now
                v_ddl_result = v_ddl_result + v_rows_fetched
            #Fetching the column names from the table
            v_column_names = tuple([i[0] for i in v_cursor.description])
            v_column_list = [v_column_names]
            #Check for inp_column_required_flag to take decision if to append the column names with the result set list
            if inp_column_required_flag == 'Y':
                return v_column_list + v_ddl_result
            else:
                return v_ddl_result
            #Exception handling
        except Exception as ex:
            print("Fetch error. Description:{0}")
            raise
        finally:
            v_cursor.close()