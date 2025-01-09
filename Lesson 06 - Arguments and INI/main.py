'''
Lesson 06 - Arguments and INI
configparser
string
sys.argv
'''
import configparser
import random
import string
import sys

CONFIG_FILE = 'config.ini'

def read_config_option():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    settings = {section: dict(config.items(section)) for section in config.sections()}
    return settings

def generate_password(length, uppercase, digits, special):
    character = string.ascii_lowercase
    if uppercase:
        character += string.ascii_uppercase
    if digits:
        character += string.digits
    if special:
        character += string.punctuation
    return ''.join(random.choice(character) for _ in range(int(length)))

def main():
    if len(sys.argv) == 5:
        password = generate_password(
            int(sys.argv[1]),
            bool(sys.argv[2]),
            bool(sys.argv[3]),
            bool(sys.argv[4]),
        )
    else:
        settings = read_config_option()
        password = generate_password(
            settings['Length']['password_length'],
            settings['CharTypes']['uppercase'],
            settings['CharTypes']['digits'],
            settings['CharTypes']['special'],
        )
    print(f'Generated password: {password}')

if __name__ == '__main__':
    main()