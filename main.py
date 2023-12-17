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

# Printing in a single quote and give a space before "Kumu"
print('Hello' + ' Kumu')
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

print("================= Headline: DAY 02  =======================")

print("Data Types: \n")
print("================= Headline: int, string, float, boolean : Practice 04 =======================")
age = 29
# integer type
print(age)

# Float
kilometers = 34.567
print(kilometers)

# Floating number with underscore to understand
saving_account = 234_34_54_495.98
# prints "2343454495.98"
print(saving_account)

# boolean
is_he_here = True
print("Is He Here: " + str(is_he_here))

print("================= Headline: types of a variable: Practice 05 =======================")
# a string
random_name = "Rabbi"
# "Random_name" is a string type. It will print "str"
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

print("================= Headline: Mathematical Operations: Practice 06 =======================")

# Addition
print(3 + 2)

# Subtraction
print(3 - 2)

# Multiplication
print(3 * 2)

# Double Asters
print(3 ** 2)

# Any mathematics flow the below rules
# PEMDAS = Parentheses (), Exponents **, Multiplication *, Division /, Addition + , Subtraction -


print("========  Insert a 2 digit Number &  calculate their addition: Practice 07 =========")

# Input a number as a string
two_digit_number = input()

# collect index 0 such if input is 54, it will collect 5
first_digit = two_digit_number[0]

# collect index 1 such if input is 54, it will collect 4
second_digit = two_digit_number[1]

# Convert first_digit string into integer
convert_into_int_first_digit = int(first_digit)

# Convert second_digit string into integer
convert_into_int_second_digit = int(second_digit)

# Add these two numbers and print in console which is supposed 9 (5+4)
print(convert_into_int_first_digit + convert_into_int_second_digit)

print("=============  Body Mass Calculator ==========")

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

print("========== Headline: Short Forms of Mathematical Operation: Practice 08 ==========")

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
# It prints till 2 decimal points
print(hourly_rate)
# it will store only the integer after division, not the decimal point as we have given "//"
# it will store the nearest small integer such 20/3 = 6.666667, it stores 6, not 7
hourly_rate = 20 // 3
print(hourly_rate)

print("================== Headline: F-String: Practice 09 ==================")

score = 10
age = 29
isGoing = True

# we have written code where converted any variable such as int, float into string
# "str(variable_name) then print in the console, but using "f-string" we can print
# any sort of variables in below format
# OUTPUT: The Score is: 10, His/Her age is 29, Is going: True
print(f"The Score is: {score}, His/Her age is {age}, Is going: {isGoing}")

print("======== weeks left if you live 90 years old comparing age: Practice 10 ==========")

age = input()
years_left = 90 - int(age)
weeks_have = years_left * 52
print(f"You have {weeks_have} weeks left.")

print("============== Bill Split calculator: Practice 11 =================")

print("Welcome to the tip calculator.")

total_bill_string = input("What was the total Bill? $")
total_bill = float(total_bill_string)

tip_string = input("What percentage of tip would you like to give? 10, 12, or 15? ")
tip = int(tip_string) * total_bill / 100

person_string = input("How many people to split the bill? ")
per_person_bill = round((total_bill + tip) / int(person_string), 2)
print(f" Each person should pay: {per_person_bill}")

print("============ Regular If Else [ Odd/Even Number ]: Practice 12 ============")
# take a number as input and convert the number as it will be taken as a string, convert in
# int
num = int(input())

# if the number has modules 0, then it is an even number such as 2,4,6 are even number
if num % 2 == 0:
    print("This is an even number.")
# Otherwise number is an odd number for instance 1,3,5
else:
    print("This is an odd number.")

print("============ Nested If Else [ Odd/Even Number ]: Practice 13 ============")

height = 120
age = 19
# as the height is equal to 120, it will go to the below first print statement
if height >= 120:
    # Asking the user his/her age
    print(f" What is your age?: {age}")
    # if age is less than or equal to bill 18 is $5.00
    if age <= 18:
        print("Pay $5.00")
    # if the age is not smaller and equal than 18, the bill is $8.00
    else:
        print("Pay $8.00")
# if height is not 120 (smaller or bigger doesn't matter). print the below statement
else:
    print("Your Height is lower than 120 meter. Sorry")

print("============ elif - conditions : Practice 14 ============")

num = 19
# if number is below 12 it prints "if statement"
if num < 12:
    print(" if statement.")
    # if the number is smaller than 17 but bigger than 12, prints "elif statement 01."
elif num < 17:
    print(" elif statement 01.")
    # if the number is bigger than 12 and also bigger than 17 but smaller than 20, then
    # prints "elif statement 02."
elif num < 20:
    print(" elif statement 02.")
# Any number from 20 to bigger will print "else statement"
else:
    print("else statement")

print("============ elif - conditions : Practice 15 - Body Mass Index with condition ============")

