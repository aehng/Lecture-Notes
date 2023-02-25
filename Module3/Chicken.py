class Chicken():
    MAX_HEALTH = 100
    def __init__(self, name, x=0.0, y=65.0, z=0.0):
        self.__name = name
        self.__eggs_laid = 0
        self.__health = self.MAX_HEALTH
        self.__has_eaten = False
        self.__location = [x, y, z]

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 20:
            self.__name = name

    def cluck(self):
        if self.isalive():
            print(f"{self.__name} says 'cluck cluck cluck.'")
        else:
            print(f"{self.__name} is very quiet.")

    def eat(self):
        if self.isalive():
            print(f"{self.__name} pecks at the food.")
            self.heal(25)
            self.__has_eaten = True
        else:
            print(f"I don't think that {self.__name} is hungry anymore...")

    def isalive(self):
        return self.__health > 0

    def lay_an_egg(self):
        if not self.isalive():
            return
        self.__eggs_laid += 1
        if self.__eggs_laid == 1:
            print(f"{self.__name} just laid her first egg. Congratulations!")
        elif self.__eggs_laid == 12:
            print(f"That's a dozen eggs!  Good work, {self.__name}!")
        elif self.__eggs_laid == 13:
            print(f"A baker's dozen!")
        elif self.__eggs_laid == 18:
            print(f"{self.__name}, we're gonna need a bigger carton.")
        elif self.__eggs_laid == 60:
            print(f"That'll do for now, {self.__name}.")
        elif self.__eggs_laid == 72:
            print(f"Seriously, knock it off, {self.__name}.")
        else:
            print(f"{self.__name} just laid another egg.")
        return Egg(self.__eggs_laid)

    def lay_some_eggs(self, eggCount):
        if eggCount <= 0:
            return
        return [self.lay_an_egg() for _ in range(eggCount) ]

    def poop(self):
        if self.isalive() and self.__has_eaten:
            print(f"{self.__name} just practiced Python Object Oriented Programming!")
            self.__has_eaten = False

    def take_damage(self, hp):
        if self.isalive():
            self.__health -= hp
            self.cluck()
        else:
            print("It's dead, Jim")

    def wander(self):
        if self.isalive():
            print(f"{self.__name} just wandered a bit.")
        else:
            print(f"{self.__name} isn't going anywhere.")



class Egg:
    def __init__(self, id):
        self.__id = id



class Coop:
    def __init__(self, id):
        self.__id = id
        self.__idx = 0
        self.__chickens = []

    def get_id(self):
        return self.__id

    def add_chicken(self, chicken):
        self.__chickens.append(chicken)

    def remove_chicken(self, chicken_id):
        return self.__chickens.pop(chicken_id)

    def get_chicken(self, chicken_id):
        return self.__chickens[chicken_id]

    # These two dunders enable Coops to work in `for` loops, like this:
    #   for chicken in coop:
    def __iter__(self):
        self.__idx = 0
        return self

    def __next__(self):
        if self.__idx >= len(self.__chickens):
            raise StopIteration
        c = self.__chickens[self.__idx]
        self.__idx += 1
        return c


class Farmer:
    def __init__(self, name):
        self.name = name
        self.__coops = []
        self.__eggs = []

    def add_coop(self, coop):
        self.__coops.append(coop)

    def remove_coop(self, coop_id):
        return self.__coops.pop(coop_id)

    def harvest_eggs(self):
        batch = []
        for coop in self.__coops:
            for chicken in coop:
                egg = chicken.lay_an_egg()
                if egg is not None:
                    batch.append(egg)
        print(f"Farmer {self.name} harvested {len(batch)} more eggs")
        self.__eggs.extend(batch)
        print(f"That makes {len(self.__eggs)} eggs all together!")
        
    def sell_eggs(self):
        print(f"Farmer {self.name} sold {len(self.__eggs)} eggs at the market")
        self.__eggs.clear()


if __name__ == '__main__':
    lucy = Chicken('Lucy')
    aubrey = Chicken('Aubrey')
    rachel = Chicken('Rachel')

    coop1 = Coop(1)
    coop1.add_chicken(lucy)
    coop1.add_chicken(aubrey)

    coop2 = Coop(2)
    coop2.add_chicken(rachel)

    chet = Farmer("Chet")
    chet.add_coop(coop1)
    chet.add_coop(coop2)

    chet.harvest_eggs()
    chet.harvest_eggs()
    chet.sell_eggs()
