import random


class Animal:
    def __init__(self, name, size, food_type, habitat, lifespan):
        self.name = name
        self.size = size
        self.food_type = food_type
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = 0
        self.satiety = random.randint(50, 100)
        self.gender = random.choice(['male', 'female'])


class Ecosystem:
    def __init__(self):
        self.animals = []
        self.possible_animals = [
            Animal("Lion", 3, "Carnivore", "Land", 20),
            Animal("Elephant", 4, "Herbivore", "Land", 50),
            Animal("Tiger", 3, "Carnivore", "Land", 15),
            Animal("Giraffe", 5, "Herbivore", "Land", 25),
            Animal("Zebra", 2, "Herbivore", "Land", 25),
            Animal("Bear", 3, "Carnivore", "Land", 30),
            Animal("Wolf", 2, "Carnivore", "Land", 12),
            Animal("Hippo", 3, "Herbivore", "Water", 40),
            Animal("Eagle", 2, "Carnivore", "Land", 30),
            Animal("Snake", 2, "Carnivore", "Land", 15),
            Animal("Fox", 1, "Carnivore", "Land", 10),
            Animal("Kangaroo", 2, "Herbivore", "Land", 20),
            Animal("Falcon", 2, "Carnivore", "Air", 20),
            Animal("Parrot", 1, "Herbivore", "Air", 50),
            Animal("Bat", 1, "Carnivore", "Air", 15)
        ]
        self.plant_food = 1000

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            print("Error: It is not an animal.")
            return

        if animal not in self.possible_animals:
            print(f"Cannot add {animal.name}. There are no animals of this kind on the planet.")
            return
        self.animals.append(animal)

    def increase_plant_food(self, amount):
        self.plant_food += amount

    def display_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Age: {animal.age}, Satiety: {animal.satiety}%, Gender: {animal.gender}")

    def reproduce(self, animal1, animal2):
        if animal1.name == animal2.name and animal1.gender != animal2.gender:
            if animal1.habitat == "Water" and animal1.satiety > 50 and animal2.satiety > 50:
                for i in range(10):
                    self.add_animal(
                        Animal(animal1.name, animal1.size, animal1.food_type, animal1.habitat, animal1.lifespan))
            elif animal1.habitat == "Air" and animal1.satiety > 42 and animal2.satiety > 42 and animal1.age > 3 and animal2.age > 3:
                for i in range(4):
                    self.add_animal(
                        Animal(animal1.name, animal1.size, animal1.food_type, animal1.habitat, animal1.lifespan))
            elif animal1.habitat == "Land" and animal1.satiety > 20 and animal2.satiety > 20 and animal1.age > 5 and animal2.age > 5:
                for i in range(2):
                    self.add_animal(
                        Animal(animal1.name, animal1.size, animal1.food_type, animal1.habitat, animal1.lifespan))

    def feed_animal(self, animal):
        if animal.food_type == "Plant":
            if self.plant_food > 0:
                self.plant_food -= 1
                animal.satiety += 26
            else:
                animal.satiety -= 9
        elif animal.food_type == "Carnivore":
            if random.random() < 0.5:
                prey = random.choice(self.animals)
                if prey.name != animal.name:
                    animal.satiety += 53
                    self.animals.remove(prey)
                else:
                    animal.satiety -= 16
            else:
                animal.satiety -= 9

    def time_step(self):
        for animal in self.animals:
            animal.age += 1
            animal.feed_animal(animal)

            if animal.satiety < 10:
                self.plant_food += animal.size
                self.animals.remove(animal)


ecosystem = Ecosystem()
while True:
    print("\n=== Menu ===")
    print("1. Add new animal")
    print("2. Display current animals")
    print("3. Feed animals")
    print("4. Reproduce animals")
    print("5. Simulate time step")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAdding a new animal:")
        name = input("Enter animal name: ")
        size = int(input("Enter animal size (1-5): "))  # Assuming size is a number
        food_type = input("Enter animal food type (Carnivore/Herbivore): ")
        habitat = input("Enter animal habitat: ")
        lifespan = int(input("Enter animal lifespan: "))

        try:
            animal = Animal(name, size, food_type, habitat, lifespan)
            ecosystem.add_animal(animal)
            print(f"{animal.name} added to the ecosystem.")
        except (TypeError, ValueError):
            print(f"Error adding animal")

    elif choice == "2":
        print("\nCurrent animals in the ecosystem:")
        ecosystem.display_animals()

    elif choice == "3":
        print("\nFeeding animals")
        ecosystem.time_step()
        print("Animals have been fed.")

    elif choice == "4":
        print("\nReproducing animals:")
        animal1 = random.choice(ecosystem.animals)
        animal2 = random.choice(ecosystem.animals)
        ecosystem.reproduce(animal1, animal2)
        print("Animals have reproduced.")

    elif choice == "5":
        print("\nSimulating time step:")
        ecosystem.time_step()
        print("Time step simulated.")

    elif choice == "0":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a valid option (0-5).")