# Take weight string and convert into integer number
weight = int(input())
# Take height and convert it into float number
height = float(input())

# Calculate body mass index
bmi = weight / (height * height)
# round the "bmi" with 4 decimal points for instance "5.7384"
bmi = round(bmi, 4)
# if bmi is less than 18.5, then print bmi and he/she is under weight
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
# if bmi is between 18.6 to 24.99, it will print the "normal weight"
# REMEMBER: if the bmi is 18.5 it will go  directly the "else" condition because in above code
# we mention bmi should be smaller than 18.5 and below code bmi should be bigger than 18.50 but
# in no other condition we mention bmi = 18.5 or bmi <= or >= 18.5. That's why it will go the
# else condition.
elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

print("============ Nested else/if Leap Year : Practice 16 ============")

# enter year and convert it into integer
year = int(input())

# if the year is divided by 4 and modules is zero then go to the next if
if year % 4 == 0:
    # As the year is divided by 4 and modules is zero sharply, then check if the year is
    # divided by 100 and modules is 0. after dividing by 4 if the number is not divided by 100,
    # then it is a leap year. Or if the number is divided by 100, then enter to the next if condition.
    if year % 100 == 0:
        # after dividing by 4 and 100, if the number is divided by 400, then it is a leap year.
        # else it is not a leap year.
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    # if the number is not divided by 100, but 4, then it is a leap year.
    else:
        print("Leap year")
# if the number is not divided by 4 and modules is not exactly 0, then it is not a leap
# year.
else:
    print("Not leap year")

print("============ Multiple else/if Leap Year : Practice 16 ============")

# Enter the height. As it will be taken as string, we will convert the string into integer
height = int(input("Enter your height in cm: "))
# declare a variable "bill" initially which is 0
bill = 0
# if the height is 120 cm or more than it, then print the statement
if height >= 120:
    print("You can ride the roller coaster.")
    # Now enter the age and convert it into integer
    age = int(input("Enter your age: "))
    # if the age is below 12, then the bill is $5.00
    if age < 12:
        # now the bill is 5
        bill = 5
        # prints it is a child ticket nad bill is 5
        print(f"Child Tickets are ${bill}")
    # if the age is 12 or smaller or equal to 18, then a bill is 7
    elif age <= 18:
        bill = 7
        # print it is a teen ticket, and a bill is 7
        print(f" Teen Tickets are ${bill}")
    else:
        # for all others a bill is 9
        bill = 9
        # print it is an adult ticket, and a bill is 7
        print(f"Adult tickets are ${bill} ")

    # take an input either "Y" or "N"
    need_photo = input("Do you want a photo? type: Y?N = ")
    # if it is "Y" then a bill is bill +3
    if need_photo == "Y":
        bill += 3
    # print the total bill and print it, but it is not inside the above if statement
    # if this print statement was inside the if statement, it will be printed if the input is
    # "Y", I mean if the user wants to take a photo then will calculate the bill and will print it.
    # Otherwise, it will close the program without printing the "total bill."
    print(f"Your total bill is: {bill}")
else:
    print("Sorry! you can not ride. ")

    print("============ else/if Pizza Delivery : Practice 16 - Project - 01 ============")

    # Take the pizza size
    pizza_size = input("What size pizza do you want? S, M, or L ")

    # Take pepperoni user wants or not
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    # extra cheese user needs or not
    extra_cheese = input("Do you want extra cheese? Y or N ")
    # Small pizza prize
    small_pizza_price = 15
    # Medium pizza price
    medium_pizza_price = 20
    # Large pizza price
    large_pizza_price = 25
    # the final price is 0 initially
    final_bill = 0

    # If the size is small, then go to this if block
    if pizza_size == "S":
        # If pepperoni is Yes, final_bill is 15 + 2
        if add_pepperoni == "Y":
            final_bill = small_pizza_price + 2
        else:
            # If no pepperoni final_bill = 15
            final_bill = small_pizza_price

    # If the size is Medium, then go to this if block
    if pizza_size == "M":
        # If pepperoni is Yes, final_bill is 20 + 2
        if add_pepperoni == "Y":
            final_bill = medium_pizza_price + 3
        else:
            # The bill now 20
            final_bill = medium_pizza_price
    # If the size is Large, then go to this if block
    if pizza_size == "L":
        # If pepperoni is Yes, final_bill is 25 + 2
        if add_pepperoni == "Y":
            final_bill = large_pizza_price + 3
        else:
            final_bill = large_pizza_price
    # if any user wants extra cheese, no matter it is small, medium or large; extra 1 dollar will be added
    # into their total bill
    if extra_cheese == "Y":
        final_bill = final_bill + 1

    print("Thank you for choosing Python Pizza Deliveries!")
    # print the final bill
    print(f"Your final bill is: ${final_bill}")

