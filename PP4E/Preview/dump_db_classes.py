import shelve

with shelve.open('class-shelve') as db:
    for key in db:
        print(key, '=>\n ', db[key])