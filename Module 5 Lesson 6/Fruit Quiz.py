import random

class FruitQuiz:

    def __init__(self):

        self.fruit={'apple':'red','banana':'yellow','orange':'orange','watermelon':'green',
        }

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruit.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()

            if user_answer.lower() == color:
                print("Correct!")
            else:
                print("Incorrect!")

            option = input("Do you want to continue? (y/n): ")
            if option.lower() == 'n':
                break

print("Welcome to the Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()