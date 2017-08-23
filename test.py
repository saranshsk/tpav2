import time
import cx_Oracle

con = cx_Oracle.connect( 'metadata/METADATA@orcl' )

start = time.time()

cur = con.cursor()
cur.arraysize = 100000
cur.execute('select * from table1 where rownum <10')
res = cur.fetchall()
print res  # uncomment to display the query results

#elapsed = (time.time() - start)
#print elapsed, " seconds"

cur.close()
con.close()
