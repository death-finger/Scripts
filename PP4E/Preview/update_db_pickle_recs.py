# eg. 1-10

import pickle

with open('sue.pkl', 'rb') as suefile:
    sue = pickle.load(suefile)

sue['pay'] *= 1.10

with open('sue.pkl', 'wb') as suefile:
    pickle.dump(sue, suefile)

