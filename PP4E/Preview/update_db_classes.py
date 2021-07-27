#!/usr/bin/env python3

import shelve

from initdata import tom
db = shelve.open('class-shelve')

sue = db['sue']         # fetch sue
sue.giveRaise(.25)      # change
db['sue'] = sue         # update sue

tom = db['tom']         # fetch tom
tom.giveRaise(.20)      # change
db['tom'] = tom         # update tom

db.close()