import glob
import time

class SourceFileWatcher:
    def __init__(self):
        print("Program purpose: This module watches for any new file in the source directory")
    def fn_filewatcher(self,CONNECTION_INFO,POLL_COUNT_NUMBER,POLL_INTERVAL_MINUTES,DF_NAME):
        print(CONNECTION_INFO,POLL_COUNT_NUMBER,DF_NAME)
        v_dff=[]
        for v_iteration_count in range(0, int(POLL_COUNT_NUMBER)):
            print ("Iteration %d: looking for %s/%s") % (v_iteration_count, CONNECTION_INFO, DF_NAME)
            v_dff = glob.glob (CONNECTION_INFO + '/' + DF_NAME)
            if v_dff:
                print ("found file: ", v_dff)
                break
            else:
                print ("file not found, sleeping for %d seconds" % POLL_INTERVAL_MINUTES)
            time.sleep (POLL_INTERVAL_MINUTES)
        return v_dff
