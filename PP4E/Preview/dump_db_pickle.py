#!/usr/bin/env python3

import pickle
dbfile = open('people-pickle', 'rb') # use binary mode files in 3.X
db = pickle.load(dbfile)
for key in db:
    print(key, '=> ', db[key])

"print(db['sue']['name'])"