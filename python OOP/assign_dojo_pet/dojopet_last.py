class Ninjaa:
    def __init__(self, nom, prenom, treats, pet_food, pet):
        self.nom=nom
        self.prenom=prenom
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self




