print("============ Nested If Else: Practice 14 ============")

height = 120
age = 19
# as the height is equal to 120, it will go to the below first print statement
if height >= 120:
    # Asking the user his/her age
    print(f" What is your age?: {age}")
    # if age is less than or equal to bill 18 is $5.00
    if age <= 18:
        print("Pay $5.00")
    # if the age is not smaller and equal than 18, the bill is $8.00
    else:
        print("Pay $8.00")
# if height is not 120 (smaller or bigger doesn't matter). print the below statement
else:
    print("Your Height is lower than 120 meter. Sorry")