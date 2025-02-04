# || Python Die Programming Shekha Part 2 || Object Oriented Programming and Web Crawling || Exercise part Solutions ||

# || Exersice of Unit 02 || Module & Package ||

# Exersice no.01
def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next   # Page no.19
    return fib_x  # It Will print 1 to before (n-1) fib

for x in range(1, 11):
    print(find_fib(x))

# Exersice no.02
def list_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1
    
    list = [1, 1]
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next   # Page no.19
        list.append(fib_next)
    return list

print(list_fib(10))

# Exersice no.03
def list_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1
    
    list = [1, 1]
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next   # Page no.25
        list.append(fib_next)
    return list

if __name__ == "__main__":
    print(list_fib(10))

# || Exersice of Unit 03 || Object & Class ||

# Exersice no.01
class Car:
    '''Car Class for All Methods of Cars'''

    def __init__(self, name, manufacturer, color, year, cc):
        self.name  = name
        self.manufacturer = manufacturer
        self.color = color
        self.year  = year
        self.cc    = cc
    
    def getInfo(self):
        print(f"The name of Car is {self.name} in {self.color} of {self.cc} cc, Manfactured by {self.manufacturer} in {self.year}")  # Page no.41

    def start(self):
        print(f"{self.name} is Starting")

    def brake(self):
        print(f"{self.name} is braking")

    def drive(self):
        print(f"Zihan is Driving {self.name}")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.name} is Turnig {self.direction}")
    
    def changeGear(self, gear):
        self.gear = gear
        print(f"{self.name} is Changing Gear into {self.gear}.")

mycar = Car("Dawn", "Rolls Royce", "White", "2019", "2200")
mycar.getInfo()
mycar.start()
mycar.brake()
mycar.drive()
mycar.turn("left")
mycar.changeGear("Max")

# || Exersice of Unit 04 || Requests Module & Creating File ||

# Exersice no.01
with open("test.txt", 'w') as f:
    f.write("This is for Python Book Exersice Solutions, Unit-04, ")

with open("test.txt", 'a') as f:
    f.write("Exercise of Page no.49")

# Exersice no.02
    # Cannot Solved // Exercise of Page no.53

# Exersice no.03
    # Cannot Solved // Exercise of Page no.54

# || Exersice of Unit 05 || More Working With File & Exception ||

# Exersice no.01
# Mistakes in the Following Program
with open("files.txt", 'r') as fp: 
    print(fp.read())  # File is not available, so it cannot read

with open("file.txt", 'w') as fp:                                       # Page no.59
    print(fp.read())  # File is in write mode, but here trying to read

# Exersice no.03
    # Cannot Solved // Exercise of Page no.60

# Exersice no.03
# Differences between "Syntax Error" & "Exeption"
# open("abc.txt") as f:
    # print(f.read())  # It's syntax error, for missing programming syntax
with open("abc.txt") as f:
    print(f.read())  # It's for Not Founding File named "abc.txt"

# || Exersice of Unit 06 || Inheritance ||

# Exersice no.01
class Vehicle:
    '''Vehicle Class for All Vehicles'''

    def __init__(self, name, manufacturer, color, year, cc):
        self.name  = name
        self.manufacturer = manufacturer
        self.color = color
        self.year  = year
        self.cc    = cc
    
    def start(self):
        print(f"{self.name} is Starting")

    def brake(self):
        print(f"{self.name} is braking")

    def drive(self):
        user = input("What's Your Name:-")
        print(f"{user} is Driving {self.name}")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.name} is Turnig {self.direction}")
    
    def changeGear(self, gear):
        self.gear = gear
        print(f"{self.name} is Changing Gear into {self.gear}.")

class MotorCycle(Vehicle):
    '''Motor Cycle Class That Inherited Vehicle Class'''

    def getInfo(self):
        user = input("What's Your Name:-")
        print(f"The name of {user}'s Motor Cycle is {self.name} in {self.color} of {self.cc} cc, Manfactured by {self.manufacturer} in {self.year}")  # Page no.73

if __name__ == "__main__":
    mybike = MotorCycle("Ninja H2R", "Kawasaki", "Black", "2020", "3300")
    mybike.getInfo()

# || Exersice of Unit 07 || Regular Expression ||

# Exersice no.01
    # Cannot Solved // Exercise of Page no.88

# Exersice no.02
    # Cannot Solved // Exercise of Page no.92
