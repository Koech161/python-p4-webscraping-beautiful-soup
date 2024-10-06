# from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')
# print(doc.select('.column-highlights.pt-sm.pb-sm.bg-white'))
courses = doc.select('.column-highlights.pt-sm.pb-sm.bg-white')[0].attrs

# for course in courses:
print(courses)