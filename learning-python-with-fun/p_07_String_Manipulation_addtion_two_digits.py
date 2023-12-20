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