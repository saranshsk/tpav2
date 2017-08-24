from subprocess import Popen, PIPE
import cx_Oracle
import csv
import sys
from source_file_watcher import SourceFileWatcher
#import logging framework goes here
class SourceToStageLoad():
    def __init__(self):
        print("Program purpose: This module reads the CIF file and inserts the same into the database")
    def fn_insert_data_to_stage(self,dff_path,DFF_FILE_DELIM):
        try:
            print(dff_path)
            print(DFF_FILE_DELIM)
            column_string=""
            values_string=""
            insert_query_1=""
            var=","
            lines=[]
            i=0
            print("test1")
            DFF_FILE_DELIM=DFF_FILE_DELIM.rstrip()
            validation_cmd = "awk -F'<INP_DELIM>' '{print NF;exit}' <INP>"
            print(validation_cmd)
            validation_cmd = validation_cmd.replace('<INP>', dff_path)
            validation_cmd = validation_cmd.replace('<INP_DELIM>', DFF_FILE_DELIM)
            print(validation_cmd)
            print("Executing the above command for extracting the column count from the file")
            p = Popen ( validation_cmd, shell = True, stdout = PIPE, stderr = PIPE )
            validation_cmd_result, err = p.communicate()
            print("Execution return code: ", p.returncode)
            print(validation_cmd_result.rstrip(), err.rstrip())
            if p.returncode == 0:
                column_count = int(validation_cmd_result.rstrip())
                print
                for x in range(1, column_count+1):
                    if x < column_count:
                        column_string = column_string+'c'+str(x)+','
                        values_string = values_string+':'+str(x)+','
                    if  x==column_count:
                        column_string = column_string+'c'+str(x)
                        values_string = values_string+':'+str(x)
            insert_query_1 = "insert into table1 (" + column_string + ") values ( " + values_string +")"
            csv.field_size_limit(sys.maxsize)
            with open(dff_path) as datafile:
                    reader = csv.reader(datafile)
                    for row in reader:
                            if(i  > 100000):
                                print("Chunks of records are being inserted into the database")
                                repo_db_conn = cx_Oracle.connect ( 'metadata/METADATA@orcl' )
                                cur=repo_db_conn.cursor()
                                cur.executemany(insert_query_1,lines)
                                repo_db_conn.commit()
                                lines=[]
                                cur.close()
                                lines=[]
                                i=0
                                lines.append(row)
                            else:
                                i +=1
                                lines.append(row)
            print("Remaining records are being inserted into the database")
            repo_db_conn = cx_Oracle.connect ( 'metadata/METADATA@orcl' )
            cur=repo_db_conn.cursor()
            cur.executemany(insert_query_1,lines)
            repo_db_conn.commit()
            lines=[]
            cur.close()
        except Exception as error:
            print("Error in program. Unable to execute the section")
            raise
