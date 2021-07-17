#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

################################################################ 
#  Fetch data from isbndb.com  database via API
################################################################ 
#  - Make sure to install requests module first: 
#      pip3 install requests
#  - Have an api key registered and use it below
################################################################

import requests as req
 
h = {'Authorization': '46371_6aa121b5f9277e57e23d4f2e9857c72a'}
isbn = "9781934759486"

url = f"https://api2.isbndb.com/book/{isbn}"
resp = req.get(url, headers=h)
print(resp.json())

