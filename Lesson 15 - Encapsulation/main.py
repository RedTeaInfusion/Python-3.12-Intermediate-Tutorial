'''
Lesson 15 - Encapsulation
encapsulation
public
protected
private
'''
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._account_type = 'Standard'
        self.__balance = initial_balance
        self.__pin = None

    def get_balance(self, pin):
        if self._verify_pin(pin):
            return self.__balance
        
    def get_account_info(self, pin):
        if self._verify_pin(pin):
            return self._account_type
        
    def set_pin(self, new_pin):
        if self.__validate_pin(new_pin):
            self.__pin = new_pin

    def _verify_pin(self, pin):
        return self.__pin is not None and self.__pin == pin

    def __validate_pin(self, pin):
        return isinstance(pin, int) and len(str(pin)) == 4

class SavingsAccount(BankAccount):
    def get_account_info_from_subclass(self, pin):
        if self._verify_pin(pin):
            return self._account_type

account = BankAccount('Alice', 1000)
account.set_pin(1111)
print(f'Public attribute: {account.account_holder}')
print(f'Protected attribute: {account.get_account_info(1111)}')
print(f'Private attribute: {account.get_balance(1111)}')

sub_account = SavingsAccount('Bob', 1200)
sub_account.set_pin(2222)
print(f'Public attribute: {sub_account.account_holder}')
print(f'Protected attribute: {sub_account.get_account_info_from_subclass(2222)}')
print(f'Private attribute: {sub_account.get_balance(2222)}')
