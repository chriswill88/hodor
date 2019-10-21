#!/usr/bin/python3
from lxml import html
from bs4 import BeautifulSoup
import requests

"""
script for voting for my id via http requests
and webscraping with beautiful soup
run script and see id update live @ http://158.69.76.135/level1.php
"""

s = requests.session()
# tree = html.fromstring(page.content)
for i in range(4096):
    page = s.get('http://158.69.76.135/level1.php')
    soup = BeautifulSoup(page.content, 'lxml')
    lucky = soup.find_all('input')[2].get('value')
    print(lucky)
    pay = dict(id="712", holdthedoor="Submit+Query", key=lucky)
    r = s.post('http://158.69.76.135/level1.php', pay)
    print(r)
# print("done!")
# print(r.headers)
# value = tree.xpath("//input[@value]").extract()
# key = value.xpath("[@name='key']")
# print(value)

print("done")
