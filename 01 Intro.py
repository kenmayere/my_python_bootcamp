# Variables

# Example
age = 30 # integer
countries_visited = 90 # snake_case
gender = 'male' # string

PI = 3.14159 # Constants are in capitals

# Numbers: Integers and float point numbers (floats)

integer = 30
float = 2.5

# mathematical operations

maths_ops = 1 + 2 * 6 / 2 - 2 # It will follow math rules, example, BODMAS
print(maths_ops)

# Division

float_division = 8 / 2 # It will result in a float (4.0) even though in essence its a whole number
print(float_division)

integer_division = 8 // 2 # It will result in an integer (4)
print(integer_division)

# Strings

name = 'Kenford'

# Commenting: I can comment with # symbol for a single line OR

''' I can write text as a multiline, either assigned to string variable or as a comment, see below
It continues here
and HERE..,
'''
multi_line_string = '''Hello a 
multiline
'''
print(multi_line_string)

# If I want to display a string with quotes, I can use single and double quotes or I can escape

string_with_quotes = 'He said "I will go" '
print(string_with_quotes) # OR escaping below

another_string_with_quotes = 'He said \'I will go\'' # The backslash escape the quotes characters/remove meaning
print(another_string_with_quotes)
let_me_try = 'I am trying it again with this word in quotes \'Try\''
print(let_me_try) # I can now use this syntax \' text \' to escape characters.

# Finally I can join string characters using '+' sign

name = 'Kenford'
greeting = 'Hello ' + name
print(greeting)

# But if I want to join a string character and an integer, I need to cast the integer into a string
height_int = 1.78
height_str = '1.78' # OR
height_casted = str(1.78)

print('Your height = ' + height_casted)

# String formatting
'''If I have for example, an integer, and I would like to join it with a string without
casting or changing the data structure, I can use f-strings'''

price = 1000
print(f'The price for the laptop is {price} dollars')
# It is important to note the format which is: f'text1{integer}text2..,'

# Another example:
shoe_size = 7
print(f'Please get me size {shoe_size} of any color')

'''However, the limitation with f-strings is that I cannot reuse them when the value
of the variable changes, for example'''

price = 4000
print(f'The new price of the laptop is {price} dollars') # Oh it has worked

# Let me try something called nesting

'''Suppose I would like to have a dynamic program,
for example, I ask users their input'''

user_input = input('What is your age: ') # I enter 3 for example
print(f'You have lived for {user_input * 12} months') # Here it will concatenate the 3's 12 times
print(type(user_input)) # If I try to check the type: <class 'str'> thats why it concatenate

''' If I want to perform mathematical operations
I need to cast the user input as an integer. I can do that under the same line by nesting'''

user_input = int(input('What is your age: ')) # I have nested two functions, int and input
print(f'You have lived for {user_input * 365 * 24 * 60 * 60} seconds on earth')
print(type(user_input)) # Here it gives <class 'int'> because I casted it to int in the nested function

# Working with booleans
# They evaluate to True or False using comparison operators (==, >=, <=, =!)

magic_num = 5
user_num = int(input('Please guess any number between 0-10: '))
match = user_num == magic_num
print(f'We do have a match? {match}') # It will evaluate to True or False if the number matches

# The 'and' & 'or' key word
'''and looks for True in both values to evaluate to True while or looks for True in either values
to evaluate to True, for example;
True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False'''

default_age = 30 # If I parse this as a bool it will result into True, because is non-zero and non-empty
age = 0 # If I parse this as a bool it will result into False, because it is zero (similary empty values)
user_age = age or default_age # age = 0 will result into false, therefore, the default age to True
print(user_age) # Will result into 30 which is true

default_greeting = 'there'
name = input('Enter your name (Optional): ')
user_name = name or default_greeting # The 'or' will stop at the first value if its true, so precedence matters!
print(f'Hello, {user_name}!')

# Let's talk about lists: These allow multiple values to be stored in a single variable

sibs = ['Ken', 'Yammie', 'Mpha']
print(sibs[0]) # Will give the first value in the list which is ken, this is called indexing

# I can have a list containing lists

birth_month = [['Ken', 'Dec'], ['Yammie', 'Oct'], ['Mpha', 'Sept']]

# the birth_month list will consider the sublists as value
# list functions include append and remove etc

# OK lets try now tuples: Similar to lists but do have a subtle difference

''' Lists are defined by square brackets, with tuples you do not need brackets
However, it is best practice to wrap tuples in round brackets'''

tuple_example = 'Ken', 'Yammie', 'Mpha'
print(type(tuple_example)) # Here the result will be <class 'tuple'>

another_tuple = ('Ken', 'Yammie', 'Mpha')
print(type(another_tuple)) # <class 'tuple'>

''' Can I then access elements in a tuple the way I would with a list?
Lets try!
'''
print(tuple_example[0]) # Yes it works

# The major difference with lists is that lists can be altered (add/remove), tuples do not change

# tuple_example.append('Amina') # Will result into AttributeError: 'tuple' object has no attribute 'append'

# I can only join a tuple to a tuple

tuple_example = tuple_example + ('Amina',) # Here it is important to note the added sep (,) to make it work
print(tuple_example) # It will result into ('Ken', 'Yammie', 'Mpha', 'Amina')


# Sets: Similar to tuples and lists but slightly different
# Sets do not contain any order and do not allow any duplicates
# They are defined using curly braces

randon_num = {20, 34, 56, 9, 17}
print(randon_num) # {17, 34, 20, 56, 9}

# Can I add to a set, let me try
randon_num.add(23)
print(randon_num) # It has worked

# Do sets contain strings, lets see:
string_set = {'Kenford','Yammie','Mphatso','Amina'}
print(string_set) # It works perfectly

# What about set methods, let me try the common methods. add/remove/append

string_set.add('Lai')
print(string_set)

# Let me pop
string_set.pop() # It will delete the first element at any given time
print(string_set)

# But why are sets important over tuples and lists
'''With sets I can perform advanced functions
for example:
    difference = elements that are in one set but not in another
    symmetric difference = elements that are not in both
    intersection = elements that are in both
    union = one long set without duplicates
'''

# For example
saprono = {'Eluphy','Tio','Love','Tindi','Fai','Aggie'}
alto = {'Aggie','Thembi','Yammie','Fai','Tindi'}

not_saprono = alto.difference(saprono) # Elements in alto that are not in sap
print(not_saprono)
not_alto = saprono.difference(alto) # Elements in sap but not in alto
print(not_alto)

one_voice = saprono.symmetric_difference(alto) # Elements that are only in sap
print(one_voice)

sap_or_alto = saprono.intersection(alto) # Elements appearing in both
print(sap_or_alto)

print(saprono.union(alto)) # One set without duplicates

'''Dictionary'''

'''It allows one to store key:value pairs
These are wrapped inside curly braces
You can assign a value by defining a key or change a value of a key to an existing key'''

dict_one = {'name':'Ken', 'voice':'Tenor'}
print(dict_one['name']) # Calling out a value by the key

# What is I want to store such information for a group: I can create a tuple of dictionaries

mds = ({'name':'Ken', 'voice':'Tenor'}, {'name':'JD', 'voice':'Tenor'})
print(mds)

# Let me try indentation

other_members = (
    {'name': 'Eluphy', 'voice': 'Sap'},
    {'name': 'Tio', 'voice': 'Sap'},
    {'name': 'Fai', 'voice': 'Sap'},
    {'name': 'Love', 'voice': 'Sap'}
) # running this block needs selection
print(other_members)