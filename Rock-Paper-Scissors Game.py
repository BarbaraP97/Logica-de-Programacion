import random
import time
from typing import Tuple

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player_score = 0
        self.computer_score = 0
        self.round_number = 0
        self.winning_score = 3  # Best of 5 (first to 3 wins)

    def get_player_choice(self) -> str:
        while True:
            choice = input("\nEnter your choice (rock/paper/scissors) or 'quit' to exit: ").lower().strip()
            if choice == 'quit':
                return choice
            if choice in self.choices:
                return choice
            print("Invalid choice! Please choose rock, paper, or scissors.")

    def get_computer_choice(self) -> str:
        # Add dramatic effect
        print("Computer is choosing", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print()
        return random.choice(self.choices)

    def determine_winner(self, player: str, computer: str) -> Tuple[str, str]:
        if player == computer:
            return "tie", "It's a tie!"

        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if winning_combinations[player] == computer:
            return "player", f"{player.capitalize()} beats {computer}! You win!"
        else:
            return "computer", f"{computer.capitalize()} beats {player}! Computer wins!"

    def display_scores(self):
        print("\n" + "="*40)
        print(f"Round {self.round_number}")
        print(f"Player Score: {self.player_score}")
        print(f"Computer Score: {self.computer_score}")
        print("="*40)

    def display_final_results(self):
        print("\n" + "*"*50)
        print("GAME OVER!")
        print(f"Final Score - Player: {self.player_score}, Computer: {self.computer_score}")
        if self.player_score > self.computer_score:
            print("Congratulations! You won the game!")
        elif self.player_score < self.computer_score:
            print("Better luck next time! Computer wins the game!")
        else:
            print("It's a tie game!")
        print("*"*50)

    def play_game(self):
        print("\nWelcome to Rock, Paper, Scissors!")
        print(f"First to {self.winning_score} wins!")

        while True:
            self.display_scores()

            player_choice = self.get_player_choice()
            if player_choice == 'quit':
                break

            computer_choice = self.get_computer_choice()

            print(f"\nYou chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")

            winner, message = self.determine_winner(player_choice, computer_choice)
            print(message)

            if winner == "player":
                self.player_score += 1
            elif winner == "computer":
                self.computer_score += 1

            self.round_number += 1

            # Check if someone has won
            if self.player_score == self.winning_score or self.computer_score == self.winning_score:
                self.display_final_results()
                break

            time.sleep(1)  # Short pause between rounds

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
