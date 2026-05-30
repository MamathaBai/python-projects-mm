class icecreamstand():
    def __init__(self, flavors):
        self.flavors = flavors
    def creamy(self):
        print(f"the icecream falvors is {self.flavors}")
icecreamstand1 = icecreamstand("chocalte")
icecreamstand1.creamy()
print(icecreamstand1.flavors)