#!/usr/bin/env python3

# web crawling, get data from a website (intro Real Pyhton basics)
import requests

resp = requests.get("https://realpython.com")
html = resp.text
print(html[159:247])
