"""
    Head First Python chapter1 & chapter2
    
"""

movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])

# 2 eg
cast = ["Cleese", "palin", "jones", "Idle"]
print(cast)
print(len(cast))
print(cast[0])

# append pop extend
cast.append("Gilliam")
print(cast)
cast.pop()
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)

# remove insert
cast.remove("Cleese")
print(cast)
cast.insert(0, "Cleese")
print(cast)

# insert years into movies
years = [1975, 1979, 1983]
for i in range(len(movies)):
    movies.insert(2*i+1, years[i])
print(movies)

# 3 eg
fac_movies = ["The Holy Grail", "The Life of Brain"]
for each_flick in fac_movies:
    print(each_flick)

# 4 eg
movies = ["The Holy Grail", 1973, "Terry Jonnes & Terry gilliam", 91, ["graham chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jonne"]]]
for item in movies:
    if(isinstance(item, list)):
        print "true"

"""
Define a fonction to print the multiple-layer list
"""
def print_movies(movies, tab):
    for item in movies:
        if(isinstance(item, list)):
            print
            print ("\t" * tab),
            print_movies(item, tab+1)

        else:
            print (item),

print_movies(movies, 1)
