class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Current Balance: {self.__balance}")

    def __display_balance(self):
        print(f"Current Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance, (int, float)) and balance >= 0:
            self.__balance = balance
            print(f"Balance updated to {self.__balance}.")
        else:
            print("Invalid balance. Balance must be a non-negative number.")

account = BankAccount("123456789", 500.0)
account.deposit(150.0)
account.withdraw(200.0)
account.set_balance(-50.0)
account.display_account_info()