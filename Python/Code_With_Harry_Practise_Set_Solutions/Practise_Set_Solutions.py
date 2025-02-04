# || Code with Harry || Python tutorial || All Practise Set Solutions ||

# || Chapter 1 - Modules, Comments & Pip || Practice Set ||

# || Chapter 1 || Practice Set Solutions || no 1 || 
print('''Twinkle, twinkle, little star, 
How I wonder what you are!
Up above the world so high, 
Like a diamond in the sky.''')

# || Chapter 1 || Practice Set Solutions || no 2 ||
print("The Multiplication Table of 5 is :- ")
print(5 * 1)
print(5 * 2)
print(5 * 3)
print(5 * 4)
print(5 * 5)
print(5 * 6)
print(5 * 7)
print(5 * 8)
print(5 * 9)
print(5 * 10)

# || Chapter 1 || Practice Set Solutions || no 3 ||
import turtle
turtle.color("red", "green")
turtle.begin_fill()
r = 120
a = 360
turtle.circle(r, a)
turtle.end_fill()
turtle.done()

# || Chapter 1 || Practice Set Solutions || no 4 ||
'''
This os module helps us
to make our program eassy.
'''
import os
print(os.listdir())

# || Chapter 2 - Vriables & Data Types || Practice Set ||

# || Chapter 2 || Practice Set Solutions || no 1 ||
print("The result of adding 2 numbers is :-", 918681 + 939194 )

# || Chapter 2 || Practice Set Solutions || no 2 ||
print("The reminder when 555 is divided by 2 is :-", 555 % 2 )

# || Chapter 2 || Practice Set Solutions || no 3 ||
user = input("Enter any word :- \n")
print(type(user))

# || Chapter 2 || Practice Set Solutions || no 4 ||
a = 34
b = 80
print("Is a greater than b ? :-", a > b)

# || Chapter 2 || Practice Set Solutions || no 5 ||
a = int(input("Enter your first number :-\n"))
b = int(input("Enter your second number :-\n"))
print(f"The avarage of two numbers is :-{(a+b)/2}")

# || Chapter 2 || Practice Set Solutions || no 5 ||
a = int(input("Enter a number to get square of the number :-\n"))
print(f"The square of the number is :-{a ** 2}")

# || Chapter 3 - Strings || Practice Set ||

# || Chapter 3 || Practice Set Solutions || no 1 ||
user = input("Enter your name :-\n")
print("Good Afternoon!", user)

# || Chapter 3 || Practice Set Solutions || no 2 ||
letter = '''Dear <|name|>,
You are Selected!
<|date|>'''
user1st_q = input("Enter Your name:-\n")
user2nd_q = input("Enter Today's date:-\n")
letter = letter.replace("name", user1st_q)
letter = letter.replace("date", user2nd_q)
print("Your Selection letter is:-\n", letter)

# || Chapter 3 || Practice Set Solutions || no 3 ||
story = "This is a story.  |"
print(story.find("  "))

# || Chapter 3 || Practice Set Solutions || no"||
story = "This is a story.  |"
print(story.replace("  ", " "))


# || Chapter 3 || Practice Set Solutions || no 5 ||
letter = "Dear Harry,\n\tThis Python course is nice & helpful!\nThanks!"
print(letter)

# || Chapter 4 - Lists & Tuples || Practice Set ||

# || Chapter 4 || Practice Set Solutions || no 1 ||
f1 = input("Enter first fruit name   :-\n")
f2 = input("Enter second fruit name  :-\n")
f3 = input("Enter third fruit name   :-\n")
f4 = input("Enter forth fruit name   :-\n")
f5 = input("Enter fifth fruit name   :-\n")
f6 = input("Enter sixth fruit name   :-\n")
f7 = input("Enter seventh fruit name :-\n") 
list   = [f1, f2, f3, f4, f5, f6, f7]
print(list)

# || Chapter 4 || Practice Set Solutions || no 2 ||
s1   = int(input("Enter your marks :"))
s2   = int(input("Enter your marks :"))
s3   = int(input("Enter your marks :"))
s4   = int(input("Enter your marks :"))
s5   = int(input("Enter your marks :"))
s6   = int(input("Enter your marks :"))
list = [s1, s2, s3, s4, s5, s6]
list.sort()
print(list)

