import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
games_list = [rock, paper, scissor]
choose_randomly = random.choice(games_list)

user_choice = ""
try:
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.")
    user_choice = int(input())

    #  rock beats scissor = rock wins
    #  scissor beats paper = scissor wins
    #  paper beats rock = paper wins
    if user_choice < 0 or user_choice >= 3:
        print("Invalid number. you lose.")
    if user_choice == 0:
        print("You choose: Rock. ")
        print(rock)
        if choose_randomly == scissor:
            print(f"Computer choose: Scissor \n {scissor}")
            print("You win.")
        elif choose_randomly == paper:
            print(f"Computer choose: Paper \n {paper}")
            print("Computer win.")
        else:
            print(f"Computer also choose: Rock \n {rock}")
            print("Game tie.")

    if user_choice == 1:
        print("You choose: Paper")
        print(paper)
        if choose_randomly == rock:
            print(f"Computer choose: Rock\n {rock}")
            print("You win.")
        elif choose_randomly == scissor:
            print(f"Computer choose: Paper\n {scissor}")
            print("Computer win.")

        else:
            print(print(f"Computer also choose: Paper\n {paper}"))
            print("Game tie.")

    if user_choice == 2:
        print("You choose: Scissor")
        print(scissor)
        if choose_randomly == paper:
            print(print(f"Computer choose: Paper\n {paper}"))
            print("You win.")
        elif choose_randomly == rock:
            print(print(f"Computer choose: Rock\n {rock}"))
            print("Computer win.")
        else:
            print(f"Computer also choose: Scissor\n {scissor}")
            print("Game tie.")
except ValueError:
    print("Put 0 or 1 or 2")