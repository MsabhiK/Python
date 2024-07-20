class BankAccount:
    accounts = []
    def __init__(self, rate, balance):
        self.rate=rate
        self.balance=balance
        BankAccount.accounts.append(self)


        #instance method
    def deposite(self, amount):
        self.balance +=amount
        return self
        
    def withdraw(self, amount):
        if amount > self.balance:
            print('-'*20)
            print(f"Insufficient funds: Charging a $5 fee!!!")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
        

    def display_account_info(self):
        print('-'*50)
        print(f"Your Balance: {self.balance} $\nRate: { self.rate }")
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
    
class User:
    users = []
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.account = BankAccount(rate=0.05, balance=0)

    def make_deposite(self, amount):
        self.account.deposite(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def make_yield_interest(self):
        self.account.yield_interest()
        return self 

    def display_user_balance(self):
        self.account.display_account_info()
        return self 
    
    def display_user_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Balance: ${self.account.balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposite(amount)
        return self
    
    @classmethod
    def all_users_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for user in cls.users:
            sum += user.account.balance
        return sum
    
#USER TEST
user_karim = User("Karim MSABHI", "sirmsabhi@gmail.com")
user_karim.make_deposite(450).make_withdraw(200).make_yield_interest().display_user_info().display_user_balance()        

user_hela = User("Hela MSABHI", "helamsabhi@gmail.com")
user_hela.make_deposite(1500).display_user_info().transfer_money(user_karim, 250).display_user_balance()
user_karim.display_user_info()
#print(BankAccount.all_users_balances())
print(BankAccount.all_balances())
    
