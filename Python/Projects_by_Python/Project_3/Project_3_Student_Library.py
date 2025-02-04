# || "Student Library" - Using Object Oriented Programming, Functions, Loops, Conditional Logic, File Handling, Exception Handling By Python ||

# A Global variable for storing & using list of book for name matching in "returnBook method" of Library Class
book_list = ["The Alchemist", "Computer Programming", "Python For Geeks", "Robust Python", "Java Programming", "Let Us C", "C++ in Depth", "Data Structures & Algorithms Through C", "Introduction To Algorithm", "Pro Git", 
"Play With Graphs", "Hines", "Mathematics For Machine Learning", "Python For Data Analysis", "Machine Learning Algorithm", "Graph Algorithm", "PHP Web Programming", "Word Press For Everybody", "Ubuntu For Everybody", "Programming Contest"]

# Creating a library class
class Library:
    '''Class Library For All Library Methods'''

    # Class Attribute to take the student name as an input 
    name = input("Q. Hello, Student! What is Your Name?\nAns:-")    

    # Class Attribute "listofbooks" to show the name of all books
    listofbooks = ["The Alchemist", "Computer Programming", "Python For Geeks", "Robust Python", "Java Programming", "Let Us C", "C++ in Depth", "Data Structures & Algorithms Through C", "Introduction To Algorithm", "Pro Git", 
    "Play With Graphs", "Hines", "Mathematics For Machine Learning", "Python For Data Analysis", "Machine Learning Algorithm", "Graph Algorithm", "PHP Web Programming", "Word Press For Everybody", "Ubuntu For Everybody", "Programming Contest"]

    # Method for showing the list of all books available in student library
    def showBooks(self):
        print(f"\n===== Explore Our Library =====\n|| List of All Books in Student Library ||")
        for index, books in enumerate(self.listofbooks):
            print(f"   {index + 1}. {books}")
    
    # Method for borrowing the books from this library
    def borrowBook(self, numofbook):
        self.numofbook = numofbook
        if numofbook <= len(self.listofbooks):
            the_book = self.listofbooks[numofbook - 1]
            self.listofbooks.remove(the_book)
            print(f'''Thanks, For Taking "{the_book}" From Our Library, {self.name}! Keep it Safely & Return it Before 30 Days!\n''')
        elif numofbook > len(self.listofbooks):
            print(f"Please, Check The list of Book Again {self.name} and Choose The Correct Number of Your Book!")

    # Method for returning the books in this library
    def returnBooks(self, nameofbook):
        self.nameofbook = nameofbook
        if nameofbook not in self.listofbooks:
            if nameofbook in book_list:
                self.listofbooks.append(nameofbook)
                print(f'''Thanks, For Returning "{nameofbook}", {self.name}! Hope You Enjoyed Reading This Book, Thanks a Lot for Using Student Library!''')
            else:
                print(f"Sorry, {self.name}! The Book have not Borrowed From Our Library!")
        else:
            print(f"Sorry, {self.name}! We have already a Book named {nameofbook}!")

# Creating a class named "Student" for object instantiation
class Student: 
    '''Student Class For Creating Student Object'''
    
    # Instantiating an object named "student"
    student = Library()
    
    # Loop for showing the options for the student's choice
    while True:
        print( f'''\n===== Welcome To Student Library =====
    How Can I help You, {Library.name}?
    1. Which Books are Available in Student Library?
    2. I want to borrow a book
    3. I want to return a book
    4. Thanks! Exit the Library
    ''')
    
        # "try" block for Exception Handling
        try:
            # Creating a variable to take the student's choice
            option = int(input("Enter Your Choice:- "))
            
            # Logics for methods calling, after choosing a number
            if option == 1:
                student.showBooks()
            elif option == 2:
                try:
                    book_num = int(input("Q. What is The Number of Book You Want to Borrow?\nAns:-"))
                    student.borrowBook(book_num)
                except Exception as e:
                    print(f"Please, Enter The Correct Book Number (Between 1 to 12) {Library.name}!")
            elif option == 3:
                book_name = input("Q. What is The Name of The Book You Want to Return?\nAns:-")
                student.returnBooks(book_name)
            elif option == 4:
                exit("Thanks For Using Student Library. Bye, See You Again in Student Library!")
            else:
                print("Invalid Choice!")

        except ValueError as e: # Handling Value Error
            print(f"Sorry, {Library.name}! Please, Enter a Choice between 1 to 4")