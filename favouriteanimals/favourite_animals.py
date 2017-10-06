# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them
import sys

def get_arguments():
        if len(sys.argv) > 1:
            return str(sys.argv[1:])
        return None

def command():
    if get_arguments() is None:
        print("```fav_animals [animal] [animal]```")
    else:
        animals = open("favourites.txt", "a")
        animals.write("\n" + get_arguments())
        animals.close()

get_arguments()
command()