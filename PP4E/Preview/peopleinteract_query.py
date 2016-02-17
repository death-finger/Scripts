# eg. 1-21
# interactive queries

import shelve

fieldnames = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldnames)

with shelve.open('class-shelve') as db:
    while True:
        key = input('\nKey? => ')
        if not key: break
        try:
            record = db[key]
        except:
            print('No such key "%s"!' % key)
        else:
            for field in fieldnames:
                print(field.ljust(maxfield), '=>', getattr(record, field))
