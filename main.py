#import random module
import random

#assinging ASCII art to the variable
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

game_images = [rock, paper, scissors]

#Horizontal line and Title
print("="*70)
print("Welcome to Stone, Paper, Scissor")
print("="*70)

#performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
  #Take the input from user
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

  # looping until user enter invalid input
  while user_choice >= 3 or user_choice < 0:
    user_choice = int(input("Enter a valid input: "))

  print(game_images[user_choice])

  # Computer chooses randomly any number
  # among 0 , 1 and 2. Using randint method
  # of random module
  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_choice])

  # condition for winning
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")
  print("DO yoy want to play again?(Y/N)")
  ans = input().lower()

   # if user input n or N then condition is True
  if ans =="n":
    break

# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")