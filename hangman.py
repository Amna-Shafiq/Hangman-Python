
import random
from words import words_mix




def generate_random_word():
   selected_word = random.choice(words_mix)
   return selected_word.upper()


def play(selected_word):
   word_completion = "_"*len(selected_word)
   guessed = False
   guessed_letter = []
   guessed_words = []
   tries = 6
   hint = 1
   print("Lets Play Hangman")
   print(display_hangman(tries))
   print(word_completion)
   print("\n")
   while not guessed and tries > 0:
      if hint > 0:
            if input("Want a hint? (Y/N) ").upper() == "Y":
                word_as_list = list(word_completion)
                hint_index = [i for i, letter in enumerate(selected_word) if word_as_list[i] == "_"]
                if hint_index:
                    index = hint_index[0]
                    word_as_list[index] = selected_word[index]
                    word_completion = "".join(word_as_list)
                    hint -= 1
                print(word_completion)
                if "_" not in word_completion:
                 guessed = True
                 
                print("\n")

      guess = input("Please enter a letter or a word: ").upper()
      if len(guess) == 1 and guess.isalpha:
         if guess in guessed_letter:
            print("you already guessed the letter",guess)
         elif guess not in selected_word:
            print(guess,"is not in the word")
            tries -=1
            guessed_letter.append(guess)
         else:
            print("Good Job,", guess, "is in the word!")
            guessed_letter.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(selected_word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
         
      elif len(guess) == len(selected_word) and guess.isalpha:
         if guess in guessed_words:
                print("You already guessed the word", guess)
         elif guess != selected_word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
         else:
                guessed = True
                word_completion = selected_word
      else:
         print("Not a valid guess.")

      print(display_hangman(tries))
      print(word_completion)
      print("\n")
   if guessed:
        print("Congrats, you guessed the word! You win!")
   else:
        print("Sorry, you ran out of tries. The word was " + selected_word + ". Maybe next time!")


def display_hangman(tries):
     stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
     return stages[tries]

    


def main():
    word = generate_random_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = generate_random_word()
        play(word)


if __name__ == "__main__":
    main()