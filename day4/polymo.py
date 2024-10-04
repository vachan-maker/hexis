class Cat:
    def speak(self):
        return "meow"
class Dog:
    def speak(self):
        return "woof!"
def animal_sound(animal):
    return animal.speak()

cat=Cat()
dog = Dog()

print(animal_sound(cat))
print(animal_sound(dog))
