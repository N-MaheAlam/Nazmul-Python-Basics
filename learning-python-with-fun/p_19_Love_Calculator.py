
print("============ Headline: Love Calculator : Practice 19 ============")
print("The Love Calculator is calculating your score...")
your_name = input()  # What is your name?
your_partner_name = input()  # What is their name?
# add these two strings
combined_names = your_name + your_partner_name

# if the "combined_names" is in the upper case, make it lower by calling the lower() function
names_in_lower = combined_names.lower()

# count how many words of 't' in you and yours partner whole name in "combined_names" variables
t = names_in_lower.count('t')
# count how many words of 'r' in you and yours partner whole name in "combined_names" variables
r = names_in_lower.count('r')
# count how many words of 'u' in you and yours partner whole name in "combined_names" variables
u = names_in_lower.count('u')
# count how many words of 'e' in you and yours partner whole name in "combined_names" variables
e = names_in_lower.count('e')
# calculate the total count of each letter variable t,r,u,e.
# such is t is 1 time, r is 2 times,u is 3 times, and e is 4 times appeared then
# first_digit = 1+2+3+4 = 10
first_digit = t + r + u + e
# same procedure for the above "true" (t,r,u,e)
l = names_in_lower.count('l')
o = names_in_lower.count('o')
v = names_in_lower.count('v')
e = names_in_lower.count('e')
second_digit = l + o + v + e

# Convert "first_digit" and "second_digit" into string then integer.For instance, if
# first_digit = 5 and second_digit = 6 "total_love" = 56 and converted 56 into integer
total_love = int(str(first_digit) + str(second_digit))

# if "total_love" is smaller than 10 and bigger than 90, then print the below line
# with the value of "total_love"
if (total_love < 10) or (total_love > 90):
    print(f"Your score is {total_love}, you go together like coke and mentos.")

# if "total_love" is bigger or equal than 40 and smaller or equal than 50, than print
# below line with the value of "total_love"
elif (total_love >= 40) and (total_love <= 50):
    print(f"Your score is {total_love}, you are alright together.")
# for everything else, print the score of "total_love"
else:
    print(f"Your score is {total_love}.")