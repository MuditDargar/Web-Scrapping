import requests
from bs4 import BeautifulSoup

url="https://www.geeksforgeeks.org/"
req=requests.get(url)

soup =BeautifulSoup(req.content,"html.parser")

res =soup.title
print(res.prettify()) # by this you find the title of url

# print(soup.get_text()) # by this you find the text of the url

# print(soup.prettify()) # by this you find the html ,script of the url