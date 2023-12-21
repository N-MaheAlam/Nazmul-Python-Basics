#   This Project is to make understandable python for everyone without watching videos
#   But reading codes, and it's output.
#   Create a small python project in your IDE.Take each block of code based on
#   "Headline:" and run in "main.py" of your project, you can understand easily how
#   each line of code is working.All the projects are stored in "learning-python-with-fun"
#   Copy each file each time, run in your "main.py", understand code structures,input, outputs
#   Very easy to learn.


husband_name_list = ["Nazmul", "Mahe", "Alam", "Rabbi"]
wife_name_list = ["Mussarat", "Jahan", "Kumu"]

# This works as lists inside in a list called nested list
#   STRUCTURE of the nested list:

#   [ parent index 0 [sub index 0, sub index 1, sub index 2, sub index 3],
#   parent index 1 [ sub index 0, sub index 1, sub index 2]]

#   [0][0]     [0][1]  [0][2]  [0][3]     [1][0]      [1][1]  [1][2]
# [['Nazmul', 'Mahe', 'Alam', 'Rabbi'], ['Mussarat', 'Jahan', 'Kumu']]
both_names_list = [husband_name_list, wife_name_list]

# prints Nested list "[['Nazmul', 'Mahe', 'Alam', 'Rabbi'], ['Mussarat', 'Jahan', 'Kumu']]"
print(both_names_list)

# prints-first index (0) of both_names_list which is
# output = ['Nazmul', 'Mahe', 'Alam', 'Rabbi']
print(both_names_list[0])

# prints 2nd or last index(1) of both_names_list which is
# output = ['Mussarat', 'Jahan', 'Kumu']
print(both_names_list[1])

# this one-prints output = Rabbi Jahan
print(both_names_list[0][3] + " " + both_names_list[1][1])
