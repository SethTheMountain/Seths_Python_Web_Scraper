import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Benjamin_Franklin')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.string)

links = soup.find_all('a')
for link in links:
  print(link.get('href'))