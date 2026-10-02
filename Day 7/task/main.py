import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print("Lives left: ", lives)
    guess = input("Enter your guess: ").lower()

    if guess in correct_letters:
        print("You already guessed this letter!")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} this letter!")

        if lives == 0:
            game_over = True
            print("You Lose!")
    print("The word was: ", chosen_word)
    if "_" not in display:
        game_over = True
        print("You win!")

    print(hangman_art.stages[lives])
