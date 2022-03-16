import requests
from bs4 import BeautifulSoup

# Get the HTML
url= "https://www.amazon.it/dp/1022369"
r=requests.get(url)
htmlContent = r.content

# Parse the HTML
soup=BeautifulSoup(htmlContent, 'html.parser')

# HTML Tree traversal
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1015"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/000004458x"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/000004458x"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1002198"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1002198"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1002791"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1002864"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1003704"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1003704"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1002864"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1003704"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1003704"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1003763"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1003763"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1004271"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1017519"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1017519"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1022369"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1034677"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1032666"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.dp/dp/1032666"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1034936"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1034936"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1034944"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1034944"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1034677"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1035002"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1035029"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1035053"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1035053"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1036866"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1037137"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1039466"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1039466"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1037944"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1037944"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1040871"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1040871"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1041002"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1041002"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1041991"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1041991"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1043331"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1013331"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1048325"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1048325"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1049119"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.de/dp/1049119"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
url= "https://www.amazon.fr/dp/1057812"
r=requests.get(url)
htmlContent = r.content
soup=BeautifulSoup(htmlContent, 'html.parser')
title=soup.title
print(title)
image_url=soup.find_all('img')
print(image_url)
price=soup.price
print(price)
details=soup.details
print(details)
print()
