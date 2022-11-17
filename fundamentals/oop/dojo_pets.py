class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self,):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print(self.noise)

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

my_treats = ['bacon', 'peanut butter', 'bone']
my_pet_food = ['kibble', 'rice', 'chicken']

dolly = Pet('Dolly', 'dog', ['boop', 'shake', 'sit'], 'rawr')

sara = Ninja('Sara', 'Lee', dolly, my_treats, my_pet_food)

sara.feed()
sara.walk()
sara.bathe()