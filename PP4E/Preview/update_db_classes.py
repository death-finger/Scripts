import shelve

with shelve.open('class-shelve') as db:
    sue = db['sue']
    sue.giveRaise(.25)
    db['sue'] = sue
    tom = db['tom']
    tom.giveRaise(.2)
    db['tom'] = tom
