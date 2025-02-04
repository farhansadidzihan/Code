# || Join Method in List || In-Built Data Structure[list] ||
z  = ['a' , 'b' , 'c' , 'd' , 'e' , 'f', 'h' , 'i' , 'j' , 'k']
a = " " .join(z)  # Used to get list's items as string 
print(a)

# || Using "max" mathod ||
li = [95, 88, 80, 98, 93, 100]
print(max(li))

# || Using "map" Mathod ||
li = [1, 2, 3, 4, 5, 6, 7]
def square(n):  
    return n ** 2
print(list(map(square, li))) # map also can be used with lambda function 

# || Using "filter" Mathod ||
greater = lambda n : n % 2 == 0
li = [1, 2, 3, 4, 5 , 6, 7, 8, 9, 10] 
print(list(filter(greater, li))) # For which the Function is True 

# || Using "Reduce" Mathod ||
from functools import reduce
li = [1, 2, 3, 4, 5]
factorial = lambda a, b : a * b
print(reduce(factorial, li)) 

# || List index ||
marks = [91 , 86 , 81 , 83 , 91 , 84]
print(marks[-1])
print(marks[0:4])

# || Methods in List ||
marks = [91 , 86 , 81]
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

# || Using list Comprehension ||
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [n for n in list1 if n % 2 == 0]
print(list2)

# || Methods in List || Example no.1 ||
li = [1 , 2 , 3 , 4]
new_li = []
for x in li:
    new_li.append(2 * x)

print(new_li)

# || With List Comprehensions || Example no.1 ||
li = [1 , 2 , 3 , 4]
new_li = [2 * x for x in li]
print(new_li)

# || Methods in List || Example no.2 ||
li   = [1 , 2 , 3 , 4 , 5 ]
list = []
for x in li:
    if x % 2 == 0:
        list.append(x)

print(list)
# || With List Comprehensions || Example no.2 ||
list = [x for x in range(1 , 5) if x % 2 == 0]
print(list)

# || Tuple unpack || Data Structure ||
x = (1 , 2 , 3 , 4)
x1 , x2 , x3 , x4 = x
print(x1 , x2 , x3 , x4)

# || All Data Types & Structures ||
items = (1, 'Zihan', 5.5, ['a', 'b', 'c'], ('apple', 'banana', 'mango'), {'Mobile', 'Laptop' , 'Notebook'})
for item in items:
    print(item, type(items))
    
# || Set || Data Structure ||
Phone  = {'Display', 'Touch Screen', 'Fingerprint Sensor', 'Motherboard', 'Processor', 'Ports', 'Camera', 'Charger', 'Battery'}
Laptop = {'Display', 'Keyboard', 'Touch Pad', 'Motherboard', 'Processor', 'Ports', 'Camera', 'Charger', 'Battery'}
print("Total items are :-", Phone | Laptop)  # "Phone union Laptop"  
print("Items that are common in both :-", Phone & Laptop)  # "Phone intersection Laptop"
print("Items that are uncommon in both :-", Phone ^ Laptop)  # "Phone disjoint Laptop"
print("Items that are only in Laptop is :-", Laptop - Phone) # "Laptop minus Phone"
print("Items that are only in Phone is :-", Phone - Laptop)  # "Phone minus Laptop"

# || Dictionary || Data Structure ||
marks = {"Bangla" : 91 , "English" : 86 , "Math" : 81 , "BGS" : 83 , "Science" : 91}
print(marks["Math"])
marks["Islam"] = 84
print(marks)

# || Dictionary Methods || Data Structure ||
my_dreams = {
    "Honest" : '''To be an honest & good.''',
    #"Topper" : '''To be topper in class.''',
"Great_Coder": '''To be a great programmer.''',
"Industrial" : '''To wark harder & more harder.''',
   "Handsome": '''To be the most handsome person in the world.'''
}
# print(my_dreams.keys())  # Prints the keys of the dictionary
# print(my_dreams.values()) # Prints the value of the dictionary
# print(my_dreams.items())  # Prints the tuple (key, value) of the dictionary
# print(my_dreams["abc"]) # This will return error 
# print(my_dreams.get("abc")) #But, This will return none
dream_update = {
    "Topper" : '''To be topper in class.'''
}
my_dreams.update(dream_update)
print(my_dreams)

# List Comprehensions
li = [1, 2, 3, 4]
square_num = [i * i for i in li]
print(square_num)