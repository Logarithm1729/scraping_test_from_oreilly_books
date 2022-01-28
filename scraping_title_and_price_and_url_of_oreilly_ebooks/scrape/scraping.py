from bs4 import BeautifulSoup
import csv
import os
import requests
from urllib.parse import urljoin

def fetch(url):
    return requests.get(url).text

def scrape(html, base_url):
    books = []
    soup = BeautifulSoup(html, 'html.parser')

    for book_info in soup.select('#bookTable > tbody > tr'):
        #get price
        price = book_info.select('td[class="price"]')[0].text

        title_url_el = book_info.select('td[class="title"] > a')[0]
        
        #get url and title
        url = urljoin(base_url, title_url_el.get('href'))
        title = title_url_el.text

        books.append({'title': title, 'price': price, 'url': url})
    return books


def save_to_csv(save_path, data, header=['title', 'price', 'url']):
    with open(save_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, header)
        writer.writeheader()
        writer.writerows(data)
