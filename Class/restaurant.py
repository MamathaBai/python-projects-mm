class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("serves food")
    def open_restaurant(self):
        print("open")
R1 = Restaurant('Indian',"Indian food") 
R2 = Restaurant("chinese","chinese food")
print(R1.restaurant_name) 
print(R1.cuisine_type) 
R1.describe_restaurant() 
R1.open_restaurant()
print(R2.restaurant_name) 
print(R2.cuisine_type) 
R2.describe_restaurant() 
R2.open_restaurant() 