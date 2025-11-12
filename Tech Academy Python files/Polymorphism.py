# Parent class: Animal
class Animal:
    def __init__(self, name, breed, age):
        # Common attributes for all animals
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        # This method will be overridden by child classes
        return f"{self.name} makes a sound."


# Child class: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed, age):
        # Initialize parent attributes
        super().__init__(name, breed, age)
        # Dog-specific attributes
        self.favorite_food = "Meat"
        self.favorite_toy = "Ball"

    def speak(self):
        # Polymorphism: overriding the parent method
        return (
            f"{self.name} barks.\n"
            f"Breed: {self.breed}\n"
            f"Age: {self.age}\n"
            f"Food: {self.favorite_food}\n"
            f"Toy: {self.favorite_toy}"
        )


# Child class: Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name, breed, age):
        # Initialize parent attributes
        super().__init__(name, breed, age)
        # Cat-specific attributes
        self.color = "Gray"
        self.favorite_drink = "Milk"

    def speak(self):
        # Polymorphism: overriding the parent method
        return (
            f"{self.name} meows.\n"
            f"Breed: {self.breed}\n"
            f"Age: {self.age}\n"
            f"Color: {self.color}\n"
            f"Drink: {self.favorite_drink}"
        )


# Create instances of Dog and Cat
dog1 = Dog("Buddy", "Golden Retriever", 5)
cat1 = Cat("Whiskers", "Korat", 7)

# Demonstrate polymorphism: same method name, different behavior
if __name__ == "__main__":
    print(dog1.speak())  # Output: Buddy barks...
    print(cat1.speak())  # Output: Whiskers meows...
