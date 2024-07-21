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
        #self.account = BankAccount(rate=0.05, balance=0)
        self.accounts = {}

    def open_new_account(self, rate=0.05, balance=0, account_name="Checking"):
        #Make a bank account instance
        new_account = BankAccount(rate, balance)
        print(f"Saving new account: {new_account.balance}")
        #add that instance to the account dictionary
        self.accounts[account_name] = new_account
        return self
    def make_deposite(self, amount, account_name):
        self.accounts[account_name].deposite(amount)
        return self

    def make_withdraw(self, amount, account_name):
        self.accounts[account_name].withdraw(amount)
        return self

    def make_yield_interest(self, account_name):
        self.accounts[account_name].yield_interest()
        return self 

    def display_user_balance(self, account_name):
        self.accounts[account_name].display_account_info()
        return self 
    
    def display_user_info(self, account_name):
        print('-'*50)
        print(f"Name: {self.name}, Email: {self.email}, Balance: ${self.accounts[account_name].balance}")
        return self
    
    def transfer_money(self, from_account, to_account, other_user, amount):
        if from_account == to_account and other_user == to_account and amount == 0:
            print("Transfering 0$ between accounts is not allowed.")
            return self
        if self.accounts[from_account].balance < amount:
            print('-'*20)
            print(f"Insufficient funds: Charging a $5 fee!!!")
            self.accounts[from_account].balance -= 5
            return self
        self.accounts[from_account].withdraw(amount)
        other_user.accounts[to_account].deposite(amount)
        return self
    
    @classmethod
    def all_users_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for user in cls.users:
            sum += user.account.balance
        return sum
    
    

karim = User("Karim MSABHI", "sirmsabhi@gmail.com")
karim.open_new_account(0.05, 0, "Checking")
karim.make_deposite(100, "Checking").display_user_info("Checking")
karim.open_new_account(0.05, 300, "Saving").display_user_balance("Saving")
#user_karim.make_deposite(450).make_withdraw(200).make_yield_interest().display_user_info().display_user_balance()        

hela = User("Hela MSABHI", "helamsabhi@gmail.com")
hela.open_new_account(0.05, 300, "Saving").display_user_info("Saving").display_user_balance("Saving") 
karim.transfer_money('Checking', 'Checking', hela, 50).display_user_info('Checking')
hela.display_user_info('Checking')
#user_karim.display_user_info()
#print(BankAccount.all_users_balances())
#print(BankAccount.all_balances())
    
