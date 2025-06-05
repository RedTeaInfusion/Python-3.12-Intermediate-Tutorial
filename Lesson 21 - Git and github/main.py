import os
import csv
import configparser
from datetime import datetime
import requests

def get_settings(path='config.ini'):
    config = configparser.ConfigParser()
    config.read(path)
    return config['settings']

def get_joke(url):
    try:
        return requests.get(url, timeout=5).json().get('joke')
    except Exception as e:
        return f'Error: {e}'

def save_jokes(filename, count, url):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            writer.writerow(['Timestamp', 'Joke'])
        for _ in range(count):
            writer.writerow([datetime.now().isoformat(timespec='seconds'), get_joke(url)])
        
def main():
    url = 'https://v2.jokeapi.dev/joke/Programming?type=single'
    settings = get_settings()
    save_jokes(settings.get('filename', 'jokes.csv'),
               int(settings.get('count', 1)),
               url)

if __name__ == '__main__':
    main()