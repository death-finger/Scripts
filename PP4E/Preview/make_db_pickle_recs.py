# eg. 1-8

from initdata import bob, sue, tom
import pickle
for (key, record) in [('bob', bob), ('sue', sue), ('tom', tom)]:
    with open(key + '.pkl', 'wb') as recfile:
        pickle.dump(record, recfile)
