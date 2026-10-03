class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"ฝาก {amount}")
        else:
            print("Error")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"ถอนเงิน {amount} บาท เรียบร้อย")
        else:
            print("ยอดเงินไม่เพียงพอหรือจำนวนเงินไม่ถูกต้อง")
    def get_balance(self):
        return f"คงเหลือ {self.__balance}"
    
account = BankAccount("Alice")
account.deposit(1000)
account.withdraw(500)
# print(account.get_balance())