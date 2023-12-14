#  create a small python project in your IDE, Take each block of code based on
#  "Headline:" and run in "main.py" of that project, you can understand easily how
#  each line of code is working.
print("================= Headline: DAY 01 =======================")
print("================= Headline: Practice 01 ==================")
print("Headline: STRING MANIPULATION: ")

print("Nazmul Mahe Alam")

# print the "print" in console
print("print('what to print')")

# Printing each name in new line
print("Nazmul\nMahe\nAlam \n Space")
print("================= Headline: Practice 02 ==================")
# Without any space
print("Hello" + "Kumu")

# Printing in single quote and give a space before "Kumu"
print('Hello' + ' Kumu')
print("================= Headline: Practice 03 ==================")

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
print("The name is: " + first_name + " " + last_name)

# string and integer can not be concatenated, so we convert the "length" variable into
# string and printed in console.
print('Length of the name: ' + str(length_of_last_name))

print("================= Headline: DAY 02 =======================")

print("Data Types: \n")
print("================= Headline: int, string, float, boolean =======================")
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

print("================= Headline: types of a variable =======================")
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

print("================= Headline: Mathematical Operations =======================")

# Addition
print(3 + 2)

# Subtraction
print(3 - 2)

# Multiplication
print(3 * 2)

# Double Asters
print(3 ** 2)

# Any mathematics flow the below rules
# PEMDAS =  Parentheses (), Exponents **, Multiplication *, Division /, Addition + , Subtraction -


print("========  Insert a 2 digit Number &  calculate their addition =========")

# Input a number as a string
two_digit_number = input()

# collect the index 0  such if input is 54, it will collect 5
first_digit = two_digit_number[0]

# collect the index 1  such if input is 54, it will collect 4
second_digit = two_digit_number[1]

# Convert first_digit string into integer
convert_into_int_first_digit = int(first_digit)

# Convert second_digit string into integer
convert_into_int_second_digit = int(second_digit)

# Add these two number and prit in console which is suppose 9 (5+4)
print(convert_into_int_first_digit + convert_into_int_second_digit)

######## Body Mass Calculator ##################

height = input()
weight = input()
# Convert height String into float number
height_as_float = float(height)
# Convert weight String into integer
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2

# If the bmi in case comes as a float, convert it into integer
bmi_as_int = int(bmi)
# print in console
print(bmi_as_int)

print("========== Headline: Short Forms of Mathematical Operation ==========")

score = 10
# score = score +1
score += 1
# prints 11
print(score)

age = 29
age -= 9
print(age)

hourly_rate = 20 / 3
# print with decimal point
print(hourly_rate)
hourly_rate = round(20 / 3)
# prints the closed integer number, 6.666666667 = 7, it prints 7
print(hourly_rate)

hourly_rate = round(20 / 3, 2)
# It prints till 2 decimal point
print(hourly_rate)
# it will store only the integer after division, not the decimal point as we have given "//"
# it will store the nearest small integer such 20/3 = 6.666667, it stores 6 , not 7
hourly_rate = 20 // 3
print(hourly_rate)

print("================== Headline: F-String ==================")

score = 10
age = 29
isGoing = True

# we have written code where converted any variable such as int, float into string
# "str(variable_name) then print in the console but using "f-string" we can print
# any sort of variables in below format
# OUTPUT: The Score is: 10, His/Her age is 29, Is going: True
print(f"The Score is: {score}, His/Her age is {age}, Is going: {isGoing}")
