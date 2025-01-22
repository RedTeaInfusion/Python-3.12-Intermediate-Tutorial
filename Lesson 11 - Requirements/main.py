'''
Lesson 11 - Requirements
freeze
requirements.txt
requests
beautifulsoup4
'''
import os
from datetime  import datetime
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        html = soup.prettify()
        text = soup.get_text(separator='\n', strip=True)
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return {'html': html, 'text': text, 'links': links}
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return None

def save_to_files(data):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    folder_name = f'scraped_data_{timestamp}'
    os.makedirs(folder_name)
    with open(os.path.join(folder_name, 'file.html'), 'w', encoding='utf-8') as file:
        file.write(data['html'])
    with open(os.path.join(folder_name, 'text.txt'), 'w', encoding='utf-8') as file:
        file.write(data['text'])
    with open(os.path.join(folder_name, 'links.txt'), 'w', encoding='utf-8') as file:
        file.write('\n'.join(data['links']))

def main():
    url = ''
    scraped_data = scrape_website(url)
    if scraped_data:
        save_to_files(scraped_data)

if __name__ == '__main__':
    main()