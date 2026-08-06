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