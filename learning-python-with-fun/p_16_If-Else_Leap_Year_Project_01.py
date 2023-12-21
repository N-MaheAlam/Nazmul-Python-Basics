print("====== Headline: Nested else/if Leap Year : Practice 16 // Project 01 ============")

# enter year and convert it into integer
year = int(input())

# if the year is divided by 4 and modules is zero then go to the next if
if year % 4 == 0:
    # As the year is divided by 4 and modules is zero sharply, then check if the year is
    # divided by 100 and modules is 0. after dividing by 4 if the number is not divided by 100,
    # then it is a leap year. Or if the number is divided by 100, then enter to the next if condition.
    if year % 100 == 0:
        # after dividing by 4 and 100, if the number is divided by 400, then it is a leap year.
        # else it is not a leap year.
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    # if the number is not divided by 100, but 4, then it is a leap year.
    else:
        print("Leap year")
# if the number is not divided by 4 and modules is not exactly 0, then it is not a leap
# year.
else:
    print("Not leap year")