# || Chapter 4 || Practice Set Solutions || no 3 ||
a = (1, 2, 3)
a[0]= 5
print(a)

# || Chapter 4 || Practice Set Solutions || no 4 ||
list = [1, 2, 3, 4]
print(sum(list))

# || Chapter 4 || Practice Set Solutions || no 5 ||
a = (7, 0, 8, 0, 0, 9)
print(a.count("0"))

# || Chapter 5 - Dictionary & Sets || Practice Set ||

# || Chapter 5 || Practice Set Solutions || no 1 ||
my_dict = {
    "Boi" : "Book",
    "Kagoz": "Page",
    "Bati" : "Box"
}
print("The words of the dictionary are:-\n", my_dict.keys())
user = input("Choose any word to get it's English meaning:-\n")
print("The English meaning of the dictionary is:-", my_dict.get(user))

# || Chapter 5 || Practice Set Solutions || no 2 ||
n1  = int(input("Input number 1:-"))
n2  = int(input("Input number 2:-"))
n3  = int(input("Input number 3:-"))
n4  = int(input("Input number 4:-"))
n5  = int(input("Input number 5:-"))
n6  = int(input("Input number 6:-"))
n7  = int(input("Input number 7:-"))
n8  = int(input("Input number 8:-"))
set = {n1, n2, n3, n4, n5, n6, n7, n8}
print(set)

# || Chapter 5 || Practice Set Solutions || no 3 ||
set = {18, '18'}
print(set)

# || Chapter 5 || Practice Set Solutions || no 4 ||
s = set()
s.add(20)
s.add(20.0) # It will be counted as repetative 
s.add('20')
print(s)
print("The lenght of the set is:-", len(s))

# || Chapter 5 || Practice Set Solutions || no 5 ||
s = {}
print("The Type of 's' is:-\n", type(s))

# || Chapter 5 || Practice Set Solutions || no 6 ||
fav_lang = {}
a = input("What's your favourite language Zihan? \n :-")
b = input("What's your favourite language Zisan? \n :-")
c = input("What's your favourite language Zabir? \n :-")
d = input("What's your favourite language Kabir? \n :-")
fav_lang["Zihan"] = a
fav_lang["Zisan"] = b
fav_lang["Zabir"] = c
fav_lang["Kabir"] = d
print(fav_lang)

# || Chapter 5 || Practice Set Solutions || no 7 ||
fav_lang = {}
a = input("What's your favourite language Zihan? \n :-")
b = input("What's your favourite language Zisan? \n :-")
c = input("What's your favourite language Zabir? \n :-")
d = input("What's your favourite language Zihan? \n :-")
fav_lang["Zihan"] = a
fav_lang["Zisan"] = b
fav_lang["Zabir"] = c
fav_lang["Zihan"] = d # The leatest value will be allowed.
print(fav_lang)

# || Chapter 5 || Practice Set Solutions || no 8 ||
fav_lang = {}
a = input("What's your favourite language Zihan? \n :-")
b = input("What's your favourite language Zisan? \n :-")
c = input("What's your favourite language Zabir? \n :-")
d = input("What's your favourite language Kabir? \n :-")
fav_lang["Zihan"] = a # Python
fav_lang["Zisan"] = b
fav_lang["Zabir"] = c
fav_lang["Kabir"] = d # Python
print(fav_lang)

# || Chapter 5 || Practice Set Solutions || no 9 ||
s = {8, 7, 12, "Harry", [1, 2]} # We cannot use list in a set.
print(s)

# || Chapter 6 - Conditional Expressions || Practice Set ||

# ||Chapter 6 || Quick Quiz Solutions ||
user_age = int(input("How old are you?\n:-"))
if user_age >= 18:
    print("Yes")
else:
    print("No!")

# || Chapter 6 || Practice Set Solutions || no 1 ||
number_1 = int(input("Enter first number\n:-"))
number_2 = int(input("Enter second number\n:-"))
number_3 = int(input("Enter third number\n:-"))
number_4 = int(input("Enter forth number\n:-"))
# First Case
if number_1 > number_2:
    greater_number = number_1
elif number_2 > number_1:
    greater_number = number_2
# Second Case
if number_3 > number_4:
    bigger_number = number_3
elif number_3 < number_4:
    bigger_number = number_4
