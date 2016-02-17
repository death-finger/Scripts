# eg. 1-22
# interactive update

import shelve
from person import Person
fieldnames = ('name','age','job','pay')
maxfield = max(len(x) for x in fieldnames)

with shelve.open('class-shelve') as db:
    while True:
        key = None
        key = input('\nInput the key you want to search: ')
        if key == 'exit': break
        if key in db:
            modify = None
            record = db[key]
            for field in fieldnames:
                print(field.ljust(maxfield), ' => ', getattr(record, field))
            modify = input('\nDo you want to change the record?(Y/N): ')
        else:
            addnew = None
            addnew = input('\n"%s" not exist, add new?(Y/N)' % key)
        try:
            if modify == 'Y':
                for field in fieldnames:
                    currval = getattr(record, field)
                    newtext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
                    if newtext:
                        setattr(record, field, eval(newtext))
                db[key] = record
        except NameError:
            pass
        try:
            if addnew == 'Y':
                for field in fieldnames:
                    newtext = input('\t[%s]= ' % field)
                    setattr(record, field, eval(newtext))
                db[key] = record
        except NameError:
            pass


