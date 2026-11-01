import random

words = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "robotics": "Technology involving robots",
    "internet": "A global network",
    "developer": "A person who writes code"
}

stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]

word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
attempts = 6

print("WELCOME TO HANGMAN!")
print("Hint:", hint)

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print(stages[attempts])

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

else:
    print(stages[0])
    print("Game Over!")
    print("Correct word:", word)
