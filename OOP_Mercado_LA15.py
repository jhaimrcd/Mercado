class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Bark!"

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Meow!"

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Chirp!"

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."
    
def animal_sounds(animal):
    print(f"{animal.name} says: {animal.speak()}")

dog = Dog("Blacky")
cat = Cat("Garfield")
bird = Bird("Tweety")
fish = Fish("Nemo")

animals = [dog, cat, bird, fish]

for animal in animals:
    animal_sounds(animal)