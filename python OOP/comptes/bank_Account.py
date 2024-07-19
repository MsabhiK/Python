class BankAccount:
    accounts = []
    def __init__(self, name, rate, balance):
        self.name=name
        self.rate=rate
        self.balance=balance
        BankAccount.accounts.append(self)


        #instance method
    def deposit(self, amount):
        self.balance +=amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('-'*20)
            print(f"Insufficient funds:{self.name}  Charging a $5 fee!!!")
            self.balance -= 5
        return self
        

    def display_account_info(self):
        print('-'*50)
        print(f"Account:{self.name}\nBalance: {self.balance} $\nRate: { self.rate }")
        return self
        
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.rate)
        return self
        
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.accounts:
            sum += account.balance
        return sum

        
balance_1 = BankAccount("Karim", 0.12, 526)
balance_2 = BankAccount("Hela", 0.12, 254)
balance_3 = BankAccount("Lobna", 0.15, 100)

balance_1.deposit(100).deposit(150).deposit(300).withdraw(250).yield_interest().display_account_info()

balance_2.deposit(300).deposit(120).withdraw(200).withdraw(380).withdraw(80).withdraw(120).yield_interest().display_account_info()

print(f"SUM of All balances of accounts is: {BankAccount.all_balances()} $")



    
