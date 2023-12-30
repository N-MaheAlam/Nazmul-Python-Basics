print("============ Headline: elif - conditions : Practice 14 ============")

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


