import requests 
from bs4 import BeautifulSoup



url = "https://books.toscrape.com/" # A site made for scraping practice

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    book_title = soup.find_all('h3')

    print("found book tites: ")

    for title in book_title:
        print(title.find('a')['title'])

except requests.exceptions.RequestException as e:
    print(e)