# Finale Case
if bigger_number > greater_number:
    greatest_number = bigger_number
else:
    greatest_number = greater_number
    print("In finale case, The greatest number is number greater nummber")
print("The Greater number is:-", greatest_number)

# || Chapter 6 || Practice Set Solutions || no 2 ||
Bng = int(input("Enter your Bangla marks\n:-"))
Eng = int(input("Enter your English marks\n:-"))
Math = int(input("Enter your Math marks\n:-"))
# In Banla
if Bng >= 33:
    print("You are passed in Bangla.")
else:
    print("You are faild in Bangla.")
# In English
if Eng >= 33:
    print("You are passed in English.")
else:
    print("You are faild in English.")
# In Mathematics
if Math >= 33:
    print("You are passed in Math.")
else:
    print("You are faild in Math.")
# In Total
total = (Bng + Eng + Math)
if total >= ((40 / 100) * 300):
    print("Congratulations! You have passed in all of your subjects.")
else:
    print("Sorry! You have faild.")

# || Chapter 6 || Practice Set Solutions || no 3 ||
text = input("Enter a comment\n:-")
if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
elif ("click this" in text):
    spam = True
else:
    spam = False
if spam == True:
    print("This text is spam.")
else:
    print("This text is not spam.")

# || Chapter 6 || Practice Set Solutions || no 4 ||
user_name = input("Enter your name\n:-")
length    = len(user_name)
if length > 10:
    print("This user name is not allowed. It's more than 10 characters.") 
else:
    print("This user name is allowed.")

# || Chapter 6 || Practice Set Solutions || no 5 ||
list = ['Hritik Roshan' , 'Shahruk Khan' , 'Tom Cruise' , 'Crist Evans', 'Crist Hemsworth']
user = input("Enter your favourite celebraty name\n:-")
if (user in list):
    print("Congratulations! Your favourite celebraty name is in the list.")
else:
    print("Sorry! Your favourite celebraty name is not in the list.")

# || Chapter 6 || Practice Set Solutions || no 6 ||
marks = int(input("Enter your Science marks\n:-"))
if marks >= 90:
    print("Your grade is 'Ex' for Exellent or 'A+'.")
elif marks >= 80:
    print("Your grade is 'A'.")    
elif marks >= 70:
    print("Your grade is 'B'.")
elif marks >= 60:
    print("Your grade is 'C'.")
elif marks >= 50:
    print("Your grade is 'D'.")
else:
    print("Your grade is 'F'.")

# || Chapter 6 || Practice Set Solutions || no 7 ||
post = input("Enter a story to post:-\n")
post = post.lower()
if "harry" in post:
    print("This post is talking about Harry.")
else:
    print("This post is not talking about Harry.")

# || Chapter 7 - Loops in Python || Practice Set ||

# ||Chapter 7 || Quick Quiz Solutions || First ||
n = 1
while n <= 50:
    print(n)
    n += 1

# ||Chapter 7 || Quick Quiz Solutions || Second ||
#  With While Loop
list = ["Hritik Roshan" , "Shahruk Khan" , "Tom Cruise" , "Crist Evans", "Crist Hemsworth"]
name = 0
while name < len(list):
    print(list[name])
    name += 1
#  With For Loop
list = ["Hritik Roshan" , "Shahruk Khan" , "Tom Cruise" , "Crist Evans", "Crist Hemsworth"]
for actors in list:
    print(actors)
    
# || Chapter 7 || Practice Set Solutions || no 1 ||
num = int(input("Enter a number to get it's multiplication table:-"))
for i in range(1, 11):
    print(num, 'X', i, '=', (num * i)) # Normally
# Same Using f string 
num = int(input("Enter a number to get it's multiplication table:-\n"))
for i in range(1, 11):   
    print(f"{num} X {i} = {num*i}")

# || Chapter 7 || Practice Set Solutions || no 2 ||
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
for name in l1:
    if name.startswith('S'):
        print(f"Congratulations! {name}")

# || Chapter 7 || Practice Set Solutions || no 3 ||
num = int(input("Enter a number to get it's multiplication table:-"))
i = 1 
while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i += 1

# || Chapter 7 || Practice Set Solutions || no 4 ||
num   = int(input("Enter a number (To get that it's prime or not) :-"))
prime = True
for i in range(2, num): 
    if (num % i == 0 and num != 2):
        prime = False
        break
