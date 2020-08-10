# Write your code here
import random
import string

print("H A N G M A N \n")
list_of_words = ['python', 'java', 'kotlin', 'javascript']
decision = input('Type "play" to play the game, "exit" to quit:')


while decision == "play":
    correct_word = list(random.choice(list_of_words))
    hidden_word = list('-' * len(correct_word))
    guessed_letters = []

    i = 8
    while i > 0:
        print("".join(hidden_word))
        player_guess = input("Input a letter: ")
        if len(player_guess) != 1:
            print("You should input a single letter")
        elif player_guess not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        else:
            if player_guess in guessed_letters:
                print("You already typed this letter")
            elif player_guess in correct_word:
                for j in range(len(correct_word)):
                    if player_guess == correct_word[j]:
                        hidden_word[j] = correct_word[j]

            else:
                print("No such letter in the word")
                i -= 1
            guessed_letters.append(player_guess)

        if hidden_word == correct_word:
            print(f"You guessed the word {correct_word}!\nYou survived!")
            break
        elif i == 0:
            print("You are hanged!")
        print("")

    decision = input('Type "play" to play the game, "exit" to quit: ')



