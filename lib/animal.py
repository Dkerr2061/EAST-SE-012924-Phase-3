import ipdb

class Animal():

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

        Animal.all.append(self)

    def make_animal_sound(self):
        print("Animal Sound")

    

class Dog(Animal):

    all = []

    def __init__(self, name, age, obidience_level, bark_volume= 3 ):
        super().__init__(name, age)
        self.obidience_level = obidience_level
        self.bark_volume =bark_volume

        Dog.all.append(self)

    def make_animal_sound(self):
        print(f"Bark{'!' * self.bark_volume}")
       

class Cat(Animal):

    all = []

    def __init__(self, name, age):
        super().__init__(name, age)

        Cat.all.append(self)

    def make_animal_sound(self):
        print("Meow!")
    