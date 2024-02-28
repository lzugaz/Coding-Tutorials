# Classes and Object-Oriented Programming

# Part 1: Defining a Class
# Classes provide a means of bundling data and functionality together.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.

class Dog:
    # Class variables shared by all instances
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Part 2: Creating Instances of a Class
# To create instances of a class, call the class using class name and pass the arguments that its __init__ method accepts.

my_dog = Dog("Rex", 2)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")

# Part 3: Instance Methods
# Instance methods are functions defined inside a class and can only be called from an instance of that class.

class Dog:
    # Class variable
    species = "Canis familiaris"

    # Initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an instance of Dog
my_dog = Dog("Rex", 2)
print(my_dog.description())  # Calling instance method
print(my_dog.speak("Woof"))  # Passing argument to instance method

# Part 4: Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Bulldog(Dog):  # Inherits from Dog class
    def run(self, speed):
        return f"{self.name} runs at {speed} speed."

# Creating an instance of Bulldog, which has access to Dog's methods plus its own
my_bulldog = Bulldog("Tom", 4)
print(my_bulldog.description())
print(my_bulldog.run("slowly"))

# Part 5: Polymorphism
# Polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

class Poodle(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)  # Using super() to call the parent class's method

my_poodle = Poodle("Max", 1)
print(my_poodle.speak())  # Overrides the default sound

# Conclusion:
# This guide introduces the basics of Python classes, including how to define and instantiate classes,
# the use of instance methods, inheritance, and polymorphism. Practice with these concepts to become comfortable with object-oriented programming in Python.
