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