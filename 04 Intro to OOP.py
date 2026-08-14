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
    return sum(my_student['grades'])/ len(my_student['grades'])

# Calling the function
print(average(my_student)) # It yields 91.75

'''
Jose explained that there is a design flaw with the software. The function is disjointed with the data it 
working with even though it it closely 'coupled' with it in this case the dict. (I must admit that my understanding limited of what he explained).
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
2. The object name 'Student' starts with an upper class
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
# In the background python is running Student.average(student_one)
# Thus accessing the class, then the method, finally passing the object
# But, Object.method() already position 'student_one' as the self aurgument in the class structure
# Which means, we can add more parameters in the call, but will point to other properties in the object


# Test: Creating class for a movie dictionary
movie = {
    'name': 'Blackberry',
    'director': 'Matth Johnson'
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




