class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says: woof!"
    


dog1 = Dog("adi",22)

print(dog1.name)
print(dog1.age)
dog1.bark()
        