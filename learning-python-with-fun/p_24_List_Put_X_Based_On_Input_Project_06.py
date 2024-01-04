
print("============ Headline: Place 'X' in desire number : Practice 24 // Project 06 ============")
# here line1, line2, line3 are three separated lists
line1 = ["1A", "1B", "1C"]
line2 = ["2A", "2B", "2C"]
line3 = ["3A", "3B", "3C"]
# put all 3 lists inside another list name "lines"
lines = [line1, line2, line3]
# print below 2 print statement
print("Hiding your treasure! X marks the spot.")
print('Enter just one combination of [a,b,c] with [1,2,3] such as "a1" or "b2":')

# take the input as a sequence like "b1" or "c2 etc
position = input()
# find the position of the letter in input variable "position" and convert into uppercase
letter = position[0].upper()
# take a list "abc"
abc = ["A", "B", "C"]
# find the index number of the letter from "abc" list
letter_index = abc.index(letter)
# when we take the input, for instance, "b3", here position[1] = 3, convert it into integer then
# subtract 1 from it
number_index = int(position[1]) - 1
# so for "b3" number index = 2 and letter index = 1
# So, in list "lines [2][1]" will be marked as "X"
# check the output
lines[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}\n")
print(lines)
