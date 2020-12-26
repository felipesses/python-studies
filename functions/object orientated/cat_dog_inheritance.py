###########################################

# CLASSES

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


dog = Dog("Billy", 14)

print(dog.get_name())

dog.set_name("felipe")

print(dog.get_name())


###########################################

# INHERITANCE

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i'm {self.age} years old")


class Cat(Pet):
    def speak(self):
        print("Meow")


cat = Cat("Felipe", 19)

cat.show()
