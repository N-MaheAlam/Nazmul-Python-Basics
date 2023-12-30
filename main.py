#   This Project is to make understandable python for everyone without watching videos
#   But reading codes, and it's output.
#   Create a small python project in your IDE.Take each block of code based on
#   "Headline:" and run in "main.py" of your project, you can understand easily how
#   each line of code is working.All the projects are stored in "learning-python-with-fun"
#   Copy each file each time, run in your "main.py", understand code structures,input, outputs
#   Very easy to learn.
##################           Write Code From Below       ####################

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

# This statement will be skipped although the num is less than 30 because the "num" is
# already caught by the above elif num < 20 , statement. Here a things come into picture
# if, elif,... else are in same intention ( I mean same structured line for which it caught
# in first elif statement where the condition matches )
elif num < 30:
    print(" elif statement 02.")
# Any number from 30 to bigger will print "else statement"
else:
    print("else statement")
