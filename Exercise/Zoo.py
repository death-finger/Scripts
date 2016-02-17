class Animal:
    def reply(self):
        print(self.speak)

class Mammal(Animal): pass

class Cat(Mammal):
    def __init__(self):
        self.speak = 'meow'
