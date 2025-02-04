# || Python Die Programming Shekha Part 1 || Python Basics || Exercise part Solutions ||

# || Exersice of Unit 03 || Variable, Data Type & Arithmatic Operation ||

# Exersice no.01
num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '+' Operator
print(f"{num1} + {num2} = {num1 + num2}")

num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '-' Operator
print(f"{num1} - {num2} = {num1 - num2}")

num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '*' Operator
print(f"{num1} * {num2} = {num1 * num2}")
                                                                # Page no.25
num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '/' Operator
print(f"{num1} / {num2} = {num1 / num2}")

num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '%' Operator
print(f"{num1} % {num2} = {num1 % num2}")

num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '//' Operator
print(f"{num1} // {num2} = {num1 // num2}")

num1 = int(input("Enter a number:-"))
num2 = int(input("Enter another number:-")) # With '**' Operator
print(f"{num1} ** {num2} = {num1 ** num2}")

# || Exersice of Unit 04 || Conditional Logic ||

# Exersice no.01
num = int(input("Enter a number:"))
if num < 0:
    print("The number is Negative.")  # Page no.35
else:
    print("The number is Positive.")

# Exersice no.02
num = int(input("Enter a number:"))
if num == 0:
    print("The number is 0.")
elif num % 2 == 0:
    print("The number is a Even Number")  # Page no.35
else:
    print("The number is not Evern Number.")

# Exersice no.03
year = int(input("Enter Any Year:-"))
if year % 100 != 0 and year % 4 == 0:
    print("Yes, The Year is a Leap Year.")
elif year % 100 == 0 and year % 400 == 0:  # Page no.39
    print("Yes, The Year is a Leap Year.")
else:
    print("No, The Year is not Leap Year.")

# || Exersice of Unit 05 || Introducing with Turtle ||

# 01
import turtle
turtle.color("Blue", "red")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)  # Page no.42
    turtle.left(120)
turtle.end_fill()
turtle.done()

# || Exersice of Unit 07 || Function ||
# Exersice no.01
import turtle
user = int(input("Enter a line of the triangle:"))
def triangle(lenth):
    for i in range(3):
        turtle.forward(lenth)  # Page no.60
        turtle.left(120)
    turtle.done()
print(triangle(user))

# 02  
marks = [91, 86, 81, 83, 91, 84]
def mean(list):
    return (sum(list) // len(list))  # Page no.65
print(mean(marks))

# 03
user = int(input("Enter a number to get it's multiplication table:"))
def multiply(n = 1):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")  # Page no.65
multiply(user)

# || Exersice of Unit 08 || Working with String ||

# Exersice no.01    
    # Cannot Solved // Exercise of Page no.73

# Exersice no.02
str   = input("Enter Any word of ten letters:-")
new_str = str[1] + str[0] + str[3] + str[2] + str[5] + str[4] + str[7] + str[6] + str[9] + str[8]  # Page no.74
print(new_str)

# 03
str   = input("Enter Any word of five letters:-")
str2 = str[4] + str[3] + str[2] + str[1] + str[0]  # Page no.74
if str == str2:
    print(f"{str} is a \"Palindrome Word\".")
else:
    print(f"{str} is not a \"Palindrome Word\".")

# || Exersice of Unit 09 || Varity of Data Structue in Python ||

# 01
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = [n ** 2 for n in list]  # Page no.81
print(square_list)

# Exersice no.02
marks_dict = {
    "Zihan" : {"Bangla" : 100, "English" : 99, "Math" : 98 },
    "Zisan" : {"Bangla" : 98, "English" : 99, "Math" : 100 },  # Page no.91
    "Zabir" : {"Bangla" : 99, "English" : 100, "Math" : 98 }
}  # Here can create a problem for this, "Can we use dictionary as a dictinary value?"
print(marks_dict.items())

# Exersice no.03
bd_division_info = {
    "Barishal"   : {"district" : 6, "upazilla" : 39, "union" : 333},
    "Chittagong" : {"district" : 11, "upazilla" : 97, "union" : 336},
    "Dhaka"      : {"district" : 13, "upazilla" : 93, "union" : 1833},  # Page no.96
    "Khulna"     : {"district" : 10, "upazilla" : 59, "union" : 270},
    "Mymensingh" : {"district" : 4, "upazilla" : 34, "union" : 350},
    "Rajshahi"   : {"district" : 8, "upazilla" : 70, "union" : 558},
    "Rangpur"    : {"district" : 8, "upazilla" : 58, "union" : 536},
    "Sylhet"     : {"district" : 4, "upazilla" : 38, "union" : 334}
}
list1 = []
list2 = []
list3 = []
for headquarters in bd_division_info:
    list1.append(bd_division_info[headquarters]["district"])
    list2.append(bd_division_info[headquarters]["upazilla"])
    list3.append(bd_division_info[headquarters]["union"])
print(f"Total Districts are:-{sum(list1)}\nTotal Upazillas are:-{sum(list2)}\nTotal Unions are:-{sum(list3)}")
    
# || Exersice of Unit 10 || Some Entertaining Programs ||

# Exersice no.01
import turtle
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtle.penup()
turtle.speed(0)

for i in range(500):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)  # It will throw an error for index out of range
    turtle.setposition(x, y)
    i = random.randint(0, len(colors))  # Page no.101
    turtle.dot(colors[i])
turtle.done()

# Exersice no.02
    # Cannot Solved // Exercise of Page no.111

# Exersice no.03
import turtle
fib_x = 1
fib_next = 1
i = 3
while i <= 13:
    i += 1
    fib_temp = fib_x + fib_next  # Page no.114
    fib_x    = fib_next
    fib_next = fib_temp
    turtle.circle(fib_next, 120)
turtle.done()
