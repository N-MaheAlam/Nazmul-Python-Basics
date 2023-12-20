# Use (") double quotes or single quote ('), it does not matter to initiate variables inside a list
it_is_a_list = ['Nazmul', 'Mahe', 'Alam']

# prints "['Nazmul', 'Mahe', 'Alam']"
print(it_is_a_list)

# prints only "Mahe"
print(it_is_a_list[1])

# It prints "Alam". To get the value from last in a list, we can use -1,-2,-3 ......
print(it_is_a_list[-1])

# prints "Mahe"
print(it_is_a_list[-2])

# It appends "Rabbi" at the end of the list
it_is_a_list.append("Rabbi")

# Prints a new list "['Nazmul', 'Mahe', 'Alam', 'Rabbi']"
print(it_is_a_list)

# Inserts "Naz" in index 2, and the previous value of index 2 "Alam", now places in index 3
it_is_a_list.insert(2, "Naz")

# prints new list ['Nazmul', 'Mahe', 'Naz', 'Alam', 'Rabbi']
print(it_is_a_list)

# Prints total how many elements are present in the lis till now. #5 elements
print(f"Total elements in it_is_a_list variable: {it_is_a_list.__len__()}")

# it reverses the list now
it_is_a_list.reverse()

# prints reverse list "['Rabbi', 'Alam', 'Naz', 'Mahe', 'Nazmul']"
print(it_is_a_list)

# Removes "Naz" from the list
it_is_a_list.remove("Naz")

# new list ['Rabbi', 'Alam', 'Mahe', 'Nazmul']
print(it_is_a_list)

it_is_another_list = ["Mussarat", "Jahan", "Kumu"]

# Now all the elements will present from "it_is_another_list" to "it_is_a_list"
it_is_a_list.extend(it_is_another_list)

# Prints ['Rabbi', 'Alam', 'Mahe', 'Nazmul', 'Mussarat', 'Jahan', 'Kumu']
print(it_is_a_list)

index_number_of_nazmul = it_is_a_list.index("Nazmul")
print(f'Name = "Nazmul" index number is: {index_number_of_nazmul}')

# search "Kumu" from index 2 to index 6, if in finds that prints the index number
search_musarrat_in_list = it_is_a_list.index("Mussarat", 2, 6)
print(f'Name = "Mussarat" index number is: {search_musarrat_in_list} ')

# Removes All the elements from the list. Left an empty list
it_is_a_list.clear()
# it prints "[]
print(f"Empty List: {it_is_a_list}")