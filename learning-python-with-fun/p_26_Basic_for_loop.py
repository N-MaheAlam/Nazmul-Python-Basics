print("============ Headline: Basic for loop : Practice 26 =======")

names = ["Nazmul", "Mahe", "Alam", "Rabbi"]
# prints each name from "names" list variable
for name in names:
    print(name)

print("2nd for loop results")
# it prints number from 0 to 8 in each new line
for num in range(9):
    print(num)

print("3rd for loop results")
# it prints 3 to 6 in new lines because the range starts from 3 and stops in 6
for number in range(3, 7):
    print(number)

family_names = ["Feroz", "Alam", "Mumin", "Islam"]

# Once the for loop is finished, we can put an else statement to send any message
for name in family_names:
    print(name)
else:
    print("Family name printing finished")

