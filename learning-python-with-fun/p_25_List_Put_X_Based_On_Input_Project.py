line1 = ["1A", "1B", "1C"]
line2 = ["2A", "2B", "2C"]
line3 = ["3A", "3B", "3C"]
lines = [line1, line2, line2]
print("Hiding your treasure! X marks the spot.")
print('Enter just one combination of [a,b,c] with [1,2,3] such as "a1" or "b2":')
position = input()
letter = position[0].upper()
abc = ["A", "B", "C"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
lines[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}\n")
print(lines)