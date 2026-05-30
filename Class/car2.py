class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


class ElectricCar(Car):

    def __init__(self, make, model, year):   # FIXED HERE
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"The car has a {self.battery_size}-KWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())
my_leaf.read_odometer()
my_leaf.describe_battery()