

print("============ Headline: For loop with continue : Practice 27  ============")

fruits = ["apple", "banana", "mango", "orange", "strawberry"]
# prints fruit names
for fruit in fruits:
    print(fruit)
    # if the fruit is "mango" it will print "mango" and also will continue the loop
    if fruit == "mango":
        continue
print("continue keyword before any other statement in for loop")
for fruit in fruits:
    # it prints each value in "fruits" variable, but once the loop finds "mango", it skips
    # and print the test of the variables
    if fruit == "mango":
        continue
    print(fruit)

# REMEMBER:
# output can be different based on where you put to continue statement and what output actual you
# want.
