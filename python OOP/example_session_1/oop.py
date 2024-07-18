class Car:
    # class attributes
    number_of_cars = 0
    cars = []

    # ! class constructor
    # ? instance method
    def __init__(self, color, hp, model):
        # ? instance attribute
        self.color=color
        self.hp=hp
        self.model=model
        Car.number_of_cars += 1
        Car.cars.append(self)   # pour stocker chaque objet crée du car

    # instance method
    def display_info(self):
        print('-'*100)
        print (f"Car_Color: {self.color}\nCar_HP: {self.hp}\nCar_Model: {self.model}")

    # class Method
    @classmethod
    def get_total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")
    
    @classmethod
    def reset_cars(cls):
        cls.number_of_cars = 0

    #Static Method
    @staticmethod
    def hp_comment(hp):
        if hp < 30:
            print("It's slow car")
        elif hp < 50:
            print("It's medium car")
        else: print("It's excellent car")



car_1 = Car("Orange", 25, "POLO")
car_2 = Car("Blue", 45, "Mercedes")
car_3 = Car("White", 75, "BMW")
#car_1.display_info()

#car_2.display_info()
#car_3.display_info()
for car in Car.cars:       #to display all cars
    car.display_info()
    car.hp_comment(car.hp)

Car.get_total_cars()

#print(car_1.color, car_1.hp, car_1.model)
#print(f"Number of cars: {Car.number_of_cars}")
Car.reset_cars()
print(f"Number of cars after reset: {Car.number_of_cars}")
# print (f"Car_Color: {car_1.color}\nCar_HP: {car_1.hp}\nCar_Model: {car_1.model}")

#Car.hp_comment(55)