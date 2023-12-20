print("================= Headline: Practice 03 ==================")

# ERROR
# IndentationError = happens when we put any unexpected space or TAB
# Syntax error = misspell of any syntax
# Name Error = when we declare a variable and call with a wrong name

# First the below code will take an input from user by asking "What's your name?:"
# Then it will take the name and print like below
# "Hello Name.Nice to meet you"
first_name = input("What's first your name?: \n")
print("Hello " + first_name + ".Nice to meet you")

# Stores the input name in "name" variable
last_name = input("What's your last name\n")
# Calculate the length of "name"
length_of_last_name = len(last_name)

# Print the name
print("The name is: " + first_name + " " + last_name)

# string and integer cannot be concatenated, so we convert the "length" variable into
# string and printed in console.
print('Length of the name: ' + str(length_of_last_name))