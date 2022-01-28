from black import main
from scraping import fetch, scrape, save_to_csv


SCRAPE_TARGET_URL = 'https://www.oreilly.co.jp/ebook/'
OUTPUT_CSV_PATH = 'output/output.csv'
BASE_URL = 'https://www.oreilly.co.jp/'

def main():
    html = fetch(SCRAPE_TARGET_URL)
    book_info = scrape(html, BASE_URL)
    save_to_csv(OUTPUT_CSV_PATH, book_info)
    print('Done')

if __name__ == '__main__':
    main()