print("=== Headline:  elif - conditions : Practice 15 - Body Mass Index with condition =====")

# Take weight string and convert into integer number
weight = int(input())
# Take height and convert it into float number
height = float(input())

# Calculate body mass index
bmi = weight / (height * height)
# round the "bmi" with 4 decimal points for instance "5.7384"
bmi = round(bmi, 4)
# if bmi is less than 18.5, then print bmi and he/she is under weight
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
# if bmi is between 18.6 to 24.99, it will print the "normal weight"
# REMEMBER: if the bmi is 18.5 it will go  directly the "else" condition because in above code
# we mention bmi should be smaller than 18.5 and below code bmi should be bigger than 18.50 but
# in no other condition we mention bmi = 18.5 or bmi <= or >= 18.5. That's why it will go the
# else condition.
elif 18.5 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
