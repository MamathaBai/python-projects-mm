class student:
    def __init__(self,fullname,age):
        self.name = fullname
        self.age = age
s1  = student("Raj",40)
s2 = student("Mamatha",34)
print(f"{s1.name} and  age is {s1.age}")
print(f"{s2.name} and age is {s2.age}")
