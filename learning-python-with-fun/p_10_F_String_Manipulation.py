print("======== Headline: weeks left if you live 90 years old comparing age: Practice 10 ==========")

# take a 2-digit number as input
age = input()
# convert age into integer then subtract from 90
years_left = 90 - int(age)
# weeks left before die
weeks_have = years_left * 52
# prints weeks left and printing an integer in the strings by using "f" string before the printing
# statement which prints strings as well as the integer.
print(f"You have {weeks_have} weeks left.")
