class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful! New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful! New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount!")

account = BankAccount("123-456-789", 1000)

print(f"Account Number: {account.get_account_number()}")

print(f"Initial Balance: {account.get_balance()}")

account.deposit(500)

account.withdraw(300)

account.withdraw(2000)

print(f"Final Balance: {account.get_balance()}")