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
