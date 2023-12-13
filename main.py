print("STRING MANIPULATION: ")

print("Nazmul Mahe Alam")

# print the "print" in console
print("print('what to print')")

# Printing each name in new line
print("Nazmul\nMahe\nAlam \n Space")
print("=================01================")
# Without any space
print("Hello" + "Kumu")

# Printing in single quote and give a space before "Kumu"
print('Hello' + ' Kumu')
print("=================02================")

# ERROR
# IndentationError = happens when we put any unexpected space or TAB
# Syntax error = misspell of any syntax

# First the below code will take an input from user by asking "What's your name?: "
# Then it will take the name and print like below
# "Hello Name.Nice to meet you"
print("Hello " + input("What's your name?: ") + ".Nice to meet you")

name = input("What's your last name")
length = len(name)
print("The name is: " + name)
print('Length of the name: ' + str(length))



