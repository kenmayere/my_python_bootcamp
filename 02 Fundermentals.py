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
    
''' Agin here, the for loop create a variable 'results' and assign it the first value in the list which is 
a dictionary, then we assign the first value in the dict with a key called name to 'name' variable,
similary grade to 'grade' variable using the key grade. For each iteration, the print function is running'''

# Now let's talk about destructuring syntax

# Here is an example: Suppose I have a tuple of currencies
currencies = 0.8, 1.2
usd, eur = currencies # Here I have assigned first element in the tuple to usd and the other to eur
# This is called destructuring
# A more concrete example

players = [('Rolf', 25), ('Anne', 37), ('Charlie', 31), ('Bob', 22)] # A list of tuples with name and points.

# To print out the elements, I can use a for loop:
for player in players:
    print(player)
# But it will just print out the tuples, to make it more intuitive, I can destricture it:

for name, points in players:
    print(f'{name} has {points} points this season')

# What about iterating over a dictionary
# Suppose the player plus points data was a dict

player_points = dict(players) # Here I have converted the list to a dict with the tuples as key:value pairs

for player in player_points:
    print(player)
# Here I will only get a print out of all the keys which are the names of the players in this case
# But if I want to print out the values which are the player points in this case;
for points in player_points.values():
    print(points)
# But I want to make it more intuitive and print out both key and value
for name, points in player_points.items():
    print(f'{name} has {points} points this season')

# Hello new day, let's continuw with break and continue keyword
# These are useful in loops

# Example: Suppose I have a list of car production status

cars = ['OK', 'OK', 'OK', 'Faulty', 'OK', 'OK']
for status in cars:
    print(f'This car is {status}')

# For my imaginary production line, once a car is faulty I stop the production
# Here I use the break key word

for status in cars:
    if status == 'Faulty':
        print('This car is faulty, stop the production')
        break
    print(f'This car is {status}')
    print('Shipping the new car to the customer')

# This code will break once the if statement evaluates to true.
# But I have two more cars remaining in the list, I only need to skip the faulty
# The continue key word is useful in this case as it will skip the element meeting the if condition and continue with the rest.

for status in cars:
    if status == 'Faulty':
        print('Faulty car detected. Skip shipping')
        continue
    print(f'This car is {status}')
    print('Shipping this new car to the customer')

# Good day, I now explore else key word in loops.
# I will use the previous example of the cars list.
# With the break key word, it will stop the iteration when it encounters the faulty
# Now to add a line to the parent for loop, we can use else key word, this runs if the branch runs successfully
# For example, there are no breaks or errors. So I will change the faulty car status to OK
cars = ['OK', 'OK', 'OK', 'OK', 'OK', 'OK']
for status in cars:
    if status == 'Faulty':
        print('Faulty car detected. Skip shipping')
        break
    print(f'This car is {status}')
    print('Shipping this new car to the customer')
else:
    print('Shipping successful. No faulty cars')

# Now let me try finding prime numbers, a classic coding hand-ons exercise
# A prime number is one that is divisible by 1 and itself
# Let me find prime numbers in the range of 2-10
for n in range(2, 10): # 10 is exclusive
    for x in range(2, n): # Here we develop a list of numbers below n
        if n % x == 0:
            print(f'{n} is equal to {x} * {n//x}')
            break # The break will apply for the inside for loop if the condition is met, but the outside will continue to iterate
    else:
        print(f'{n} is a prime number')

# List slicing: process of getting a part of the list or other iterable
friends = ['JD','Frank','Davie','Bule','MacD']
print(friends[2:4]) # Here it will display item on first index specified and end on the second index -1 
# ['Davie', 'Bule']
# There many ways like [:], [1:], [:3], [-3:2], [-1:-3] for various things..,

# Good day, now let's talk about list comprehensions
# This allows the creation of new lists succinctly and in a powerful way
number = [1, 2, 3, 4, 5]
# If I want to create a new list of numbers doubled from the list I can do the following
double_number = []
for number in number:
    double_number.append(number * 2)

# But with list comprehensions, I can produce the same in a more succinct and powerful way
double_number = [x * 2 for x in number]
# Here is another example
friends_ages = [23, 24, 25, 26, 24]
age_string = [f'My friend is {k} years old' for k in friends_ages] # A list of strings

# Another example
names = ['Rolf', 'Bob', 'Jen']
lower = [k.lower() for k in names]

# Another example: Reusing the friends variable
friend = input("Please enter your friend's: ")
friends = ['JD','Frank','Davie','Bule','MacD']
# I need to create another list to convert the input into lower cases for easy comparison
friends_lower = [k.lower() for k in friends]
# And I need to convert the input into lowercase and compare it against the lowercase list that I have created above
# I can also do title casing on the output for that regardless of how input is made, it capitalize first letter only

