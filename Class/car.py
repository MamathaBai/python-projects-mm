class car:
    """ A Simple attempt to represent a car"""
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descrptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"this car has {self.odometer_reading} miles on it")
    def update(self,milage):
        """ set the odometer reading to the given value.
        Reject the changes if it attempts to roll the odometer back"""
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:print("You can't roll back on odometer!")        
car1 = car("audi",'a4',2026)
print(car1.make)
print(car1.get_descrptive_name())
car1.read_odometer()

