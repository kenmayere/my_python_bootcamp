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
'''If I have for examplee, an integer, and I would like to join it with a string without
casting or changing the data structure, I can use f-strings'''

price = 1000
print(f'The price for the laptop is {price} dollars')

'''However, the limitation with f-strings is that I cannot reuse them when the value
of the variable changes, for example'''

price = 2000
print(f'The new price of the laptop is {price} dollars') # Oh it has worked

# Let me try something called nesting

'''Suppose I would like to have a dynamic program,
for example, I ask users their input'''

user_input = input('What is your age: ') # I enter 3 for example
print(f'You have lived for {user_input * 12} months') # Here it will concatenate the 3's 12 times

''' If I want to perform mathematical operations
I need to cast the user input as an integer. I can do that under the same line by nesting'''

user_input = int(input('What is your age: ')) # I have nested two functions, int and input
print(f'You have lived for {user_input * 365 * 24 * 60 * 60} seconds on earth')

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
user_name = name or default_greeting # The or will stop at the first value if its true, so precedence matters!
print(f'Hello, {user_name}!')

# Let's talk about lists: These allow multiple values to be stored in a single variable

sibs = ['Ken', 'Yammie', 'Mpha']
print(sibs[0]) # Will give the first value in the list which is ken, this is called indexing

# I can have a list containing lists

birth_month = [['Ken', 'Dec'], ['Yammie', 'Oct'], ['Mpha', 'Sept']]

# the birth_month list will consider the sublists as value
# list functions include append and remove etc

# OK lets try now tuples: Similar to lists but do have a subtle difference

''' Lists are defined ny square brackets, with tuples you do not need brackets
However, it is best practice to wrap tuples in round brackets'''

tuple_example = 'Ken', 'Yammie', 'Mpha'
print(type(tuple_example)) # <class 'tuple'>

another_tuple = ('Ken', 'Yammie', 'Mpha')
print(type(another_tuple)) # <class 'tuple'>

# The major difference with lists is that why lists can be altered (add/remove), tuples do not change

# tuple_example.append('Amina') # Will result into AttributeError: 'tuple' object has no attribute 'append'

# I can only join a tuple to a tuple

tuple_example = tuple_example + ('Amina',)
print(tuple_example) # It will result into ('Ken', 'Yammie', 'Mpha', 'Amina')


# Sets: Similar to tuples and lists but slightly different
# Sets do not contain any order and duplicates
# They are defined using curly braces

randon_num = {20, 34, 56, 9, 17}
print(randon_num) # {17, 34, 20, 56, 9}