if prime == False:
    print(num, " is not a prime number.")
else:
    print(num, " is a prime number.")
    
# || Chapter 7 || Practice Set Solutions || no 5 ||
user = int(input("Enter a number:-"))
num = 0
for i in range(user):
    num += i
    num += 1
print(f"The sum of the n natural numbers is:-{num}")

# || Chapter 7 || Practice Set Solutions || no 6 ||
num  = int(input("Enter a number:-"))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    print(f"The factorial of the number is {fact}")

# || Chapter 7 || Practice Set Solutions || no 7 ||
n = 3
for i in range(3):
    print(' ' * (n - i - 1), end = ' ')    # Hard to understand 
    print('*' * (2 * i + 1), end = ' ')
    print(' ' * (n - i - 1))

# || Chapter 7 || Practice Set Solutions || no 8 ||
for i in range(1, 4):
    print("*" * i)

# || Chapter 7 || Practice Set Solutions || no 9 ||

# || Chapter 7 || Practice Set Solutions || no 10 ||
num = int(input("Enter a number to get it's multiplication table:-"))
i   = 11 
while i > 1:
    i -= 1
    print(f"{num} X {i} = {num*i}")

# || Chapter 8 - Functions & Recursion || Practice Set ||

# ||Chapter 8 || Quick Quiz Solutions ||
user = input("Enter your name:-")
def greet(user):
    print("Good Day, ", user)
greet(user)

# || Chapter 8 || Practice Set Solutions || no 1 ||
num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))
num3 = int(input("Enter third number:-"))
def greatest_num(num1, num2, num3):
    if num1 > num2:
        big = num1
    else:
        big = num2
    if big > num3:
        great = big
    else:
        great = num3
    return print("The greatest of three numbers is :-", great)
greatest_num(num1, num2, num3)

# || Chapter 8 || Practice Set Solutions || no 2 ||
user = int(input("Enter Today's temparatue:-\n"))
def convert(statement, celcious):
    return print(statement, (celcious * (9/5)) + 32)
convert("The temparature in farehait is:-", user)

# || Chapter 8 || Practice Set Solutions || no 3 ||
print("Zihan", end = ' ')
print("Zisan", end = ' ')
print("Zabir")

# || Chapter 8 || Practice Set Solutions || no 4 ||
user = int(input("Enter a number:-\n"))
def recursive_sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return n + recursive_sum(n-1)
print("The sum of first n natural numbers is:-", recursive_sum( user))

# || Chapter 8 || Practice Set Solutions || no 5 ||
num = int(input("Enter a number for stars:-"))
def stars(n):
    for i in range(num):
        print ('*' * (num - i))
stars(num)

# || Chapter 8 || Practice Set Solutions || no 6 ||
inch = int(input("Enter inch to convert it into centimetre:-\n"))
def convert(inch):
    return (inch * 2.54)
print(convert(inch), "inch")

# || Chapter 8 || Practice Set Solutions || no 7 ||
car = "  Rolls Royace is a Luxury car. "
print(car)
user = input("Enter a word or letter to remove from it & strip it:-")
def remove(str, word):
    done = car.replace(user, '')
    return done.strip() 
print(remove(car, user))

# || Chapter 8 || Practice Set Solutions || no 8 ||
num = int(input("Enter a number to get it's multiplication table:-"))
def multiply(n):
    i = 1  
    while i <= 10:
        print(f"{num} X {i} = {num * i}")
        i += 1
multiply(num)

# || Chapter 9 - File I/O || Practice Set ||

# || Chapter 9 || Practice Set Solutions || no 1 ||
with open("poems.txt") as b:
    text = b.read()
if "twinkle" in text:
    print("Yes, The word 'twinkle' is in the text.")
else:
    print("No, The word 'twinkle' isn't in the text.")

# || Chapter 9 || Practice Set Solutions || no 2 ||
def game():
    return int(input("Enter your score:-"))
    
user_score = game()
with open("Hiscore.txt") as f:
    hiscore_str = f.read()
    if hiscore_str == '':
        with open("Hiscore.txt", 'w') as f:
            f.write(str(user_score))
    elif int(hiscore_str) <= user_score:
        with open("Hiscore.txt", 'w') as f:
            f.write(str(user_score))       # type casting in file's value
        print("Congratulations! Your score is new hiscore.")
    else:
        print("Your score is less than hiscore.")  

