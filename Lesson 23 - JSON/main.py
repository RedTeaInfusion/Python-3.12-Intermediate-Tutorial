import json
import requests

def create_article(url, title, content, author_id=1):
    r = requests.post(url, json={"title": title, "body": content, "userId": author_id})
    return r.json()

def read_articles(url):
    r = requests.get(url)
    return r.json()[:1] if r.ok else []

def update_article(url, article_id, title, content):
    r = requests.put(f"{url}/{article_id}", json={"id": article_id, "title": title, "body": content, "userId": 1})
    return r.json()

def delete_article(url, article_id):
    r = requests.delete(f"{url}/{article_id}")
    return r.status_code == 200

def write_json_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def read_json_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def main():
    user_1 = {
        "id": 1,
        "name": "Red",
        "is_student": True,
        "courses": ["Python", "Science"]
    }
    write_json_to_file(user_1, 'user.json')
    user_2 = {
        "id": 2,
        "name": "Bob",
        "is_student": False,
        "courses": ["Python", "History"]
    }
    users = [user_1, user_2]
    write_json_to_file(users, 'users.json')

    config = read_json_from_file('config.json')
    print(type(config), config)

    print(f'POST: {create_article(config['url'], 'News', 'JSON')}')
    print(f'GET: {read_articles(config['url'])}')
    print(f'PUT: {update_article(config['url'], 1, 'New Title', 'New Content')}')
    print(f'DELETE: {delete_article(config['url'], 1)}')

if __name__ == '__main__':
    main()