print("================= Headline: Body Mass Calculator: Practice 08 =======================")

height = input()
weight = input()
# Convert height String into float number
height_as_float = float(height)
# Convert weight String into integer
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2

# If the bmi in case comes as a float, convert it into integer
bmi_as_int = int(bmi)
# print in console
print(bmi_as_int)
