import pet
import dojopet_last

rumi = pet.Pet("Rumi", "CAT", "Jumping")
ninja_1 = dojopet_last.Ninjaa("Patric", "Bruel", "fisher", "cake", rumi)
pet_2 = pet.Lion("Dragon", "LION", "Jumping")
ninja_2 = dojopet_last.Ninjaa("Patric", "Bruel", "fisher", "cake", pet_2)

if __name__ == "__main__":
    ninja_1.walk().feed().bathe()
    print(f"HEALTH: {ninja_1.pet.healthy}")
    print(f"ENERGY: {ninja_1.pet.energy}")
    print(f"2/****Name's Pet_2: {pet_2.name}")
    ninja_2.walk().walk().feed().feed().bathe()
    print(f"HEALTH: {ninja_2.pet.healthy}")
    print(f"ENERGY: {ninja_2.pet.energy}")

else:
    print("ERREUR")