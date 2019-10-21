#!/usr/bin/python3
import requests

"""
script for voting for my id via http requests
"""
for i in range(1024):
    pay = dict(id="712", holdthedoor="Submit+Query")
    r = requests.post('http://158.69.76.135/level0.php', pay)
    print(r)

print("done")
