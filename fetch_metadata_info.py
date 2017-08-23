import os
import subprocess
from create_db_connection import CreateDbConnection
from execute_dml_query import ExecuteDmlQuery
#import logging framework goes here
class FetchMetadataInfo:
    def __init__(self):
        print("Program purpose: Fetch the information from metadata tables")
    def fn_fetch_metadata_info(self,inp_query_name):
        try:
            v_connection_obj = CreateDbConnection()
            v_connection = v_connection_obj.fn_connect_to_db()
            v_sql_query = u"select query from df_query where name = :inp_bind_value"
            v_execute_query_obj = ExecuteDmlQuery()
            v_execute_query_result = v_execute_query_obj.fn_fire_query_master(v_connection,v_sql_query,inp_query_name)
            v_sql_query = str(v_execute_query_result)
            v_execute_query_result = v_execute_query_obj.fn_fire_query_slave(v_connection,v_sql_query,1,'Y')
            v_query_result_dict = dict()
            if len(v_execute_query_result)>0:#atleast 1 row is returned
                for i in range(len(v_execute_query_result[0])):
                    v_query_result_dict[v_execute_query_result[0][i]] = v_execute_query_result[1][i]
            for i in v_query_result_dict:
                print(i,v_query_result_dict[i])
            return v_query_result_dict
        except Exception as error:
            print("Error in program. Unable to execute the section")
            raise