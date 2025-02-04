# || Inheritance of Object Oriented Programming(OOPs) ||

# || Single Inheritance ||
class Vehicle:
    '''Base class for all vehicles'''

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Driving", self.manufacturer, self.name)

    def turn(self, direction):
        print(f"Turning {self.name} to {direction}")
    
    def brake(self):
        print(self.name, "is stopping!")

class Car(Vehicle):
    '''Car class'''

    def changeGear(self, gear_name):
        '''Metods for gear changing'''
        print(self.name, "is changing gear to", gear_name)

if __name__ == "__main__":
    c = Car("Lafarrari", "Farrari", "Red")
    c.drive()
    c.brake()
    c.changeGear("fast")
  
# || Multiple Inheritance ||
class Freelancer: # First Parent class or base class
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:   # Second Parent class or base class
    company = "Visa"
    eCode = 120

class Programmer(Freelancer, Employee): # Inherited Child class or derived
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.company) # It prints Fiverr, cause in derived class there Freelancer class is on first position

# || Multilevel Inheritance ||
class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath()
# print(p.company) # throws an error

e = Employee()
e.takeBreath()
print(e.company)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)

# || Inheritance using Turtle ||
import turtle

class AjobTurtle(turtle.Turtle):
    '''AjobTurtle is a class for new type of turtle'''

    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        super().left(angle)

if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

turtle.done()

# || Super method in Inheritance ||
class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()  # It's calls the takebreath method of Person
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"
    
    def getSalary(self):
        print(f"No salary to programmers")
    
    def takeBreath(self):
        super().takeBreath()  # It's calls the takebreath method of Employee
        print("I am a Progarmmer so I am breathing++..")

p = Person()
p.takeBreath()
# print(p.company) # throws an error

e = Employee()
e.takeBreath()
print(f"My company is {e.company}")

pr = Programmer()
pr.takeBreath()
print(f"My company is {pr.company}")
print(f"My country is {pr.country}")

# || Class Method in OOPs ||
class Employee:
    company = "Bentley"
    location = "UK"

    # def changeLocation(self, new):
    #     self.__class__.company = new  # Using Dunder Method

    @classmethod
    def changeLocation(cls, new):  # Using class method decorator
        cls.company = new 

Harry = Employee()
print(Employee.company)

Harry.changeLocation("Cambridge")
print(Harry.company)

# || @Property/Getter and @Setter Method ||
class Employee:
    company = "Google"
    salary  = 5600
    salaryBonus = 500

    @property   # It's also called getter method
    def totalSalary(self):
        return self.salary + self.salaryBonus

    @totalSalary.setter  # It's setter method 
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary

emp = Employee()
print(emp.totalSalary) # It will called like a property
emp.totalSalary = 5800
print(emp.salaryBonus)

# || Operator Overloading in Python ||
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2): # __add__ is used to addition
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2): # __mul__ is used to multiplication
        print("Lets multiply")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)

# || Other Dunder Methods ||
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2): # __add__ is used to addition
        print("Lets add")
        return self.num + num2.num

    def __mul__(self, num2): # __mul__ is used to multiplication
        print("Lets multiply")
        return self.num * num2.num

    def __str__(self):  # prints the number
        return f"Decimal Number: {self.num}"

    def __len__(self):  # prints the length of the number
        return 3

n = Number(6)
print(n)
print(len(n))

# || Using Super Method to Call Base Class's Constructor ||
class Vehicle:

    def __init__(self, name, manufacturer, color):
        print("Creating a Vehicle")
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

class Car(Vehicle):

    def __init__(self, name, manufacturer, color, year):
        print("Creating a Vehicle")
        super().__init__(name, manufacturer, color)
        self.year = 2017
        self.weels = 4

if __name__ == "__main__":
    c = Car("Chiron", "Bugatti", "Blue", "2020")
    print(c.name, c.year, c.weels)

# || Choosing House for the Students of Hogwarts using Class Method ||
import random

class Hat:
    
    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))

if __name__ == "__main__":
    Hat.sort("Harry")