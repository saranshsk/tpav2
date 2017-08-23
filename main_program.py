import os
import subprocess
from fetch_metadata_info import FetchMetadataInfo
from source_file_watcher import SourceFileWatcher
#import logging framework goes here
class MainProgram:
    def __init__(self):
        print("Program purpose: Main method that is calling all the other classes")
def main():
    try:
        #Fetch data from df_inp table
        v_fetch_df_inp_metadata_obj = FetchMetadataInfo()
        v_fetch_df_inp_metadata = v_fetch_df_inp_metadata_obj.fn_fetch_metadata_info('df_inp')
        print(v_fetch_df_inp_metadata)
        #Fetch data from df_inp_validation and df_validation table
        v_fetch_df_inp_validation_metadata_obj = FetchMetadataInfo()
        v_fetch_df_inp_validation_metadata = v_fetch_df_inp_validation_metadata_obj.fn_fetch_metadata_info('df_validation')
        print(v_fetch_df_inp_validation_metadata)
        #Start to watch file availability
        v_source_file_watcher_obj = SourceFileWatcher()
        v_source_file_watcher = v_source_file_watcher_obj.fn_filewatcher(v_fetch_df_inp_metadata['CONNECTION_INFO'],v_fetch_df_inp_metadata['POLL_COUNT_NUMBER'],v_fetch_df_inp_metadata['POLL_INTERVAL_MINUTES'],v_fetch_df_inp_metadata['DF_NAME'])
        
    except Exception as error:
        print("Error in program. Unable to execute the section")
        raise
if __name__=='__main__':
    main()