if friend.lower() in friends_lower:
    print(f'{friend.title()} is one of your friends') # Used title casing

# Let me try list comprehensions with conditionals
gents = ['JD','Frank','Davie','Bule','MacD']
practice = ['davie', 'MacD', 'FRANK', 'Ken', 'Fai', 'MissT']
# I would like to print a list of friends that showed up for practice
gents_lower = [g.lower() for g in gents]
present = [
    p.title() for p in practice
    if p.lower() in gents_lower
]
print(present)

# Hello new day
# Now we move to set and dictionary comphrehension
# From the previous example, I can create a set for each list

lower_gents = set([n.lower() for n in gents])
lower_practice = set([n.lower() for n in practice])
print(lower_gents.intersection(lower_practice))

# But I can also directly create a set using curry brackets
gents_lower2 = {n.lower() for n in gents}
practice_lower2 = {n.lower() for n in practice}
present_members = {name.title() for name in gents_lower2.intersection(practice_lower2)}
# I could have also created a variable
# present_set = gents_lower2.intersection(practice_lower2), then create a set with comprehensions
# Like: present_members = {name.title() for name in present_set}
print(present_members)

# Now lets looks at dictionary comprehension using the following example
members = ['Davie', 'Frank', 'Bule', 'JD']
days_last_seen = [3, 12, 2, 2]

# I can create a disctionary using comphrehensions like
time_count = {
    members[i]:days_last_seen[i]
    for i in range(len(members))
}
# I can now iterate over the dictionary
for members, days_last_seen in time_count.items():
    print(f'About {days_last_seen} days have passed since I last met {members}')

# There is a shorter way of creating a dictionary and that is using the dict function
# But from the two lists I need to combine the elements into tuples, for example, ('Davie', 3)('Frank', 12) etc
# I can do that through the zip function and parse a dict function
zipped = dict(zip(members, days_last_seen))
print(zipped)

# Good day
# Let's start with the enumerate function
classmates = ['Theo', 'Likhwa', 'Ken', 'Khumbz', 'Thymon']
# I want to print out all these but starting with a number like 0, 1, 2, 3 etc
counter = 0
for counter, classmate in enumerate(classmates):
    print(counter)
    print(classmate)

# If I want to make a list of each number and element
print(list(enumerate(classmates)))
# Or a dict
print(dict(enumerate(classmates, start=1))) # The count will start at 1

# Now let me explore functions
# Functions are defined by the def key word followed by an indented block of code, for example
def greet():
    name = input('Please Enter your name: ').title()
    print(f'Hello {name}')
# Above, greet is the name of the function and its only defined, it wont run the block of code until its called
greet()

# Hello new day: Let's talk about arguments and parameters
# These are useful in functions as they make functions to be reusable with multiple data
# Example:
def calculate_mpg():
    sports_car = {
        'make': 'Ford',
        'model': 'Fiesta',
        'mileage': 23000,
        'fuel_consumed': 460
    }
    mpg = sports_car['mileage']/sports_car['fuel_consumed']
    name = f'{sports_car['make']} {sports_car["model"]}'
    print(f'{name} does {mpg} miles per gallon')
calculate_mpg() # Calling the function

# Here the function is limited because I can not resuse it with other data
# I need to use define a parameter and use arguments
# Arguments: Data passed in a function call, parameter: variable that accepts/receives the value of an argument
# Syntax: def function(parameter), function_call(argument)
# I will create a function that I can reuse with multiple data/values: List of cars

sport_cars = [
    {'make':'Ford', 'model':'Fiesta', 'mileage':23000, 'fuel_consumed':460},
    {'make':'Ford', 'model':'Focus', 'mileage':17000, 'fuel_consumed':360},
    {'make':'Mazda', 'model':'MX5', 'mileage':49000, 'fuel_consumed':900},
    {'make':'Cooper', 'model':'Mini', 'mileage':31000, 'fuel_consumed':235}
]

def calculate_car_mpg(car_to_calculate):
    car_mpg = car_to_calculate['mileage']//car_to_calculate['fuel_consumed']
    car_name = f'{car_to_calculate['make']} {car_to_calculate['model']}'
    print(f'{car_name} does {car_mpg} miles per gallon.')

# Calling the function for the any car, for example the Mazda
calculate_car_mpg(sport_cars[2])
# Calling the function for all the cars in the list I can use a for loop
for car_to_calculate in sport_cars:
    calculate_car_mpg(car_to_calculate)

# Let me explore default parameters and named arguments
def add(x,y):
    total = x + y
    return total
print(add(3,4))
# I can create a default value for example y=5 in the def, this will become a default parameter
# Or I can do x=10, y=7 in the function call, these become named arguments
def subtract(x, y=5):
    total = x-y
    return total
print(subtract(10))
