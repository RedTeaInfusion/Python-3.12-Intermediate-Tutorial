'''
Lesson 22 - Logging
logging
RotatingFileHandler
info
error
warning
'''
import os
import logging
from logging.handlers import RotatingFileHandler

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        logging.info(f'Account for {owner} created with ${balance}')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            logging.info(f'{self.owner} deposited ${amount} (Balance: ${self.balance})')
        elif amount == 0:
            logging.warning(f'Deposit must be bigger than 0')
        else:
            logging.error(f'Deposit can\'t be negative')
    
    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount
        elif amount <= 0:
            logging.warning(f'Withdraw must be greater than 0')
        elif amount > self.balance:
            logging.error(f'You can\'t withdraw ${amount}')

def setup_logging(log_file, log_dir='logs'):
    log_path = os.path.join(log_dir, log_file)
    os.makedirs(log_dir, exist_ok=True)
    handler = RotatingFileHandler(
        log_path,
        maxBytes=512,
        backupCount=3
    )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

def main():
    setup_logging('bank.log')
    acc = BankAccount('Bob', 100)
    acc.deposit(40)
    acc.withdraw(20)
    acc.withdraw(150)
    acc.deposit(-10)
    
if __name__ == '__main__':
    main()