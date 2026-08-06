### ----------------------------------- A Movie Collection App ------------------------------------ ###

'''This is a milestone project, I will go over the brief, try it out and then follow through the solutions for evaluation'''

# I must admit that I really liked Jose's brief of the project because of its logic
# I learnt alot of how I need to break down problems with what I would call thinking in code or logic-code
# I will now highlight major steps and I will code my solution, making use of the provided hints as well

'''
First, I need user stories in the form of 'As a user, I would like to be able to.. '
    a. Add new movies to my collection; So I can keep track of all my movies
    b. List all the movies in my collection; So I can see what movies I already have
    c. Find a movie by using the movie title; So I can locate a specific movie easily when the collection grows

Implementation Tasks
    - Decide where to store the movies in code
    - Decide what data I want to store for each movie
    - Show the user a menu and let them pick an option
    - Implement each requirement in turn, each as a seperate function
    - Stop running the prog. when user type in 'q' in the menu

Breakdown:
    1. Where to store the movies: I will use a list, it was hinted as well to be easy to add more information
    2. What data to store: Title, director, year of release. This will be in a dict
    3. Show user a menu, get input and run a loop

'''

# --------------- Step 1 -------------------------------------
# Where to store the movies - I will create an empty movies list
movies = []

# --------------- Step 2 -------------------------------------
# I will need to populate this list with data (movie title, director, and release year)
# I need to use the input functiuon to allow users to add new movies to the collection
# For automation, let me wrap it in a function and a while loop

def new_movies():
    new = 'yes'
    while new == 'yes':
        title = input('Please Enter Title: ').title() # I would like to capitalize the first letters in the string of words
        director = input("Please Enter the Director's Name: ").title()
        year = int(input('Please Enter the Release Year: '))

        # Here I have created these variables to capture data about our movies

        # --------------- Step 3 -------------------------------------
        # I need to store the data in a dictionary and use the .append function to add new data in the list for every movie

        movies.append({
            'Title': title,
            'Director': director,
            'Year': year
        })
        add_new = input('Do you want to add a new movie (yes/no): ').lower()
        new = add_new

# --------------- Step 4 -------------------------------------
# Here I need to create functions to run listing all movies and searching


# Movies List
def movies_list():
    print('Here is the list of all movies in your library:')
    for movie_lib in movies:
        movie_name = movie_lib['Title']
        print(movie_name)

# Searching movie by title name
def search_movies():
    search = input('Please Enter the Title to Search: ')
    for x in movies:
        results = x['Title']
        if search == results:
            print(f'Match(es) Found: {search}')
            return
    print('No Matches Found')


# --------------- Step 5 -------------------------------------
# Creating a user menu
# Include functions to run in the loop
MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to list all movies, 's' to search for a movie by title, or 'q' to quit: "

selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        new_movies()
    if selection == 'l':
        movies_list()
    if selection == 's':
        search_movies()
    else:
        print('Unknown Command. Please Try Again')
    selection = input(MENU_PROMPT)


# ------------ Here below is the solution proposed by Jose ---------------

'''
This is the solution to the Movie Collection App as shown in the course.
After I tried developing the app, I am proud that my app in the above code works best. I however, have some issues with the output
on some functions. I will add comments of the issues and how similar functions were designed in the course project solution.

'''

# Jose started with the prompt and movie list variables

MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to list all movies, 's' to search for a movie by title, or 'q' to quit: "
movies = []

# As a next step, he created a function to add new movies
# For his implementation, he adds one movie at a time and loops back to the menu to repeat function
# In my implementation, I made it to take in more entries before you can exit back to the menu with a prompt
# I like my implementation, it makes it less repeatitive for the user.
# Additionally, in my implementation, I added type casting for year(int for now) and also string formatting options(.title) just to neat up

# Adding movies >>
def add_movies():
    title = input('Enter the Movie title: ')
    director = input('Enter the Movie Director: ')
    year = input('Enter the Movie Release Year: ')
    movies.append({
        'Title': title,
        'Director': director,
        'Release Year': year
    })


# He created the menu and wrap it in a function.
# I didnt have my menu as a function and to run it I had to highlight lines of code, which is not ideal
# I like Jose's, it makes having the menu options seamlessly easy
# He also used first class functions which is a great choice for the functions running different options

# Showing movies >>
def showing_movies():
    for movie in movies:
        print_movie(movie)
# For my listing, i failed to display all movies information, only the list of titles. I coudn't find a better way
# I like this, spliting the function into two functions.
def print_movie(movie):
    print(f"Title: {movie['Title']}")
    print(f"Director: {movie['Director']}")
    print(f"Release Year: {movie['Release Year']}")


# Searching movie >>
def find_movie():
    search_title = input('Enter Title of the Movie: ')
    for movie in movies:
        if movie['Title'] == search_title:
            print_movie(movie)
# Man! I love this implementation, so slick and effortless. How a function is reusable, superb! 


# Implementing the first class functions concept bu storing the functions in a dict
user_options = {'a': add_movies, 'l': showing_movies, 's': find_movie}


# With the options functions stored in a dict, he made his code more succinct unlike my long if statements
def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()

# Quit Simple! I must admit I have learnt a few things and I am also proud of what I did 😁

# Now time to run the app
menu()