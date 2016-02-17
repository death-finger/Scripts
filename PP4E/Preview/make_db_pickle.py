"""
eg. 1-5
"""

from initdata import db
import pickle
"""
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
"""

with open('people-pickle', 'wb') as dbfile:
    pickle.dump(db, dbfile)

