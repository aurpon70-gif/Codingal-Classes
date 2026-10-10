import random
import time

number = random.randint(1, 100)

def intro():
    print("What is your name?")
    global name
    name = input()
    print(name + ", let's play a game! I'm thinking of a number between 1 and 100. Can you guess it?")
    if (number%2 == 0):
        x='even'
    else:
        x='odd'
    print("This is an {} number.".format(x))
    time.sleep(.5)
    print("Let's begin!")

def pick():
    guessestaken = 0

    while guessestaken < 6:
        time.sleep(.25)
        enter=input("Take a guesss: ")

        try:
            guess = int(enter)

            if guess<=100 and guess>=1:
                guessestaken= guessestaken + 1
                if guessestaken < 6:
                    if guess < number:
                        print("Your guess is too low.")
                    elif guess > number:
                        print("Your guess is too high.")
                    if guess != number:
                        time.sleep(.5)
                        print("Try again.")

                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("Make the guess in between 1 and 100.")
                time.sleep(.25)
                print("Try again.")
        except:
            print("That isn't a number. Try again.")
    if guess == number:
        guessesTaken = str(guessestaken)
        print("Nice job, {}! You figured out the number in {} smart guesses.".format(name, guessesTaken))

    if guess != number:
        print("You lost. The number was {}.".format(number))
playagain="Yes"
while playagain=="yes" or playagain=="Yes" or playagain=="y":
    intro()
    pick()
    playagain = input("Play again? (y/n)")
    playagain=input()


