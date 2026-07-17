''' This follows the introduction section of the python bootcamp'''

# If statements

''' These by definition evaluates a bool and run a block of code if its true basically'''

name = 'Rolf'
user_name = input('Please enter your name: ')

if user_name == name:
    print('Hello friend!')

''' Let's discuss the syntax:
1. the if key word - this defines the statement
2. the if is followed by a boolean/condition and a colon
3. then a block of code to run if the boolean evaluates to true
But if the condition is not true then there's another key word
5. the else followed by a colon, code under this key word will run if the condition is not true
'''
# For example

if user_name == name:
    print(f'Hello {name}!')
else:
    print('Hello there!')

# Now suppose I want to get a name either in the friend or family variable as below

friends = ['JD','Frank','Davie','Bule','MacD']
family = ['Ken','Yammie','Mphatso']

# Now since I will check IN the lists, I will check the condition using in key word

if user_name in friends:
    print('Hello friend!')

# Same can be done for the family,  but I can also chain the conditions using elif key word

if user_name in friends:
    print('Hello friend')
elif user_name in family:
    print('Hello fam')
else:
    print('Hello there!')

# Great stuff, lets now talk about loops - While loops
# Loops let us do something repeatedly

is_learning = True

while is_learning:
    print('I am learning')
    user_input = input('Are you learning? (yes/no) ')
    is_learning = user_input == 'yes'
    print('I have stopped learning')

# Let's now look at for loops
''' These are used when I want to repeat something a definate number of time and or
I want to use a value of each of an iterable (tuple, list, dict or set) to do something'''

# For example
for friend in friends:
    print(friend)
''' Here it will print each element in the friend list one after the other.
When the loop is running, it will create a variable 'friend' and assign it an element fromn the friends list,
it will then print that variable, then it will repeat the process by creating a new variable with a new element'''

students = [
    {'name':'JD', 'grade': 85},
    {'name':'Frank', 'grade':90},
    {'name':'Davie', 'grade':95},
    {'name':'Bule', 'grade':100}
]
for results in students:
    name = results['name']
    grade = results['grade']
    print(f'{name} has got {grade} marks')
    
''' Agin here, the for loop create a variable results and assign it the first value in the list which is 
a dictionary, then we assign the first value in the dict with a key called name to name variable,
similary grade to grade variable using the key grade. For each iteration, the print function is running'''