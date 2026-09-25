import random
playing = True
number = str(random.randint(0,9))

print("Let's play the number game! I choose a number from 0 to 9, and you guess it!")
print("If you guess the number correctly, then you win.")

while playing:
    guess = input("Now, guess a number from 0 to 9: \n")
    if number == guess:
        print("You've Won!")
        print("I chose the number",number)
        break

    else:
        print("Wrong! Try again.")