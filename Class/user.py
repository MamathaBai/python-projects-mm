class user:
    def __init__(self,fisrt_name,last_name):
        self.fisrt_name = fisrt_name
        self.last_name  = last_name
    def describe_user(self):
        print(f"Information of this {self.fisrt_name} is nice and good guy")
    def greet_user(self):
        print(f"Welcome {self.fisrt_name}!")
user1 = user("raj","K")
user2 = user("Mamatha","M")
print(f"{user1.fisrt_name} {user1.last_name}")
user1.describe_user()
user1.greet_user()
print(f"{user2.fisrt_name} {user2.last_name}")
user2.describe_user()
user2.greet_user()