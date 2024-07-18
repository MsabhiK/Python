class User_oop:
    is_rewards_member=False
    gold_card_points = 0
    users = []

    def __init__(self, first_name, last_name, email, age, is_rewards_member, gold):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member = False
        self.gold_card_points = 0
        User_oop.users.append(self)
        

    #instance method
    def display_info(self):
        print('-'*50)
        print(f"FULL NAME: {self.first_name} {self.last_name}\nEmail: {self.email}\nÂge: {self.age}\nIs_reward_member: {self.is_rewards_member}\nGold_card_points: {self.gold_card_points} points")
        return self

    #instance method
    def enroll(self):
        if self.is_rewards_member:
            print(f"{self.first_name} {self.last_name} is already a member")
            return self
        else:
            self.is_rewards_member=True
            self.gold_card_points += 200
            print(f"Mrs {self.first_name} {self.last_name} enrolled")
            return self
            

    #instance method
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"Mrs {self.first_name} {self.last_name} spent {amount} points and actually has {self.gold_card_points} points")
            return self
        else:
            print(f"Mrs {self.first_name} {self.last_name} does not have enough points to spend {amount} points")
            return self


user_1 = User_oop("Karim", "MSABHI", "sirmsabhi@gmail.com", 42, False, 0)
user_2 = User_oop("Lobna", "CHOUCHENE", "sirmsabhi@gmail.com", 35, False, 0)
user_3 = User_oop("Hela", "MSABHI", "sirmsabhi@gmail.com", 32, False, 0)

#for u in User_oop.users:
#    u.display_info()

user_1.display_info().enroll().spend_points(50).display_info()
print("\n-----------------------------------------------\n")
user_2.enroll().spend_points(80).display_info()
print("\n-----------------------------------------------\n")
user_3.enroll().spend_points(40).display_info()


    

