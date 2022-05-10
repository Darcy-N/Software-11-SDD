import random, os

def clear():
    os.system('cls||clear')

clear()


HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
word = random.choice(words).upper()

MAX_WRONG = 8
so_far = ("-") * len(word)
used = []
wrong = 0

print("\t \t Welcome to Hangman!")
print()
input("Press Enter to START: ")

while wrong < MAX_WRONG and so_far != word:
    clear()
    print(HANGMAN[wrong])
    print("Word so far: ", so_far)
    print("Letters used: ", used)

    guess = input("Guess a letter: ").upper()
    if guess == "\x1b": # Debugging
        exit()
    print()

    while guess in used:
        print("Try again... You've already used this letter")
        guess = input("Guess a letter: ").upper()
        print()
    used.append(guess)

    if guess in word:

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new 

    else:
        print("INCORRECT! Try again!")
        wrong += 1

if wrong == MAX_WRONG:
    print("UNLUCKY! Better luck next time!")
    print("The word was " + word)

else:
    print("WINNER! Congratulations!")
    print(f"The word was {word}")

print()
print()
input("Press Enter to Leave: ")