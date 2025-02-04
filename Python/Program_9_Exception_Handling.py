# || Exception Handing in Factorial Fuction using Recursion || 
def recusive_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * recusive_factorial(n - 1)
try:
    user = int(input("Enter a number:-"))
except Exception as e:
    print(f"You made a error:- {e}")
print(recusive_factorial(user))

# || More than one Exception Handling Different Statement for Some Exception || 
try:
    num = int(input("Enter a number:-"))
    def square(n):
        return 100 // n
    print(square(num))
except ZeroDivisionError as e:
    print("Please don't enter 0!")
except ValueError as e:
    print("Please enter a valid value!")
except Exception as e:
    print(e)

# || Exception Raise in python ||
def increment(n):
    return n + 1
    
try:
    num = int(input("Enter a number:-"))
except:
    raise ValueError("It's not allowed!")

print(increment(num))

# || Try with else clause ||
def recusive_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * recusive_factorial(n - 1)
try:
    user = int(input("Enter a number:-"))
except Exception as e:
    print(f"You made a error:- {e}")
else:
    print("This Program ran without error!")
print(recusive_factorial(user))

# || Try with finally clause ||
try:
    num = int(input("Enter a number:-"))
    def square(n):
        return 100 // n
    print(square(num))
except ZeroDivisionError as e:
    print("Please don't enter 0!")
except ValueError as e:
    print("Please enter a valid value!")
except Exception as e:
    print(e)
finally:
    print("We are done any how!")