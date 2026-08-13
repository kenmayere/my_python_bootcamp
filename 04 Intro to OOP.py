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

# This has defined the structure of the object. A few things to note
# 1. The object is created using a 'class' key word
# 2. The object name 'Student' starts with an upper class

# Step 2: Creating the object >> This essentially means calling the object structure
student_one = Student()

# Here are a few points
# 1. student_one is the object that we have created using the object structure 'Student'
#     - I should think of objects as holding both data and actions
# 2. When it (Student) is created, it immediately calls the dunder init function which pass the self argument
# 3. This self argument creates a blank object, which eventually populates using the 'self.' for name and grades
