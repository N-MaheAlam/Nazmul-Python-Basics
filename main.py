
print("================= DAY 01 =======================")
print("================= Practice 01 ==================")
print("STRING MANIPULATION: ")

print("Nazmul Mahe Alam")

# print the "print" in console
print("print('what to print')")

# Printing each name in new line
print("Nazmul\nMahe\nAlam \n Space")
print("================= Practice 02 ==================")
# Without any space
print("Hello" + "Kumu")

# Printing in single quote and give a space before "Kumu"
print('Hello' + ' Kumu')
print("================= Practice 03 ==================")

# ERROR
# IndentationError = happens when we put any unexpected space or TAB
# Syntax error = misspell of any syntax
# Name Error = when we declare a variable and call with a wrong name

# First the below code will take an input from user by asking "What's your name?: "
# Then it will take the name and print like below
# "Hello Name.Nice to meet you"
first_name = input("What's first your name?: \n")
print("Hello " + first_name + ".Nice to meet you")

# Stores the input name in "name" variable
last_name = input("What's your last name\n")
# Calculate the length of "name"
length_of_last_name = len(last_name)

# Print the name
print("The name is: " + first_name+" " + last_name)

# string and integer can not be concatenated, so we convert the "length" variable into
# string and printed in console.
print('Length of the name: ' + str(length_of_last_name))


print("================= DAY 02 =======================")


print("Data Types: \n")
print("================= int, string, float, boolean =======================")
age = 29
# integer type
print(age)

# Float
kilometers = 34.567
print(kilometers)

# Floating number with underscore to understand
saving_account = 234_34_54_495.98
# prints "34534556.79"
print(saving_account)

# boolean
is_he_here = True
print("Is He Here: " + str(is_he_here))

print("================= types of a variable =======================")
# a string
random_name = "Rabbi"
# "random_name" is a string type. It will print "str"
print(type(random_name))

# "random_number" is an integer type
random_number = 123
# It will print the data type of "random_float_number" which is int
print(type(random_number))


random_float_number = 456.044
# It will print the data type of "random_float_number" is float
print(type(random_float_number))


a_number_with_comma = 345_345_56.79
# It prints 34534556.79
print(a_number_with_comma)

# it is a string
new_price = "29"
price = "999"
old_price = 15
# prints "29999"
print("Total price is in string: " + new_price + price)

# Converting string into integer
new_price = int("29")
# 29 - 15 = 14
price_diff = new_price - old_price

# Convert 'price_diff' to a string before concatenating and prints 14
print("price difference is: " + str(price_diff))


