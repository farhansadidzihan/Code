# || First code with Function ||
def myfnc(x):
    print("inside myfnc" , x)
    x = 10
    print("inside myfnc" , x)

x = 20 
myfnc(x)
print(x)
 
# || Second code with Function ||
def myfnc(y):
    print("y =" , y)
    print("x =" , x)

x = 20
myfnc(x)

# || Third code with Function ||
def myfnc(x , z , y = 10):
    print("x =" , x , "y =" , y , "z =" , z)

myfnc(x = 1 , y = 2 , z = 3) 
a = 5 
b = 6
myfnc(x = a , z = b)
a = 1
b = 2
c = 3
myfnc(y = a , z = b , x = c)

# || Fourth code with Function ||
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

result = add_numbers([1 , 2 , 3 , 4 , 5])
print(result)

# || Fifth code with Function ||
def test_fnc(li):
    li[0] = 212
    li[3] = 44

my_list = [1 , 2 , 3 , 4]
print("before function call" , my_list)
test_fnc(my_list)
print("after function call" , my_list)

# || Factorial of numbers using Function & Recurtion ||
user = int(input("Enter a number:-"))
def recusive_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * recusive_factorial(n - 1)
print(recusive_factorial(user))

# || Sum of n natural numbers using Function & Recursion ||
user = int(input("Enter a number:-\n"))
def recursive_sum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return n + recursive_sum(n-1)
print("The sum of first n natural numbers is:-", recursive_sum( user))

# || Using Lambda Function ||
user = int(input("Enter Today's temparatue:-\n"))
convert = lambda c : c  * (9 / 5) + 32  # Lambda usually used to give function as a argument
print(f"The temparature in farehait is:- {convert(user)}")

# || Using enumerate Function ||
list = ["Zihan", "Zisan", "Zabir", True]
for index, item in enumerate(list):
    print(f"{index + 1}. {item}")

# || A Function to Find Prime numbers ||
def is_prime1(n):
    if n < 2:
        return False 
    prime = True
    for x in range(2, n):
        if n % x == 0:
            print(n, "is divisible by", x)
            prime = False
        return prime

while True:
    number = input("Please enter a number(enter 0 to exit):-")
    number = int(number)
    if number == 0:
        break
    prime = is_prime1(number)
    if prime is True:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")
        
# || Default Parameter Value ||
def sum(num1 = 3, num2 = 5):
    return print(num1 + num2)
    
sum()

# A Function to greet User
user = input("Enter your name:-")
def greet(user):          
    return "Good Day, " +  user
name = greet(user)
print(name)
# Same Function with another style 
user = input("Enter your name:-")
def greet():          
    return "Good Day, " + user
name = greet()
print(name)

# || Student With House of Hogwarts, Harry Potter ||
def get_student():
    student = {}
    student["name"] = input("Name:- ")
    student["house"] = input("House:-")
    return student

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

if __name__ == "__main__":
    main()

# || A Function to get Fibonacci Number ||
def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n :
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next

def list_fib(n):
    fib_list = [1, 1]
    if n <= 2:
        return fib_list[:n]

    fib_x, fib_next = 1, 1

    i = 3
    while i <= n :
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        fib_list.append(fib_next)
    return fib_list

for x in range(1, 11):
    print(find_fib(x))
    
print(list_fib(10))