# || Chapter 9 || Practice Set Solutions || no 3 ||
for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i * j}")
            if j != 10:
                f.write('\n')

# || Chapter 9 || Practice Set Solutions || no 4 ||
with open("Donkey.txt") as f:
    text = f.read()
    if "Donkey" in text:
        text = text.replace("Donkey", "$%^@$^#")
        with open("Donkey.txt", 'w') as f:
            f.write(text) 

# || Chapter 9 || Practice Set Solutions || no 5 ||
words = ["Donkey", "Ass", "Pig"]
with open("Donkey.txt") as f:
    text = f.read()
    for word in words:
        text = text.replace(word, "$%^@$^#")
        with open("Donkey.txt", 'w') as f:
            f.write(text) 

# || Chapter 9 || Practice Set Solutions || no 6 ||
with open("log.txt") as f:
    text = f.read() # ".lower" can be used here
if "python" in text.lower():
    print("Yes, Python is in the text.")
else:
    print("No, Python is not in the text.")

# || Chapter 9 || Practice Set Solutions || no 7 ||
text = True
i = 1
with open("log.txt") as f:
    while text:
        text = f.readline()         # Hard to understand 
        if "python" in text.lower():
            print("Yes, Python is in the text.", i)
        i += 1
    
# || Chapter 9 || Practice Set Solutions || no 8 ||
with open("this.txt") as f:
    text = f.read()
with open("copy.txt", 'w') as f:
    f.write(text)

# || Chapter 9 || Practice Set Solutions || no 9 ||
file1 = "this.txt"
file2 = "copy.txt"
with open(file1) as f:
    text1 = f.read()
with open(file2) as f:
    text2 = f.read() 

if text1 == text2:
    print("Files are identical.")
else:
    print("Files are not identical.")

# || Chapter 9 || Practice Set Solutions || no 10 ||
with open("copy.txt", 'w') as f:
    f.write(' ')
    
# || Chapter 9 || Practice Set Solutions || no 11 ||  
import os
old_name = "sample.txt"
new_name = "renamed_by_python.txt"
with open(old_name) as f:
    text = f.read()
with open(new_name, 'w') as f:
    f.write(text)
os.remove(old_name)

# || Chapter 10 - Object Oriented Programming || Practice Set ||

# || Chapter 10 || Practice Set Solutions || no 1 ||
class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def information(self):
        print(f"The name of the Programmer working at {self.company} is {self.name}.") 
        
z = Programmer("Zihan", "Data Science", "10,000$")
z.information()

# || Chapter 10 || Practice Set Solutions || no 2 ||
class Calculator:
    user = int(input("Enter a number:-"))

    def square(self):
        print(f"The value of square is {self.user ** 2}")

    def cube(self):
        print(f"The value of cube is {self.user ** 3}")

    def squareroot(self):
        print(f"The value of squareroot is {self.user ** 0.5}")

user = Calculator()
user.square()
user.cube()
user.squareroot()

# || Chapter 10 || Practice Set Solutions || no 3 ||
class Number:
    a = 10
    def output(self):
        print(self.a)

num = Number()
num.a = 0
print(Number.a)
print(num.a)

# || Chapter 10 || Practice Set Solutions || no 4 ||
class Calculator:
    user = int(input("Enter a number:-"))
    @staticmethod
    def greet():
        print("Hello!")

    def square(self):
        print(f"The value of square is {self.user ** 2}")

    def cube(self):
        print(f"The value of cube is {self.user ** 3}")

    def squareroot(self):
        print(f"The value of squareroot is {self.user ** 0.5}")

user = Calculator()
user.greet()
user.square()
user.cube()
user.squareroot()

# || Chapter 10 || Practice Set Solutions || no 5 ||
availableSeats = int(input("Enter, How many seats are avaiable:"))
priceOfTickets = 50

class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"The name of the Train is {self.name}, available seats {self.seats}")
        print(f"The price of Ticket is {self.fare}")
    
    def bookTicket(self):
        if (self.seats != 0):
            print("Your Ticket is Booked!")
            self.seats = self.seats - 1
            print(f"Now, Seats available:{self.seats}")
        else:
            print("Sorry, Train has no seats.")

