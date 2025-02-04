# || Moduels like turtle, random, math, timeit, os, webbrowser, datetime ||

# || "Guess the correct answer Game." using random module || playing by human

import random

numbers = random.randint(1, 100)
attemps = 0

while True:
    input_numbers = input("Guess a number between 1 & 100:- \n")
    input_numbers = int(input_numbers)
    attemps += 1 
    if input_numbers == numbers:
        print("Yes, Your guess is correct!")
        break
    if input_numbers > numbers:
        print("Sorry! The number is less than your guess.")
    else:
        print("Sorry! The number is greater than your guess.")
print("You tried:", attemps, "Times to find the correct number.")

# || "Guess the correct answer Game." using random module || playing by Computer ||
import random 

number  = random.randint(1, 100)
attemps = 1
low     = 1
high    = 100
while True:
    print("Guess the number (between 1 & 100) :- \n")
    input_number = (low + high) //2 
    print("My Guess is", input_number)
    attemps += 1

    if input_number == number:
        print("Yes, your guess is correct!")
        break
    if input_number > number:
        print("Sorry! Your number is greater than guess.")
        high = input_number - 1 
    else:
        print("Sorry! Your number is less than guess.")
        low = input_number + 1

print("You tried", attemps, "times to find the correct answer!")

# || Using Math Module Comparing 2 program ||
import math

def is_prime2(n = 1013):
    if n < 2:
        return False
    if n == 2:
        return True 
    if n % 2 == 0:
        return False
    m = math.sqrt(n)
    m = int(m) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
        return True

def is_prime3(n = 1013):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    prime = True
    for x in range(3, n, 2):
        if n % x == 0:
            prime = False
            return prime
        return prime

import timeit
t2 = timeit.timeit(is_prime2)
t3 = timeit.timeit(is_prime3)    
print(t2, t3)

# || Deleting File using os module ||
import os
old_name = "sample.txt"
new_name = "renamed_by_python.txt"
with open(old_name) as f:
    text = f.read()
with open(new_name, 'w') as f:
    f.write(text)
os.remove(old_name)

# || Using Datetime Module ||
from datetime import datetime # Here first datetime is module & second is class
print(datetime.today())

# || Using webbrowser module to brouse in web ||
import webbrowser as wb
wb.open("http://google.com")

# || Creating own Module & Importing It From Another File ||
# Creating a function 
def greet(name):
    print(f"Good Morning! {name}")

if __name__ == "__main__":
    try:
        user = input("Enter your name:-")
        greet(user)
    except Exception as e:
        print(f"You made a error:- {e}")
# importing that function from another file
# import greet # It's importing greeet from another file
name = input("What's your name?\n:-")
greet.greet(name)

# || Using sys module's exit method ||
import sys

class Student:
    def __init__(self, name, house):
        if not name:
            sys.exit("Missing Name!")
        self.name  = name
        self.house = house

name = input("Name: ")
house = input("House: ")
Harry = Student(name, house)

# || Circle Using turtle ||
import turtle
r = 120
a = 360
turtle.circle(r, a)
turtle.done()

# Loop in Turtle
import turtle

turtle.shape("turtle")
turtle.speed(1)

for side_length in range(50 , 100 , 10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)
        

turtle.exitonclick()

# Loop in Turtle
import turtle

turtle.shape("turtle")
turtle.speed(1)
turtle.color("red", "green")

turtle.begin_fill()
for i in range(4):
    for i in range(20):
        turtle.forward(2)
        turtle.penup()
        turtle.forward(3)
        turtle.pendown()
    turtle.left(90)
    
turtle.end_fill()
turtle.done()

# Turtle using While Loop
import turtle 

turtle.shape("turtle")
turtle.color("black")
turtle.speed(1)
   
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    counter += 1 

turtle.exitonclick()

# Dot Graph using Turtle Loop
import turtle

height = 5
width  = 5

turtle.speed(1)

turtle.penup() ,

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)

turtle.exitonclick()
 
# ||Turtle || Using Function & Loop ||
import turtle

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0 
while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()

# || Turtle begin_fill & end_fill ||
import turtle
turtle.color("red", "green")
turtle.begin_fill()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.end_fill()

# || Sun project using Turtle ||
import turtle
turtle.color("red", "yellow")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break
turtle.end_fill()
turtle.done()

#  || Random || Random & Radiant ||
import random
print(random.random())
print(random.randint(1, 10))

# || Random & Turtle ||
import turtle
import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
turtle.penup()
turtle.speed(0)

for i in range(500):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    i = random.randint(0, len(colors)-1)
    turtle.dot(colors[i])

turtle.done()
