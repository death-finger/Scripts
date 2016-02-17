# eg. 1-13

from initdata import tom
import shelve

with shelve.open('people-shelve') as db:
    sue = db['sue']
    sue['pay'] *= 1.10
    db['sue'] = sue
    db['tom'] = tom
