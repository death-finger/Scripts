#e.g. 17-2

import sys
if input('Are you sure?')[0] not in ('y', 'Y'):
    print('Operation Cancelled!')
    sys.exit()

dbname = sys.argv[1] if len(sys.argv) > 1 else 'dbase1'
table = sys.argv[2] if len(sys.argv) > 2 else 'people'

from loaddb import login
conn, curs = login(dbname)
curs.execute('delete from ' + table)
print(curs.rowcount, 'records deleted')
conn.commit()
