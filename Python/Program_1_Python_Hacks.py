# || "a == '' & not a" is same ||
name = input("Name: ")
house = input("House: ")
if name == '': # Same as not name
    print("No Name is given!")
if not name:  # Same as name == ''
    print("No Name is given!")

# || Colouring & Styling Output || 
from colorama import Fore, Back, Style
print(f"{Style.BRIGHT} He{Fore.RED}llo {Back.BLUE}World")

# || Walrus Operator ||
n = [1, 2, 3, 4, 5]
while (num := len(n)) > 0:
	print(n.pop())
l = []
while (i := input("enter:- ")) != "q":
	l.append(i)
print(l)

# || Os Module ||
import os
if (not os.path.exists("directory")):
	os.mkdir("directory")
for i in range(0, 100):
	os.mkdir(f"directory/Tutorial {i+1}")
	os.rename(f"directory/Tutorial {i+1}", f"directory/Day {i+1}")
folders = os.listdir("directory")
print(folders)
print(os.getcwd())

# || Shutil Module ||
import shutil
import os
shutil.copy("main.py", "main2.py")
shutil.copytree("testing", "mytesting")
shutil.move("testing/main2.py", "main2.py")
shutil.move("main2.py", "testing/")
os.remove("testing/main2.py")

# || Requests & BeautifulSoup Modules ||
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
for h2 in soup.find_all("h2"):
	print(h2.text)
print(soup.prettify())

# || Command Line Utilities ||
import argparse
import requests
def download_file(url, local_filename): 
  if local_filename is None:
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
      r.raise_for_status()
      with open(local_filename, 'wb') as f:
          for chunk in r.iter_content(chunk_size=8192): 
              # If you have chunk encoded response uncomment if
              # and set chunk_size parameter to None.
              #if chunk: 
              f.write(chunk)
  return local_filename
parser = argparse.ArgumentParser()
# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)
# Parse the arguments
args = parser.parse_args()
# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)

# || Function Caching ||
import functools
import time
@functools.lru_cache(maxsize=None)
def fx(n):
	time.sleep(3)
	return n * 5
print(fx(20))
print(fx(40))
print(fx(60))
print(fx(20))
print(fx(40))
print(fx(60))

# || Asyncio Module in Python ||
import asyncio
import requests
async def function1():
	URL = "https://instagram.com/favicon.ico"
	response = requests.get(URL)
	open("instagram.ico", "wb").write(response.content)
	await asyncio.sleep(1)
	print("function1")
async def function2():
	URL = "https://instagram.com/favicon.ico"
	response = requests.get(URL)
	open("instagram2.ico", "wb").write(response.content)
	await asyncio.sleep(1)
	print("function2")
async def function3():
	URL = "https://instagram.com/favicon.ico"
	response = requests.get(URL)
	open("instagram3.ico", "wb").write(response.content)
	await asyncio.sleep(1)
	print("function3")
async def main():
	# await function1()
	# await function2()
	# await function3()
	L = await asyncio.gather(function1(), function2(), function3())
	print(L)
asyncio.run(main())

# || Multithreading in Python ||
import threading
import time
def func(s):
	print(f"sleeping for {s} seconds")
	time.sleep(s)
tm1 = time.perf_counter()
func(4)
func(3)
func(1)
tm2 = time.perf_counter()
print(f"Time Taken {tm2 - tm1} ")
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
tm3 = time.perf_counter()
print(f"Time Taken with Threading {tm3 - tm2}")

# || seek(), tell() & truncate() functions ||
with open("file.txt", 'r') as f:
	f.seek(3)
	print(f.tell())
	data = f.read()
	print(data)
with open("file.txt", 'w') as f:
	f.write("Hello World!")
	f.truncate(3)
with open("file.txt", 'r') as f:
	print(f.read())

# || Binary & Decimal Conversation ||
num = 100
print(bin(num)[2: ]) # Gives the Binary representation
print(int(str(num), 2)) # Gives the Decimal representation
print(chr(num)) # Gives the ASCII character of that number
print(ord("z")) # Gives the Unicode for one-character string

# || Shallow Copy || Deep Copy ||
import copy
arr = [1, 2, 3, 4, 5, 6, 7]
list1 = arr.copy()
list2 = list(arr)
list3 = arr[:]
deep_list = copy.deepcopy(arr)
print(list1, list2, list3, deep_list)

