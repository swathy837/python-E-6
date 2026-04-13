import sys

class Product:

    class Specification:
        def __init__(self, brand, price):
            self.brand = brand
            self.price = price

        def display_spec(self):
            print("Brand:", self.brand)
            print("Price:", self.price)

    def __init__(self, name):
        self.name = name
        self.spec = None

    def add_specification(self, brand, price):
        self.spec = Product.Specification(brand, price)

    def display(self):
        print("\nProduct Name:", self.name)
        if self.spec:
            self.spec.display_spec()


class Supplier:
    def __init__(self, supplier_name):
        self.supplier_name = supplier_name

    def display(self):
        print("Supplier Name:", self.supplier_name)


p_name = input("Enter product name: ")
brand = input("Enter brand: ")
price = float(input("Enter price: "))
s_name = input("Enter supplier name: ")

p1 = Product(p_name)
p1.add_specification(brand, price)

s1 = Supplier(s_name)

p1.display()
s1.display()

print("\nProduct reference count:", sys.getrefcount(p1))
print("Supplier reference count:", sys.getrefcount(s1))

p2 = p1
s2 = s1

print("\nAfter creating new references")
print("Product reference count:", sys.getrefcount(p1))
print("Supplier reference count:", sys.getrefcount(s1))

del p2
del s2

print("\nAfter deleting references")
print("Product reference count:", sys.getrefcount(p1))
print("Supplier reference count:", sys.getrefcount(s1))
