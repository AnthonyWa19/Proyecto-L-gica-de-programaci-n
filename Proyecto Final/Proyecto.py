import random

def Guess_the_Number():
    Name = input("Hello, What's your name? ")
    print(f"Welcome, {Name}! Let's play Guess the Number")
    
    while True:
        print("\nChoose a difficulty level:")
        print("1 - Easy (Numbers of 1 to 10)")
        print("2 - Medium (Numbers of 1 to 50)")
        print("3 - Hard (Numbers of 1 to 100)")
        level = input("Choose 1, 2 or 3: ")
        
        if level in ['1', '2', '3']:
            level = int(level)
            break
        else:
            print("Invalid option. Try again.")

    if level == 1:
        Random_number = random.randint(1, 10)
        Max_Attempts = 4
    elif level == 2:
        Random_number= random.randint(1, 50)
        Max_Attempts = 6
    else:
        Random_number= random.randint(1, 100)
        Max_Attempts = 9

    print(f"\nI am thinking in a number. You have {Max_Attempts} attempts to a guess.")

    Guess = 0
    while Guess < Max_Attempts:
        Guess += 1
        while True:
            try:
                Attempt = int(input(f"\nIntento {Guess}: "))
                break
            except ValueError:
                print("Please, Enter a valid number.")

        if Attempt < Random_number:
            print("No, the number I'm thinking of is higher")
        elif Attempt > Random_number:
            print("No, the number I'm thinking of is lower")
        else:
            print(f"\n¡Congratulations, {Name}! ¡You guessed a number in {Guess} attempts!")
            break

    if Attempt != Random_number:
        print(f"\nSorry, {Name}.The number, I was thinking of was  {Random_number}.")

    Play_Again = input("\n¿Do you want to play again? (y/n): ")
    if Play_Again.lower() == 'y':
        Guess_the_Number()
    else:
        print(f"\nThanks for playing, {Name}!")

Guess_the_Number()