import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print("\nWell,",name, ", I am thinking of a number between 1 and 20.")
    
    secr = random.randint(1, 20)
    attempts = 0

    while True:
        guess = int(input("\nTake a guess.\n"))
        attempts += 1
        if guess < secr:
            print("\nYour guess is too low.")
        elif guess > secr:
            print("\nYour guess is too high.")
        else:
            print(f"\nGood job,", name,"! You guessed my number in",attempts, "guesses!")
            break

guess_the_number()
