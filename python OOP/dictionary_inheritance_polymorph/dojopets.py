class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    #walk
    def walk(self):
        self.pet.play()
        return self

    #feed()
    def feed(self):
        self.pet.eat()
        return self

    #bather()
    def bathe(self):
        self.pet.noise()
        return self     
    


class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        
    #sleep()
    def sleep(self):
        self.energy += 25

    #eat()
    def eat(self):
        self.health += 10
        self.energy -= 5

    #play()
    def play(self):
        self.health +=5

    #noise()
    def noise(self):
        if self.type=="dog":
            print("ouf ouf")
        if self.type=="cat":
            print("meow meow")
        else:
            print("mou")

luna = Pet("Luna", "cat", "jumping")
joe = Ninja("Joe", "Doe", "Bacon", "Pizza", luna)
joe.feed()
joe.walk()
joe.bathe()
print(joe.pet.health)