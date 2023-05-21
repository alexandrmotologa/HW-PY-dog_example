class Dog:
    def __init__(self, name, race, year, alive):
        self.name = name
        self.race = race
        self.year = year
        self.alive = alive
    
    def printDog(self):
        print(self.name)
        print(self.race)
        print(self.year)
        print(self.alive)


my_dog = Dog("Tuzik", "BullDog", 2010, True)
my_dog.printDog()