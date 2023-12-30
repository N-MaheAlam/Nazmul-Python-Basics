print("========== Headline: Short Forms of Mathematical Operation: Practice 09 ==========")

score = 10
# score = score +1
score += 1
# prints 11
print(score)

age = 29
age -= 9
# prints 20
print(age)

hourly_rate = 20 / 3
# print with decimal point
print(hourly_rate)
hourly_rate = round(20 / 3)
# prints the closed integer number, 6.666666667 = 7, it prints 7
print(hourly_rate)

hourly_rate = round(20 / 3, 2)
# It prints till 2 decimal points
print(hourly_rate)
# it will store only the integer after division, not the decimal point as we have given "//"
# it will store the nearest small integer such 20/3 = 6.666667, it stores 6, not 7
hourly_rate = 20 // 3
print(hourly_rate)
