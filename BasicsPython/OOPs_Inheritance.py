# Inheritance: Creating a new class from existing once.


def lines(number_of_lines):
    print("--"*number_of_lines)

# 1. Single Inheritance
class Parent:
    def __init__(self):
        print("Parent Class")

    def Parent_method(self):
        print("Parent Method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class")

    def Child_method(self):
        print("Child Method")

p1 = Child()
p1.Parent_method()
p1.Child_method()


class RateOfInterest:
    interest = 0.5
    def __init__(self, name, loan_amount):
        self.name = name
        self.loan_amount = loan_amount
    def CalculateRateOfInterest(self):
        print(f"Hi {self.name}!, your loan amount is {self.loan_amount} with interest of {self.interest*self.loan_amount}")

class Student(RateOfInterest):
    interest = 0.02

class BusinessMan(RateOfInterest):
    interest = 0.1

class Labour(RateOfInterest):
    interest = 0.03

class People(RateOfInterest):
    pass

lines(40)
s1 = Student("Sagar", 5000)
s1.CalculateRateOfInterest()

b1 = BusinessMan("Business", 5000)
b1.CalculateRateOfInterest()

l1 = Labour("Labour", 5000)
l1.CalculateRateOfInterest()

p1 = People("People", 5000)
p1.CalculateRateOfInterest()


# 2. Multiple Inheritance
class Move:
    def move_forward(self):
        print("Moving forward")
    def move_back(self):
        print("Moving back")
class Jump:
    def jump_forward(self):
        print("Jumping forward")
    def jump_back(self):
        print("Jumping back")
class Right:
    def step(self):
        print("Right step")
class Left:
    def step(self):
        print("Left step")
    def lstep(self):
        print("Left step")

class GameStart(Move, Jump, Right, Left):
    pass

lines(40)
gamer1 = GameStart()
gamer1.move_forward()
gamer1.move_back()
gamer1.jump_forward()
gamer1.jump_back()
gamer1.step()
gamer1.step()
gamer1.lstep()
print(GameStart.mro())



# 3. Multi-level Inheritance
class Parentclass:
    def Parent_method(self):
        print("Parent Class")
class Child(Parentclass):
    def Child_method(self):
        print("Child Method")
class GrandChile(Child):
    def GrandChile_method(self):
        print("GrandChile method")

lines(80)
pp1 = GrandChile()
pp1.Parent_method()
pp1.Child_method()
pp1.GrandChile_method()