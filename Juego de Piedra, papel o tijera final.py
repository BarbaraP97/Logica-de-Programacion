import pygame
import sys
import random
import json
from os.path import exists

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
clock = pygame.time.Clock()

# Load and scale images
rock_img = pygame.image.load("rock.png").convert_alpha()
paper_img = pygame.image.load("paper.png").convert_alpha()
scissors_img = pygame.image.load("scissors.png").convert_alpha()

rock_img = pygame.transform.scale(rock_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissors_img = pygame.transform.scale(scissors_img, (100, 100))

class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Game:
    def __init__(self):
        self.state = "menu"
        self.player_name = ""
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 5
        self.round_result = None
        self.result_timer = 0
        self.load_scores()

        # Create buttons
        self.start_button = Button(300, 200, 200, 50, "Start Game", GREEN)
        self.history_button = Button(300, 300, 200, 50, "History", BLUE)
        self.exit_button = Button(300, 400, 200, 50, "Exit", RED)

        # Create choice buttons
        self.rock_button = Button(150, 400, 100, 100, "", WHITE)
        self.paper_button = Button(350, 400, 100, 100, "", WHITE)
        self.scissors_button = Button(550, 400, 100, 100, "", WHITE)

    def load_scores(self):
        if exists("scores.json"):
            with open("scores.json", "r") as f:
                self.scores_history = json.load(f)
        else:
            self.scores_history = []

    def save_scores(self):
        with open("scores.json", "w") as f:
            json.dump(self.scores_history, f)

    def handle_menu_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.is_clicked(event.pos):
                    self.state = "name_input"
                elif self.history_button.is_clicked(event.pos):
                    self.state = "history"
                elif self.exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

    def handle_name_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.player_name:
                    self.state = "game"
                elif event.key == pygame.K_BACKSPACE:
                    self.player_name = self.player_name[:-1]
                else:
                    if len(self.player_name) < 15:
                        self.player_name += event.unicode

    def handle_game_input(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_choice(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    self.handle_key_choice(event.key)

    def handle_choice(self, pos):
        player_choice = None
        if self.rock_button.is_clicked(pos):
            player_choice = "rock"
        elif self.paper_button.is_clicked(pos):
            player_choice = "paper"
        elif self.scissors_button.is_clicked(pos):
            player_choice = "scissors"

        if player_choice:
            self.play_round(player_choice)

    def handle_key_choice(self, key):
        choices = {pygame.K_1: "rock", pygame.K_2: "paper", pygame.K_3: "scissors"}
        self.play_round(choices[key])

    def play_round(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        # Determine round winner and set result message
        if player_choice == computer_choice:
            self.round_result = "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            self.player_score += 1
            self.round_result = f"{self.player_name} wins!"
        else:
            self.computer_score += 1
            self.round_result = "Computer wins!"

        self.rounds_played += 1
        self.result_timer = pygame.time.get_ticks()  # Start timer for result display

        if self.rounds_played >= self.max_rounds:
            self.end_game()

    def end_game(self):
        winner = "Player" if self.player_score > self.computer_score else "Computer"
        self.scores_history.append({
            "player_name": self.player_name,
            "player_score": self.player_score,
            "computer_score": self.computer_score,
            "winner": winner
        })
        self.save_scores()
        self.state = "game_over"

    def draw(self):
        screen.fill(WHITE)

        if self.state == "menu":
            self.draw_menu()
        elif self.state == "name_input":
            self.draw_name_input()
        elif self.state == "game":
            self.draw_game()
        elif self.state == "history":
            self.draw_history()
        elif self.state == "game_over":
            self.draw_game_over()

        pygame.display.flip()

    def draw_menu(self):
        title_font = pygame.font.Font(None, 64)
        title = title_font.render("Rock Paper Scissors", True, BLACK)
        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 100))

        self.start_button.draw(screen)
        self.history_button.draw(screen)
        self.exit_button.draw(screen)

    def draw_name_input(self):
        font = pygame.font.Font(None, 48)
        prompt = font.render("Enter your name:", True, BLACK)
        name = font.render(self.player_name, True, BLUE)

        screen.blit(prompt, (WINDOW_WIDTH//2 - prompt.get_width()//2, 200))
        screen.blit(name, (WINDOW_WIDTH//2 - name.get_width()//2, 300))

    def draw_game(self):
        # Draw scores
        font = pygame.font.Font(None, 36)
        score_text = f"{self.player_name}: {self.player_score} - Computer: {self.computer_score}"
        rounds_text = f"Round {self.rounds_played + 1} of {self.max_rounds}"

        score_surface = font.render(score_text, True, BLACK)
        rounds_surface = font.render(rounds_text, True, BLACK)

        screen.blit(score_surface, (20, 20))
        screen.blit(rounds_surface, (WINDOW_WIDTH - rounds_surface.get_width() - 20, 20))

        # Draw choice buttons with images
        screen.blit(rock_img, (150, 400))
        screen.blit(paper_img, (350, 400))
        screen.blit(scissors_img, (550, 400))

        # Draw instructions
        instructions = font.render("Click an icon or press 1, 2, or 3 to make your choice", True, BLACK)
        screen.blit(instructions, (WINDOW_WIDTH//2 - instructions.get_width()//2, 300))

        # Draw round result if active
        if self.round_result and pygame.time.get_ticks() - self.result_timer < 2000:  # Show for 2 seconds
            # Create semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.fill(WHITE)
            overlay.set_alpha(128)
            screen.blit(overlay, (0, 0))

            # Draw result text
            result_font = pygame.font.Font(None, 72)
            result_text = result_font.render(self.round_result, True, BLUE)
            result_rect = result_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
            screen.blit(result_text, result_rect)
        elif pygame.time.get_ticks() - self.result_timer >= 2000:
            self.round_result = None

    def draw_history(self):
        font = pygame.font.Font(None, 36)
        title = font.render("Score History", True, BLACK)
        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 50))

        y = 100
        for score in self.scores_history[-10:]:  # Show last 10 scores
            text = f"{score['player_name']}: {score['player_score']} - Computer: {score['computer_score']} ({score['winner']} won)"
            score_surface = font.render(text, True, BLACK)
            screen.blit(score_surface, (WINDOW_WIDTH//2 - score_surface.get_width()//2, y))
            y += 40

        back_button = Button(300, 500, 200, 50, "Back to Menu", BLUE)
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    self.state = "menu"

    def draw_game_over(self):
        font = pygame.font.Font(None, 48)
        winner = "You won!" if self.player_score > self.computer_score else "Computer won!"
        text = font.render(winner, True, BLACK)
        final_score = font.render(f"Final Score: {self.player_name} {self.player_score} - Computer {self.computer_score}", True, BLACK)

        screen.blit(text, (WINDOW_WIDTH//2 - text.get_width()//2, 200))
        screen.blit(final_score, (WINDOW_WIDTH//2 - final_score.get_width()//2, 250))

        back_button = Button(300, 300, 200, 50, "Back to Menu", BLUE)
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    # Reset game state and return to menu
                    self.state = "menu"
                    self.player_name = ""
                    self.player_score = 0
                    self.computer_score = 0
                    self.rounds_played = 0
                    self.round_result = None

def main():
    game = Game()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game.state == "menu":
            game.handle_menu_input(events)
        elif game.state == "name_input":
            game.handle_name_input(events)
        elif game.state == "game":
            game.handle_game_input(events)

        game.draw()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    
# Created/Modified files during execution:
# scores.json