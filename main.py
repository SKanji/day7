import random
import hangman_art as ha
import hangman_words as hw

chosen_word = random.choice(hw.word_list)
lives = 6
#Testing code
print(ha.logo)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for i in chosen_word:
  display.append("_")
print(display)

while '_' in display and lives > 0:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already used this letter: {guess}")

  for letter in chosen_word:
    if letter == guess:
      indexes = [i for i, n in enumerate(chosen_word) if n == guess]
      for x in indexes:
        display[x] = guess

  if guess not in chosen_word:
    lives -=1
    print(f'You have {lives} lives left.')
    print(f'The following letter is not in the word: {guess}')
    print(ha.stages[lives])

  print(display)

if '_' not in display:
  print("You've won")
  print(display)
else:
  print("Game Over")

