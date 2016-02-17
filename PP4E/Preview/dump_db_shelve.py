# eg. 1-12

import shelve

with shelve.open('people-shelve') as db:
    for key in db:
        print(key, '=>\n ', db[key])
    print(db['sue']['name'])

