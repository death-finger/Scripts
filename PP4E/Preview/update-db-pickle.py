"""
eg. 1-7
"""

import pickle

with open('people-pickle', 'rb') as dbfile:
    db = pickle.load(dbfile)

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Pickle'

with open('people-pickle', 'wb') as dbfile:
    pickle.dump(db, dbfile)

