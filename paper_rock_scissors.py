#Paper rock scissors game where you play against the computer
import random
user1 = input("Paper, Rock, or Scissors? ")
first_choice = user1.lower()
print("you chose ", first_choice)
options = ["rock", "paper", "scissors"]
user2 = random.choice(options)
print("The computer chose " + user2)

if user1 == user2:
    print("It's a tie!!!!")
elif user1 == "paper" and user2 == "rock":
    print("Congratulations you win")
elif user1 == "rock" and user2 == "scissors":
    print("Congratulations you win")
elif user1 == "scissors" and user2 == "paper":
    print("Congratulations you win")
else:
    print("That aint it cap you lose")
