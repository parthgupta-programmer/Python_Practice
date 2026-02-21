 class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @property
    def move(self):
        print("Airplane move")
class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @property
    def move(self):
        print("Boat move")
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @property
    def move(self):
        print("Car move")
p1=Plane("Boeing","747")
b1=Boat("Ibiza","Touring 20")
c1=Car("Ford","Mustang")


for x in (p1,b1,c1):
    x.move


# Polymorphism(Many Forms): When the same method/operator/function can be applied to many different objects or classes.
# len() function can be applied to many classes (string,list,dictionary,etc.)


# Here ,in the above example,because of polymorphism we can execute the same method for all classes.

# Source : Learnt the concept from w3 Schools-python_polymorphism

