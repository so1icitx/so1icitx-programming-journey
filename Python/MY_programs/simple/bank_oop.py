class Account:
    def __init__(self, acc_num, balance, holder_name):
        self.account_num = acc_num
        self.balance = balance
        self.holder_name = holder_name

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.holder_name} deposited {amount} in the bank , total balance: {self.balance}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{self.holder_name} withdrew {amount} from the bank total balance: {self.balance}')
        else:
            raise Exception("not enough balance to withdraw!")




Steve = Account(1, 1000, 'Steve')
Steve.withdraw(100)
Chang = Account(2, 1610, 'Chang')
Chang.deposit(390)
