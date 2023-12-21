import random

print("============ Headline: Who Will Pay The Bill : Practice 22 // Project - 05 ============")
# Take input of names.Make sure they are separated by (, ) comma and space for instance
# input = Nazmul, Mahe, Alam
names_string = input()

# split each name by comma and space (, ) and store as a list in "names"
names = names_string.split(", ")
# count the total number of names present in "name"
total_names = len(names)

# it generates a random integer number from 0 to the length -1 of the list
random_name_index = random.randint(0, total_names - 1)
# get the name by random_name_index number
person_who_pay_bills_payer = names[random_name_index]
# print the name in console
print(person_who_pay_bills_payer + " is going to buy the meal today!")