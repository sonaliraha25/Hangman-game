import random
stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========
  ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========
  ''', '''
    +---+
    |   |
        |
        |
        |
        |
  =========
  ''']
end_of_game = False
word_list=["ardvark","baboon","camel"]
lives=6
generate=random.choice(word_list)
display=[]
for i in range(len(generate)):
    display.append("_")
while not end_of_game:
    letter = input("Guess a letter: ").lower()
    for position in range(len(generate)):
      if letter==generate[position]:
          display[position]=letter
    if letter not in generate:
         lives-=1
         if lives==0:
          end_of_game=True
          print("You lose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win")
    print(stages[lives])

