
print("============ Headline: else/if Pizza Delivery : Practice 18 // project -03 ============")

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