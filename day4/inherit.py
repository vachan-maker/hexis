class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # constructor self similar to this
    def speak(self):
        print(f'{self.name} says hello!')
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!!")
dog = Dog('Rex',3)
dog.speak()