print("============== Headline: Bill Split calculator: Practice 11 =================")

print("Welcome to the tip calculator.")

# Take a number which is bill as input
total_bill_string = input("What was the total Bill? $")
total_bill = float(total_bill_string)

# take percentage of tips
tip_string = input("What percentage of tip would you like to give? 10, 12, or 15? ")

# calculate  total tips based on bill
tip = int(tip_string) * total_bill / 100

# take an integer as input which will represent the total person
person_string = input("How many people to split the bill? ")
# add total bill and tips , then divide by total person and round the bill in 2 decimal format
per_person_bill = round((total_bill + tip) / int(person_string), 2)

# print how much each person has to pay
print(f" Each person should pay: {per_person_bill}")
