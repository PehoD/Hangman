import random
import hangman_words
import hangman_art


lives = 6


print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:


    print(f"**************************** {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()






    for letter in correct_letters:
        if guess == letter:
            print(f"You already guessed a: {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Word to guess: " + display)



    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed: {guess} it's not in the word")

        if lives == 0:
            game_over = True


            print(f"*********************** IT WAS <{chosen_word}>! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(hangman_art.stages[lives])
