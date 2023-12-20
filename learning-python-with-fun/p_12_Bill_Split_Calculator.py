print("============== Bill Split calculator: Practice 12 =================")

print("Welcome to the tip calculator.")

total_bill_string = input("What was the total Bill? $")
total_bill = float(total_bill_string)

tip_string = input("What percentage of tip would you like to give? 10, 12, or 15? ")
tip = int(tip_string) * total_bill / 100

person_string = input("How many people to split the bill? ")
per_person_bill = round((total_bill + tip) / int(person_string), 2)
print(f" Each person should pay: {per_person_bill}")