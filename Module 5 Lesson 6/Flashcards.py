class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):


        return self.word+'  ( '+self.meaning+' )'

flash = []
print("welcome to flashcard app")


while True:
    word = input("Enter the word : ")
    meaning = input("Enter the meaning : ")

    flash.append(flashcard(word, meaning))
    option = input("Do you want to add more flashcards? (y/n) : ")

    if option.lower() == 'n':
        break

print("\nYour flashcards are : ")
for i in flash:
    print(i)
      