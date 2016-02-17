import pickle, glob
for filename in glob.glob('*.pkl'):
    with open(filename, 'rb') as recfile:
        record = pickle.load(recfile)
        print(filename, '=>\n ', record)

with open('sue.pkl', 'rb') as suefile:
    print(pickle.load(suefile)['name'])
