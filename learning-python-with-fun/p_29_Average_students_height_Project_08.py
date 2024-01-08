
print("====== Headline: For loop to measure average height : Practice 28 / Project - 08 =======")
# Only just input numbers and put space in each number to produce desire output
height_of_students = input().split()
# after splitting the input the list is a string
print(f"String list: {height_of_students}")

# run for loop to convert string numbers into int
for n in range(0, len(height_of_students)):
    height_of_students[n] = int(height_of_students[n])
# Now the input list is an int list
print(f"int list: {height_of_students}")

# a variable to hold the total height
total_height = 0
for height in height_of_students:
    # each time when the loop starts, it takes each value from the list height_of_students
    # than add it like total_height = total_height + height
    total_height += height
# print the total height from out of loop
print(f"total height = {total_height}")

total_number_of_students = 0
for number in height_of_students:
    # each time when the loop starts, it takes each index number from the list height_of_students
    # than add it like total_number_of_students = total_number_of_students + height
    total_number_of_students = total_number_of_students + 1
# print the total students number from out of loop
print(f"number of students = {total_number_of_students}")

# calculate average by dividing total height by total students
average_height = round(total_height / total_number_of_students)
# print average height
print(f"average height = {average_height}")
