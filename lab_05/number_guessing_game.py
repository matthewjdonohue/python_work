import random

def get_user_guess():
    user_guess = int(input("Please enter a number between 1 and 50: "))
    
    while user_guess < 1 or user_guess > 50:
        print("Number is out of range!")
    return user_guess
    
def evaluate_user_guess(user_guess, target):
    if user_guess < target:
        print("Oh, too low, guess again.")
        return False  
    elif user_guess > target:
        print("Oh, too high, guess again.")
        return False  
    else:
        return True  

def print_end(user_won, target):
    if user_won:
        print("Congrats! You won!")
    else:
        print(f"So sorry, you lost. The number was {target}.")
    print("Thanks for playing!")

def main():
    target = random.randint(1, 50)
    user_won = False

    for i in range(8):
        user_guess = get_user_guess()
        user_won = evaluate_user_guess(user_guess, target)
        if user_won:
            break

    print_end(user_won, target)

if __name__ == "__main__":
    main()
