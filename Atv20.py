import random as rdm

secret_number = rdm.randint(1, 50)
guess = 0
attempts = 0

while True:
    guess = int(input("Guess the number (1,50): "))
    attempts += 1


    if guess == secret_number:
        print("YOU WIN!!!!")
        print("Attempts: ", attempts)
        break
    elif guess < secret_number:
        print("Too Low!")
    else: print("Too high!")