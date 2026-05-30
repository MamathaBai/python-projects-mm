class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over."""
        print(f"{self.name} rolled over!")

# Create instance OUTSIDE the class
my_dog = Dog('Wellie', 6)
your_dog = Dog('Lucy',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"your dog's name is {your_dog.name}.")
print(f"your dog is {your_dog.age} years old.")
my_dog.sit()