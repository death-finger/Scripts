# -*- coding:utf-8 -*-
"""
eg. 1-3
"""

from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])

