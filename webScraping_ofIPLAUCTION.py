import requests
from bs4  import BeautifulSoup
import pandas as pd


url="https://www.iplt20.com/auction/2022"


# request ot the url
r= requests.get(url)
# print(r)


#get text from the url using the beautiful soup
soup=BeautifulSoup(r.text,"lxml")
# print(soup)


#data of table fetch
table=soup.find("table",class_="ih-td-tab auction-tbl")
#print(table)


# then fetch the header  data
title=table.find_all("th") 
# print(title)

header=[]


# then fetch the data of title..
for i in title:
    name=i.text
    header.append(name)

# print(header)

df=pd.DataFrame(columns=header)
# print(df)

# then fetch the data from tr tag
rows=table.find_all("tr")
# print(rows)


#then find the rows from  using loop after index
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div",class_="ih-pt-ic").text.strip()
    data= i.find_all("td")[1:]
    row =[tr.text for tr in data]
    #print(row)
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row


print(df)
    # print(data)

df.to_excel("ipl Auction stats.xlsx")
df.to_csv("ipl Auction stats.txt")