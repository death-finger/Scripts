# -*- coding:utf-8 -*-
"""
eg. 1-1
Initiate the data which saves into file, pickle and shelve
"""

# Record data
bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}
tom = {'name':'Tom', 'age':50, 'pay':0, 'job':None}

# Database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom


# Run as scripts
if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])

