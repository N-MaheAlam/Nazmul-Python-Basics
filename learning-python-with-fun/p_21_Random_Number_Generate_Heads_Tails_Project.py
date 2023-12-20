# to generate random numbers, we nees to bring the "random" modules by importing in our
# project
import random

random_int = random.randint(100, 200)
print(f"This is a random integer 100 <= random_int <= 200: {random_int}")
random_float = random.random()
print(f"Random number between 0000000< random_float< 1.0000 : {random_float}")

# Heads or Tails games starts from here
flip_coin = random.randint(0, 1)

if flip_coin == 1:
    print("Heads")
else:
    print("Tails")
