class Pet:
    def __init__(self, name, type, tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.healthy=100
        self.energy=100

    def sleep(self):
        self.energy +=25
        return self
    
    def eat(self):
        self.healthy +=10
        self.energy +=5
        return self
    
    def play(self):
        self.healthy +=5
        return self
    
    def noise(self):
        if self.type=="DOG":
            print("🐶 OUF OUF")
        elif self.type=="CAT":
            print("🐱 Meaou meaou")
        else:
            print("Mou mou")

class Dog(Pet):
    def __init(self, name, type, tricks):
        super().__init__(name, "DOG", tricks)

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, "CAT", tricks)

class Lion(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, "LION", tricks)
