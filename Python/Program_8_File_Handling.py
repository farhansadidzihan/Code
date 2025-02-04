# || File Handling in Python ||

# || Opening selected file in read mode to read ||
f = open("poems.txt")
print(f.read())
f.close()

# || Opening first one line from the file using readline method ||
f = open("poems.txt")
print(f.readline(), end = ' ')
print(f.readline(), end = ' ')
print(f.readline(), end = ' ')
print(f.readline(), end = ' ')
f.close()

# || Opening selected file in write mode to write (if anything is written write method wil overwrite that)||
f = open("python.txt", 'w') # if the file isn't exist this method will create a new file.
print(f.write("Python is an Interpreted Object Oriented Language using dynamic semantics.\nGuido van Rossum is the inventor of Python.\n"))
f.close()

# || Opening selected file in appending mode to append ||
f = open("python.txt", 'a')
print(f.write("In 1980, Guido van Rossum started to create Python.\nThe name was taken from a circus name, called \"Monty Python Circus.\""))
f.close()

# || Opening selected file in appending mode with "with statement" ||
with open("poems.txt", 'a') as f:
    a = f.write("\nThis is 'Twinkle' poem.")
print(a)