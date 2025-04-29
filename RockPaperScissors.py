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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Hello, let's play a game!")
game_list = [rock, paper, scissors]
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n")
if choice == "0":
    print(game_list[0])
elif choice =="1":
    print(game_list[1])
else:
    print(game_list[2])

print("Computer  chose: ")
random_index = random.choice(game_list)
print(random_index)
if choice == "0" and random_index == game_list[0]:
    print("It's a draw")
elif choice == "0" and random_index == game_list[1]:
    print("You lose")
elif choice == "0" and random_index == game_list[2]:
    print("You win!!")
elif choice == "1" and random_index == game_list[1]:
    print("It's a draw")
elif choice == "1" and random_index == game_list[2]:
    print("You lose")
elif choice == "1" and random_index == game_list[0]:
    print("You win!!")
elif choice == "2" and random_index == game_list[2]:
    print("It's a draw")
elif choice == "2" and random_index == game_list[0]:
    print("You lose")
elif choice == "2" and random_index == game_list[1]:
    print("You win!!")
