import requests # this is use for request to webpage to get data
from bs4 import BeautifulSoup # this isuse for scrapping

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
# print(r)


# print the text in lxml format
soup=BeautifulSoup(r.text ,"lxml")
# print(soup.prettify())


# fetch the data of a particular class and for a particular tag
boxes=soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
# print(len(boxes))


# by this you fetch the data of the all a tag with class title 
#by this you get the all name of the tablets
names=soup.find_all("a",class_="title")


#print all the name of the tablets using for loop 
# for i in names:
#     print(i.text)


# for this you fetch the data of prices
prices=soup.find_all("h4",class_="pull-right price")

# after fetching the data you print the prices
for i in prices:
    print(i.text)