passenger = Train("Intercity Express", availableSeats, priceOfTickets)
passenger.getStatus()
passenger.bookTicket()

# || Chapter 10 || Practice Set Solutions || no 6 ||
class Sample:
    def sample(slf): # This parameter can be anything 
        print("ok")

experiment = Sample()  
experiment.sample()

# || Chapter 11 - Inheritance || Practice Set ||

# || Chapter 11 || Practice Set Solutions || no 1 ||
    # Vector

# || Chapter 11 || Practice Set Solutions || no 2 ||
class Animals:
    '''All Animals are Here'''
    animalType = "Mammal"

class Pets(Animals):
    '''All Pets are Here'''
    type = "cute"

class Dog(Pets):
    '''All Dogs are Here'''
    
    @staticmethod
    def bark():
        print("The dog is barking.")

tom = Dog()
tom.bark()
 
# || Chapter 11 || Practice Set Solutions || no 3 ||
class Employee:
    salary = 1000
    increment = 2
    salaryAfterIncrement = 1200

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.salaryAfterIncrement = val / self.salary

zihan = Employee()
print(zihan.salaryAfterIncrement)

# || Chapter 11 || Practice Set Solutions || no 4 ||
    # Complex Number

# || Chapter 11 || Practice Set Solutions || no 5 ||
    # Vector

# || Chapter 11 || Practice Set Solutions || no 6 ||
    # Vector

# || Chapter 11 || Practice Set Solutions || no 7 ||
    # Vector

# || Chapter 12 - Advanced Python 1 || Practice Set ||

# || Chapter 12 || Practice Set Solutions || no 1 ||
def readfile(filename):
    with open(filename) as f:
        print(f.read())
try:
    readfile("1.txt")
    readfile("2.txt")
    readfile("3.txt")

except FileNotFoundError as e:
    print("Sorry! There is no file in this directory named that.")

# || Chapter 12 || Practice Set Solutions || no 2 ||
list = ["first", "second", "third", "forth", "fifth", "sixth", "seventh"]
for index, item in enumerate(list):
    if index == 2 or index == 4 or index == 6:
        print(f"{item} is element no.{index + 1}")

# || Chapter 12 || Practice Set Solutions || no 3 ||
try:
    num   = int(input("Enter a number to get it's multiplication table:-"))
    list = [n * num for n in range(1, 11)]
    print(list)
except ValueError as e:
    print("Please enter a valid value!")

# || Chapter 12 || Practice Set Solutions || no 4 ||
def division(a, b):
    return a / b
try:
    first  = int(input("Enter first number:-"))
    second = int(input("Enter second number:-"))
    print(division(first, second))
except ZeroDivisionError as e:
    print("Infinite")

# || Chapter 12 || Practice Set Solutions || no 5 ||
try:
    num   = int(input("Enter a number to get it's multiplication table:-"))
    list = [n * num for n in range(1, 11)]
    print(list)
except ValueError as e:
    print("Please enter a valid value!")
with open("Tables.txt", 'a') as f:
    print(f.write(f"\n{str(list)}"))

# || Chapter 13 - Advanced Python 1 || Practice Set ||

# || Chapter 13 || Practice Set Solutions || no 1 ||
    # Virtual Environment 

# || Chapter 13 || Practice Set Solutions || no 2 ||

name  = input("Enter your name:-\n")
marks = input("Enter your marks:-\n")
phone_num = input("Enter your phone number:-\n")
print("The name of the student is {0}, his marks are {2} and phone number is {1}".format(name, phone_num, marks)) 

# || Chapter 13 || Practice Set Solutions || no 3 ||
li = [str(n * 7) for n in range(1, 11)]
print("\n".join(li))


# || Chapter 13 || Practice Set Solutions || no 4 ||
li = [43, 35, 60, 74, 85, 105, 5, 15]
divisible = lambda n : n % 5 == 0
print(list(filter(divisible, li)))

# || Chapter 13 || Practice Set Solutions || no 5 ||
from functools import reduce
li = [95, 88, 80, 98, 93, 100]
print(reduce(max, li))

# || Chapter 13 || Practice Set Solutions || no 6 ||
    # Pip Freeze

# || Chapter 13 || Practice Set Solutions || no 7 ||
    # Module: Flask
