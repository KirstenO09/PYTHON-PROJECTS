# Import ABC and abstractmethod from the abc module
from abc import ABC, abstractmethod

# Define an abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    # Regular method: shared by all animals
    def sleep(self):
        print(f"{self.name} is sleeping... 😴")

    # Abstract method: must be implemented by any subclass
    @abstractmethod
    def make_sound(self):
        pass

# Define a child class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent constructor
        self.breed = breed

    # Implement the abstract method
    def make_sound(self):
        print(f"{self.name} says: Woof! 🐶")

    # Additional method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball! 🎾")

# Create an object of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Call the regular method from the parent class
my_dog.sleep()

# Call the implemented abstract method
my_dog.make_sound()

# Call the child class's own method
my_dog.fetch()
