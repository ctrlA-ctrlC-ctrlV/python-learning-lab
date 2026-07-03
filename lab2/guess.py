# Lab problem: "Number Guessing Game"
SECRETE = 42;

guess = int(input("I'm thinking of a number between 1 and 100.\nYour guess? >> "))
num = 1

while guess != SECRETE:
    if guess > 100 or guess < 0:
        print("ERROR: OUT OF RANGE")        
    elif guess > SECRETE:
        print("Too high!")
    elif guess < SECRETE:
        print("Too low!")    
    
    guess = int(input("Your guess again? >> "))
    num+=1
    
print(f"Correct! You got it in {num} guesses. Sharp!")