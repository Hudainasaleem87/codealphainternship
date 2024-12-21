import random

def hangman():
    word_list = ["python", "java", "javascript", "c++", "c#"]
    word = random.choice(word_list).upper()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("Lives left:", lives)
        print("Used letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You already used that letter. Guess again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, "!")

hangman()