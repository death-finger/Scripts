# e.g. 17-11

import sys
if input('Are you sure?')[0] not in ('y', 'Y'):
    print('Operation Cancelled!')
    sys.exit()

dbname = len(sys.argv) > 1 and sys.argv[1] or 'dbase1'
table =  len(sys.argv) > 2 and sys.argv[2] or 'people'

from loaddb import login
conn, curs = login(dbname)
try:
    curs.execute('drop table ' + table)
except:
    print('Error while dropping table ' + table + ': file not exist or in use!')

command = 'create table %s (name char(30), job char(10), pay int(4))' % table

curs.execute(command)
conn.commit()
print('made', dbname, table)
