# eg. 1-11

from initdata import bob, sue
import shelve

with shelve.open('people-shelve') as db:
    db['bob'] = bob
    db['sue'] = sue
