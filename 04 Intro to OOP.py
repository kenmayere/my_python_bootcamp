''' 
------------------- Intro to Object Oriented Programming --------------------
'''
# I start by creating a student library to contain name and a list of grades
my_student = {
'name': 'Rolf Smith',
'grades': [90, 88, 90, 99]
}

# Creating a function for calculating average
def average(student):
    return sum(student['grades'])/ len(student['grades'])


#  Calling the function
print(average(my_student)) # It yields 91.75

'''
Jose explained that there is a design flaw with the software. The function is disjointed with the data it is
working with even though it it closely 'coupled' with it, in this case the dict. (I must admit that my understanding maybe limited of what he explained).
It means that everytime the data changes, the function must change, for example, changing from 'grades' to 'results', which pose a problem if these
data and actions are not physically at the same place. The solution would be to include the function inside of the data dict,
for example, but unfortunately it is not possible. That's why the idea of OOP comes in.
'''

# Steps for OOP
# Step 1: Defining an Object

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    def average(self):
        return sum(self.grades)/len(self.grades)

''' ------------ A few points here: ----------------
1. The object is created using a 'class' key word
2. The class name 'Student' starts with an upper class
'''

# Step 2: Creating the object >> This essentially means calling the object structure
student_one = Student('Ken', [70, 80, 90, 99])
student_two = Student('Ford', [75, 80, 85, 99])

''' ------------ A few points here: ----------------

1. Student_one is the object that we have created using the object structure 'Student'
     - I should think of objects as holding both data and actions
2. When it (Student) is created, it immediately calls the dunder init function which pass the self argument
3. This self argument creates a blank object, which eventually populates using the 'self.' for name and grades
4. Now student_one and _two are objects that contain the data (name and grades passed to it).
    - These are called properties. Normally, they could have been called variables
2. The objects also have a function inside it. Functions inside a class are called Methods
    - The functions takes in an argument 'self' which is the now populated object
    - To call the function, it uses the syntax Object.Method_name()
'''
# Calling the method
print(student_one.average())
print(student_two.average())
# In the background python is running Student.average(student_one)
# Thus accessing the class, then the method, finally passing the object
# But, Object.method() already position 'student_one' as the self aurgument in the class structure
# Which means, we can add more parameters in the call, but will point to other properties in the object


# Test: Creating class for a movie dictionary
movie = {
    'name': 'Blackberry',
    'director': 'Matt Johnson'
}
# Creating a class to create a 'Movie' object
class Movie:
    def __init__(self, movie_name, movie_director):
        self.name = movie_name
        self.director = movie_director
    def print_info(self):
        print(f'<<{self.name}>> by {self.director}')

# Creating the Movie Object to contain the data in the movie dictionary
movie_object = Movie('Blackberry', 'Matt Johnson')
movie_object.print_info()

# In the Movie class, the dunder init function is not creating name or director variable in the self blank object
# It is creating a property in the self, thats why the syntanx self.parameter

# --------------------------- Magic Methods ------------------------------
# Hello new day, I proceed looking into magic methods (dunder functions)
# I will write code of all I wanted to discuss today just to save space and explain line by line as I go for this section.
class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]
    def __repr__(self):
        return f'<Garage {self.cars}>'
    def __str__(self):
        return f'Garage with {len(self)} cars'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars.__class__) # It shows me that my object is a list
print(len(ford)) # TypeError: object of type 'Garage' has no len(). This because it doesnt know what the len of the object will be.

# To go beyond this error, I created a dunder function to return len for the ford list object
# Calling it >> According to the way it is defined 
print(len(ford)) 

# Now given that, my ford object is a list. Can I just call any item by indexing.
# This is only possible, if I create another dunder function to access an item by index slicing. I created the __getitem__ function
print(ford[0])

# Using the getitem function unlocks the potential for a for-loop
# Why? The ford object is a list. However, created through a class definition will require special functions to access, hence I guess OOP.
# For the for-loop, now it runs because in the background, python runs the __getitem__ function and then iterate the object
for car in ford:
    print(car)

# In the class structure, there is the __repr__ . This is code oriented and recommended for debugging
print(repr(ford))

# Additionally, there is a line for a string function. This is user-facing
print(str(ford))

# -------------------- Exercise 1: Designing the architecture and inner methods of the Club class ---------------------------
# I now move to complete an exercise on dunder functions. I will tackle it by list of steps to complete
# Step 1: Creating a club class
# Step 2: Creating an instance (my_club)
# Step 3: Adding players to the object my_club
# Step 4: Accessing the i-th player in my_club
# Step 5: Return a string representation of the current object
# Step 6: Return a readable string to the user about this object

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
    def __len__(self):
        return len(self.players)    
    def __getitem__(self, i):
        return self.players[i] # Step 4
    def __repr__(self):
        return f'Club {self.name}: {self.players}' # Step 5 - This will allow me to use it on any club
    def __str__(self):
        return f'Club {self.name} has {len(self)} players' # Step 6

