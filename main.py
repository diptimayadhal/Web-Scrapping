#Flipkart website scrapping
import requests

#get the HTML
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/search?q=boat&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
response=requests.get(url)
htmlcontent= response.content
# print(htmlcontent)

# Parse the HTML
soup=BeautifulSoup(htmlcontent, 'html.parser')
# print(soup)
# print(soup.prettify())

# HTML Tree Traversal
titles=[]
prices=[]
image_urls=[]
for d in soup.find_all('div',attrs={'class':'_13oc-S'}):
#  print(d)
  title=d.find('a',attrs={'class':'s1Q9rs'})
  print(title.string)
  price=d.find('div',attrs={'class':'_30jeq3'})
  print(price.string)
  images=d.find('img',attrs={'_396cs4 _3exPp9'})
  print(images.get('src'))

titles.append(title.string)
prices.append(price.string)
image_urls.append(images.get('src'))

