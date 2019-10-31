#Generate a random number between 1 and 9
#(including 1 and 9). Ask the user to guess the number,
#then tell them whether they guessed too low, too high, or exactly right.
#(Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends,
#print this out.
import random
guesses = ["1","2","3","4","5","6","7","8","9"]
comp_choice = random.choice(guesses)
going = True
while going == True:
    my_guess = input("Guess a number between 1 and 9 ")
    a = str(my_guess)
    if int(my_guess) > 9 and int(my_guess) < 1:
        print("sorry out of guess range")
    elif a == comp_choice:
        print("Aye!!!!! you're pretty good at this")
        going = False
    elif  a > comp_choice:
        print("Guess a little lower")
    elif a < comp_choice:
        print("Guess a little higher")