# || Usage of * asterisk to unpack list data ||
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = (11, 22, 33, 44, 55, 66, 77, 88, 99)
beginning, *middle, last = numbers
print(middle)
print(*numbers, *num)
# In Dictionary
dict1 = {"name":"Apple", "type":"Company"}
dict2 = {"name":"Zihan", "age":14, "hobby":"Programming"}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# || Unpacking List using * Asterisk ||
def print_num(a, b, c):
    print(a, b, c)
arr = [12, 24, 33]
py_dict = {"a":12 , "b":33, "c":32}
print_num(*arr)
print_num(**py_dict)

# || Generator consumes less memory it is used like list comprehensions, but with parenthesis () ||
import sys
my_generated_list = (num for num in range(10 ** 20) if num % 10 == 0)
print(sys.getsizeof(my_generated_list))
list_comp = [num for num in range(10 ** 5) if num % 10 == 0]
print(sys.getsizeof(list_comp))

# || Usage of "yield" - Generator ||
def first_n_gen(num):
    while num > 0:
        yield num
        num -= 1

print(list(first_n_gen(45)))

# || Decorator in Function ||
def print_decorator(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        result = func(*args, **kwargs)
        print("Bye!")
        return result
    return wrapper

@print_decorator
def total(a, b, c):
    print(f"The sum of all numbers is {a + b + c}")

total(3432, 43234, 33434)

# || JSON(JavaScript Object Notation) Module || 
import json
py_dict = {"name":"Zihan", "age":14, "country":"Bangladesh", "city":"Bogura", "prog.lang.":"Python"}
# Converting Python Dictionary to Json
json_dict = json.dumps(py_dict, indent = 4)
# Converting Json to Python Dictionary
reverse = json.loads(json_dict)
print(reverse)

# || Logging Module ||
import logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(name)s - %(levelname)s - %(massage)s", datefmt = "%d/%m/%Y %H:%M:%S")
logging.debug("This is a debug massage")
logging.info("This is a info massage")
logging.warning("This is a warning massage")
logging.error("This is a error massage")
logging.critical("This is a critical massage")

# || Item rotating using Deque ||
from collections import deque
queue = deque()
queue.appendleft(5)
queue.appendleft(4)
queue.appendleft(3)
queue.appendleft(2)
queue.appendleft(1)
queue.rotate(-1) # Rotates the Queue into reverse
print(queue)

# || Split Method ||
num = "4, 3, 2, 3, 4, 2"
arr = num.split(",")
print(arr)

# || We can create set of a list using forzenset method ||
a_set = frozenset([1, 2, 3, 4, 5, 6, 7, 8])
print(a_set)

# || Counting Number of Bytes ||
import sys
print(sys.getsizeof(10**30000), "Bytes")

# || Using "%" for String Formatting ||
print("Hello %s" % "World")

# || "pass" & "..." Both Statements are Same ||
class Student:
    pass
class Bag(Student):
    ...

# || Differences between 'f' string & "format" string ||
name = "Zihan"
age  = 15
hobby = "Programming"
print(f"This is {name} of {age} years old & His hobby is {hobby}") # Using 'f' string
print("This is {0} of {2} years old & His hobby is {1}".format(hobby, name, age)) # Using "format" string

# || Creating empty set ||
# a = {} #It is wrong way to create an empty set
a = set()
print(a)
print(type(a))

# || Using "Assert" - statement ||
def average(l):
    if not l:
        return None
    return sum(l) / len(l)

if __name__ == "__main__":
    li = [1, 2, 3, 4, 5]
    expected_result = 3
    assert expected_result == average(li), "Average() produced incorrect result!"

# || Set Hack no.01 ||
s = set()
s.add(20)
s.add(20.0) # It will be counted as repetative 
s.add('20')
print(s)
print("The lenght of the set is:-", len(s))

# || Set Hack no.02 ||
a_set = {18, '18'}
print(a_set)

# || In Loop, we can use exit() method to break loop ||
# while True:
n = int(input("Inter a positive number(0 to exit): "))
if n < 0:
    print("We only allow positive number. Please try again!")
    # continue
if n == 0:    
    exit("Ok Close!") # It replaces break & prints Ok CLose! 
print("Square of" , n , "is" , n * n)

# || Using global keyword ||
a = 50 # Global Variable
def function():
    global a # It changes the value of global variable
    a = 40   # Local variable
    print(f"Under function output:- {a}")

function()
print(a)

# || (end = ' ') - it prevents to print a new line ||
print("Zihan", end = ' ')
print("Zisan", end = ' ')
print("Zabir")

# || Dunder Method "__repr__" & special string ||
class Node:
    ''' An object for storing a single node of linked list '''
    data = None
    next_data = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data  # What's this!
