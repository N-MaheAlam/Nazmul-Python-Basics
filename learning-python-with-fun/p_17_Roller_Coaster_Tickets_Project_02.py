print("======= Headline:  Roller coaster tickets price based on age : Practice 17 ======")
print("======= Project 02 ======")

# Enter the height. As it will be taken as string, we will convert the string into integer
height = int(input("Enter your height in cm: "))
# declare a variable "bill" initially which is 0
bill = 0
# if the height is 120 cm or more than it, then print the statement
if height >= 120:
    print("You can ride the roller coaster.")
    # Now enter the age and convert it into integer
    age = int(input("Enter your age: "))
    # if the age is below 12, then the bill is $5.00
    if age < 12:
        # now the bill is 5
        bill = 5
        # prints it is a child ticket nad bill is 5
        print(f"Child Tickets are ${bill}")
    # if the age is 12 or smaller or equal to 18, then a bill is 7
    elif age <= 18:
        bill = 7
        # print it is a teen ticket, and a bill is 7
        print(f" Teen Tickets are ${bill}")
    else:
        # for all others a bill is 9
        bill = 9
        # print it is an adult ticket, and a bill is 7
        print(f"Adult tickets are ${bill} ")

    # take an input either "Y" or "N"
    need_photo = input("Do you want a photo? type: Y?N = ")
    # if it is "Y" then a bill is bill +3
    if need_photo == "Y":
        bill += 3
    # print the total bill and print it, but it is not inside the above if statement
    # if this print statement was inside the if statement, it will be printed if the input is
    # "Y", I mean if the user wants to take a photo then will calculate the bill and will print it.
    # Otherwise, it will close the program without printing the "total bill."
    print(f"Your total bill is: {bill}")
else:
    print("Sorry! you can not ride. ")
