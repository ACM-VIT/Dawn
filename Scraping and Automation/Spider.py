import requests
from bs4 import BeautifulSoup

def king_spider():
    
    
    url='https://pure-inlet-32646.herokuapp.com/posts'
    results = requests.get(url)
    prometheus = results.text
    soup= BeautifulSoup(prometheus, "lxml")
    for title in soup.find_all('h4'):
        print(title)

king_spider()