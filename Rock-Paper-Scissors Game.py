import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    while True:
        # Get player's choice
        player = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()

        if player == 'quit':
            print("Thanks for playing!")
            break

        if player not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Computer's random choice
        computer = random.choice(choices)

        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")

        # Determine winner
        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

# Start the game
print("Welcome to Rock, Paper, Scissors!")
play_game()

# No files are created or modified during execution