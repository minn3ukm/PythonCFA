import random

genres = ['pop', 'rock', 'hip-hop', 'country', 'jazz', 'classical']

# Randomly select a genre
random_genre = random.choice(genres)

print("Welcome to MinnzZz Music Genre Guessing Game!")
print("Can you guess the genre of a randomly chosen music?")
print("Here are the available genres: ", genres)

tries = 3
while tries > 0:
    guess = input("\nEnter your guess: ")
    
    if guess.lower() == random_genre.lower():
        print("Congratulations! You guessed it right.")
        break
    
    tries -= 1
    print("Wrong guess! Try again. Tries left:", tries)

if tries == 0:
    print("Sorry, you ran out of tries. The correct genre was", random_genre)