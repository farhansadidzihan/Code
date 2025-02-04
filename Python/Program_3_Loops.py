# First
a = 0
b = 1
for i in range(50):
    a += b
    b += 1
print(a)
   
# Second
a = 0 
for i in range(1 , 51):
    a += i
print(a)

# Third
for i in range(5 , 50 , 5):
    print(i)

# Fourth
numbers = [6 , 1 , 4 , 6 , 9 , 7 , 5 , 40 ,333, 342]
max_n   = numbers[0]
for n in numbers:
    if n > max_n:
        max_n = n
print(max_n)

# Fifth
result = 0
for n in range(5 , 101 , 5):
    print(n)
    result += n
print("The sum is :-" , result)

# Sixth
i = 1
while i <= 7:
    print(i * '$')
    i += 1
# Opposite Site
i = 7
while i >= 1:
    print(i * '$')
    i -= 1

# loop in string
a = "barcelona"
# using for loop
for i in a:
    print(i)
# using while loop
i = 0
while i < len(a):
    print(a[i])
    i += 1

# Loop in List 
# Favourite,
Actors      = ['Hritik Roshan' , 'Shahruk Khan' , 'Tom Cruise' , 'Crist Evans', 'Crist Hemsworth']
Players     = ['Cristiano Ronaldo' , 'Messi' , 'Neymar JR']
Youtubers   = ['Marshmallow', 'Mr.Beast']
Persons     = ['Mohammad(s)' , 'Elon Mask' , 'Sundar Pichai' , 'Aman Dattarwala']
Billionires = ['Elon Mask ' , 'Jeff Bezoz' , 'Bill Gates' , 'Jack Ma' ]
Companies   = ['Apple' , 'Google' , 'Microsoft' , 'Tesla' , 'Royal Z']
Cars        = ['Rolls Royace' , 'Lamborgini' , 'Farrari' , 'Bugatti' , 'Bentley' , 'Tesla']
for car in Cars:
    print(car , "is a favourite car of Zihan")

# || Multiplication table by Loop ||
n = input("Input an integer:-")
n = int(n)

m = 1
while m <= 10:
    print(n , "x" , m , "=" , n*m)
    m += 1

# || Loop || Break & Continue 1
while True:
    n = int(input("Inter a positive number(0 to exit): "))
    if n < 0:
        print("We only allow positive number. Please try again!")
        continue
    if n == 0:    
        break
    print("Square of" , n , "is" , n*n)

# || Loop || Break & Continue 2
terminate = False
while not terminate:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    if num1 < 0:
        print("Please enter a positive number!")
        continue
    if num2 < 0:
        print("Please enter a positive number!")
        continue
    while True:
        operator = input("Select a oparator(enter 0 to exit):")
        if operator == '0':
            terminate = True 
            break
        elif operator == '+':
            print(num1 + num2) 
            break
        elif operator == '-':
            print(num1 - num2)
            break
        elif operator == '*':
            print(num1 * num2)
            break
        elif operator == '/':
            print(num1 / num2)
            break
        elif operator == '%':
            print(num1 % num2)
            break
        else:
            print("Unknown Operator!")

# || Fibonacci Number Finding using Loop ||
fib_x    = 1  
fib_next = 1  
n        = int(input("enter a number :-"))
if n <= 2:
    fib_n = 1
else:
    i = 3
    while i <= n:
        i += 1
        fib_next, fib_x = fib_next + fib_x, fib_next
    fib_n = fib_next
print(fib_n)
