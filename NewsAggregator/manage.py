import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.mediapart.fr/')

#converts html into a searchable object
soup = BeautifulSoup(response.content, 'html.parser')

#formats the html nicely for an easier reading
#print(soup.prettify())

#Pour avoir les headlines
s = soup.find('div', class_= 'block _headlines _intertwine-headlines')

for i in s.find_all('a'):
    print(i.text.strip())
