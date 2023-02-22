class Chicken():
    def __init__(self, name, x=0.0, y=65.0, z=0.0):
        self.name = name
        self.eggs_laid = 0
        self.max_health = 100
        self.health = self.max_health
        self.has_eaten = False
        self.location = [x, y, z]

    def cluck(self):
        if self.isalive():
            print(f"{self.name} says 'cluck cluck cluck.'")
        else:
            print(f"{self.name} is very quiet.")

    def eat(self):
        if self.isalive():
            print(f"{self.name} pecks at the food.")
            self.heal(25)
            self.has_eaten = True
        else:
            print(f"I don't think that {self.name} is hungry anymore...")

    def get_location(self):
        return self.location

    def get_name(self):
        return self.name

    def heal(self, hp):
        if self.isalive(): # there are no Zombie Chickens in this mod
            self.health += hp
            if self.health > self.max_health:
                self.health = self.max_health

    def isalive(self):
        return self.health > 0

    def lay_an_egg(self):
        if not self.isalive():
            return
        self.eggs_laid += 1
        if self.eggs_laid == 1:
            print(f"{self.name} just laid her first egg. Congratulations!")
        elif self.eggs_laid == 3:
            print(f"You can make an omelete with this many eggs (maybe don't tell {self.name})")
        elif self.eggs_laid == 12:
            print(f"That's a dozen eggs!  Good work, {self.name}!")
        elif self.eggs_laid == 13:
            print(f"A baker's dozen!")
        elif self.eggs_laid == 18:
            print(f"{self.name}, we're gonna need a bigger carton.")
        elif self.eggs_laid == 60:
            print(f"Five dozen eggs! Somebody get {self.name} a blue ribbon!")
        elif self.eggs_laid == 72:
            print(f"That'll do for now, {self.name}.")
        elif self.eggs_laid == 108:
            print(f"Seriously, knock it off, {self.name}.")
        else:
            print(f"{self.name} just laid another egg.")
        return self.eggs_laid  # for now, an Egg is simply an integer

    def lay_some_eggs(self, eggCount):
        if eggCount <= 0: return
        eggs = []
        for _ in range(eggCount):
            eggs.append(self.lay_an_egg())
        return eggs

    def poop(self):
        if self.isalive() and self.has_eaten:
            print(f"{self.name} just practiced Python Object Oriented Programming!")
            print(f"You probably need to clean up after {self.name}.") 
            self.has_eaten = False

    def take_damage(self, hp):
        if self.isalive():
            self.health -= hp
            self.cluck()

    def wander(self):
        if self.isalive():
            print(f"{self.name} just wandered a bit.")
        else:
            print(f"{self.name} isn't going anywhere.")

