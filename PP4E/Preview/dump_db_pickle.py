"""
eg. 1-6
"""

import pickle

with open('people-pickle', 'rb') as dbfile:
    db = pickle.load(dbfile)
    for key in db:
        print(key, '=>\n ', db[key])
    print(db['sue']['name'])
