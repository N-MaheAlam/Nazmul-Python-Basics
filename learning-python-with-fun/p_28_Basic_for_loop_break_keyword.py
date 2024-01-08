
print("============ Headline: For loop with break : Practice 28  ============")
fruits = ["apple", "banana", "mango", "orange", "strawberry"]

# prints till mango and stops
for fruit in fruits:
    print(fruit)
    if fruit == "mango":
        break

print("break keyword before any other statement in for loop")

for fruit in fruits:
    # it does not print "mango." because it breaks the loop when the value is "mango"
    if fruit == "mango":
        break
    print(fruit)