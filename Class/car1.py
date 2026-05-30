class car:
    def __init__(self,make,model,year):
        """Intialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descrptive_name(self):
        """ Return a neatly formmated dexriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement reading to the given value."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,mileage):
        """set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """Adding the given amount to the odometer reading."""
        self.odometer_reading += miles
class ElectricCar(car):
    """Represent aspects of a car, specfic to electric vechiles."""
    def __init__(self,make,model,year):
        """Intialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery_size = 40
    def describe_battery(self):
        """ Print a statement describing the battery size."""
        print(f"the car has a {self.battery_size} - KWh battery.")
my_leaf = ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descrptive_name())
print(my_leaf.read_odometer())
my_leaf.describe_battery()
