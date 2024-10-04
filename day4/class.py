class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # constructor self similar to this
    def speak(self):
        print(f'{self.name} says hello!')
cat = Animal('cat',4)
dog = Animal('dog',5)
print(cat.name)
print(cat.age)

cat.speak()
dog.speak()