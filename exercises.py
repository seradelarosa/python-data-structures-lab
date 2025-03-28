# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()

##################
##################

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students = ['Sera', 'Matt', 'Grey', 'Bel']
    first_student = students[1]
    # grab last value instead of hardcoding position
    last_student = students[-1]
    # need to return values!
    return first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

##################
##################

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # your code here
    # variable bc no trailing comma
    # append method only works on lists, but this is a string...
    meal = ''
    # tuple aka mutable parentheses
    foods = ('sushi', 'pizza', 'pho', 'twizzlers')

    for food in foods:
        # add a comma and space to format meal like a list
        meal += food + ', '
    
    # remove comma and space after the last string
    # meal.strip cannot remove commas...
    # use slice notation : to remove last two characters
    # meal[start:stop:step]
    return meal[:-2]

# Call the function and print the result
print('Exercise 2:', combine_foods())



