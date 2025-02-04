# || Object Oriented Programming(OOPs) Basics ||

# || Railway Reservasion Information Form using OOPs ||
class RailwayForm:
    formType = "RailwayForm"
    def printForm(self):
        print(f"Name is {self.name} & Age is {self.age}")

my_application = RailwayForm()
my_application.name = "Zihan"
my_application.age  = 15
my_application.printForm()

# || Sum of two numbers using OOPs ||
class Number:
    def sum(self):
        return self.a + self.b
num = Number()
num.a = 12
num.b = 23
print(num.sum())

# || Class Attributes & Instance Attributes using OOPs ||
class Employee:
    company = "Apple"  # Class Attributes
    salary  = 300      # Class Attributes
    
Zihan = Employee()
Zihan.company = "Microsoft"   # Instance Attributes
Zihan.salary = 100            # Instance Attributes are always prefered than Class Attributes
print(Zihan.salary)
print(f"The company of Zihan is:-{Zihan.company}")

# || Why should we use self parameter? ||
class Employee:
    company = "Apple"

    def getSalary(self):
        print(f"The salary of the company is:{self.salary}")
Zihan = Employee()
Zihan.salary = 1000
Zihan.getSalary() # It means, "Employee.getSalary(Zihan)". That's why we use self

# || Use of Static Method Decorator ||
class Employee:
    company = "Google"

    @staticmethod  # Decorator use for no parameter passing.
    def greet():
        print("Good Morning, Sir!")

Zihan = Employee()
Zihan.greet()

# || Use of "__init__" consructor & it's working technique ||
class Employee:
    company = "Google"
    
    def __init__(self):       # __init__ is called constructor, that run without calling it.
        print("It's Working!")  

# || Use of "__init__" consructor & it's working technique ||
Zihan = Employee()

class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name
        print("Employee is created!")

    def getSalary(self):
        print(f"Your salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, Sir!")

FSZ = Employee("Zihan") # Must need one argument 
FSZ.salary = 1000
FSZ.greet()
FSZ.getSalary() 
    