my_club = Club('Asernal') # Step 2
my_club.players.append('Rolf') # Step 3
my_club.players.append('Anne') # Step 3

print(my_club[0]) # Step 4 = Rolf
print(repr(my_club)) # Step 5 = Club Asernal: ['Rolf', 'Anne']
print(my_club) # Step 6 = Club Asernal with 2 players

# In the above code, I made some mistakes: I casted 'name' Asernal in the code. This locked my class object for multiple use
# I have made changes to the __repr__ and __str__ dunder functions to take in any arguments

# --------------------- Inheritance ----------------------
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks)

# The above class represent a Student, and it takes in name and school.
# I would like to create another class WorkingStudent with the only addition being salary parameter

# ------------ This is a class : WorkingStudent
# class WorkingStudent():
#     def __init__(self, name, school, salary):
#         self.name = name
#         self.school = school
#         self.salary = salary
#         self.marks = []
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#----------------
# In this class, I see alot of duplicates with the class Student
# I must inherit the parameters from Student as a parent class
# Inheritance is possible using the key work super() and then manually calling the __init__ ..,
# .. and specifiying the parameters/propertiers interested in.
# I will comment out the prev class constrution for a new one below

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    @property
    def weekly_salary(self):
        return self.salary * 40

# A few things to note: The WorkingStudent takes in the Student class as shown in parenthesis
# I have manually initilized the __init__ function using the super().__init__ to inherit parameters
# In this class, since it is a child of Student, it has inherited the average method as well
# And I can extend my class with other methods, for example, the weekly_salary.
# Inheritance works top to bottom and not viceversa
ken = WorkingStudent('Ken', 'Wits', 250)
ken.marks.append(85)
ken.marks.append(92)
ken.average()

'''
Property decorator: Usually methods are called using Object.method() syntax. But other methods, only takes in the self parameter,
and return a value. These can better be called using Object.method syntax. To do so in the above example, to call the weekly_salary,
I have added @property as a decorator to the class before defining the weekly_salary function
The @property is only useful when calculating values from the objects themselves. Otherwise, I need to use the traditional way
of calling object methods.
'''
ken.weekly_salary

# -------------------- 

# Hello World, I am now back to coding after a month long break! 
# I will be back soon! Apologies.

# -------------- Let me kick start with class and static methods

# Let me do so by creating a class as I have done multiple times
class AnotherStudent():
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks)

# Creating an object called mike
mike = AnotherStudent('mike', 'MIT')
mike.marks.append(90)
mike.marks.append(90)

mike.average()
# In the above class method call, it uses the object as an argument (=self) in the average method
# There are other ways to call a method: 1. Uses the class as first argument and another(2) takes in nothing
# Examples: Just highlighting the syntax

# ------- class method
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi() # Here the result will be Foo the class name
# Since, I have defined it as class method, the hi() takes in the class as its argument

# -------- static method
class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take in parameters' )

my_other_object = Bar() # Creating an object
my_other_object.hi()
# In the static method, it takes in nothing as its argument, the hi() method doesnt pass anything as an argument

# ------- more examples
# Let me create a class that will return a fixed amount of something, for example, currency
class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

# Creating an object using the class above
number = FixedFloat(18.5746)
print(number)

# If I want to extend the class to sum up two values I can add another function
# (I will be recreating the class and extend to show progress instead of modifiying an existing one above)

class FixedFloat_1:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    def from_sum(self, value_1, value_2):
        return FixedFloat(value_1 + value_2)

number_1 = FixedFloat_1(18.5746) # Creating an object from FixedFloat_1 cls
new_number = number_1.from_sum(19.575, 0.789)
print(new_number)
# But here I have not used number_1 object as value (18.5746).
# I can use @staticmethods to have the class as the argument in my from_sum method
# I will recreate the class and use @staticmethod and have the class not object whose values I may not use

class FixedFloat_2:
    def __init__(self, amount):
        self.amount = amount
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    @staticmethod
    def from_sum(value_1, value_2):
        return FixedFloat(value_1 + value_2)

new_mumber_1 = FixedFloat_2.from_sum(19.575, 0.789) # I am calling the from_sum method using the class
print(new_mumber_1)
# Here I dont need to create an object that I cannot use later on

# ----- Extendig further the class (FixedFloat_2) with currency parameters
class Dollar(FixedFloat_2):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'
    def __repr__(self):
        return f'<Dollar {self.symbol}{self.amount:.2f}>'

money = Dollar(18.789)
print(money)