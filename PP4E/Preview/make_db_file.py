# -*- coding:utf-8 -*-
"""
eg. 1-2
Save the data in memory to diskfile using customized format;
Suppose that the data do not use 'endrec.', 'enddb.' or '=>';
Suppose the database is double used dict; WARNING: use eval will execute the string as command;
Also you can use eval() to creat an dict record one by one;
You can use dbfile.write(key + '\n') instead of print(key, file=dbfile)
"""

dbfilename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename=dbfilename):
    "Format and save the datebase to diskfile"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    "Anaysis the data and restruct the database"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)

