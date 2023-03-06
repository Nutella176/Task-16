# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "lion" #Syntax Error: quatation marks missing, also may want to make this lower case 
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" #Logical Error: although no error pops up, it doesn't produce the desired output.
#it's an f-string so f is missing. Also number_of_teeth and animal_type need swapping. 

print(full_spec) #Syntax Error: missing parentheses

