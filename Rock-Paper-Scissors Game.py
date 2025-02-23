import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors - Best of 5")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (34, 177, 76)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font
FONT = pygame.font.Font(None, 36)
LARGE_FONT = pygame.font.Font(None, 72)
SMALL_FONT = pygame.font.Font(None, 24)

class Game:
    def __init__(self):
        self.choices = ["ROCK", "PAPER", "SCISSORS"]
        self.player_score = 0
        self.computer_score = 0
        self.result = ""
        self.player_choice = ""
        self.computer_choice = ""
        self.game_state = "PLAYING"  # PLAYING, SHOWING_RESULT, or GAME_OVER
        self.result_timer = 0
        self.winning_score = 3  # Best of 5 (first to 3 wins)

        # Load and scale images
        self.rock_img = pygame.image.load("rock.png")
        self.paper_img = pygame.image.load("paper.png")
        self.scissors_img = pygame.image.load("scissors.png")

        # Scale images to 80x80 pixels
        self.icon_size = (80, 80)
        self.rock_img = pygame.transform.scale(self.rock_img, self.icon_size)
        self.paper_img = pygame.transform.scale(self.paper_img, self.icon_size)
        self.scissors_img = pygame.transform.scale(self.scissors_img, self.icon_size)

    def draw_button_with_icon(self, text, x, y, width, height, active, icon):
        # Draw button background
        color = GRAY if active else WHITE
        button = pygame.draw.rect(WINDOW, color, (x, y, width, height))
        pygame.draw.rect(WINDOW, BLACK, (x, y, width, height), 2)  # Border

        # Draw icon
        icon_rect = icon.get_rect(center=(x + width/2, y + height/2 - 15))
        WINDOW.blit(icon, icon_rect)

        # Draw text
        text_surface = FONT.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=(x + width/2, y + height - 20))
        WINDOW.blit(text_surface, text_rect)

        return button

    def show_result_screen(self, result_text, color):
        # Create semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(WHITE)
        WINDOW.blit(overlay, (0,0))

        # Show result text
        text = LARGE_FONT.render(result_text, True, color)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        WINDOW.blit(text, text_rect)

        # Show choices with icons
        player_text = FONT.render("You chose:", True, BLACK)
        comp_text = FONT.render("Computer chose:", True, BLACK)

        WINDOW.blit(player_text, (WIDTH/4 - 50, HEIGHT/2 + 50))
        WINDOW.blit(comp_text, (3*WIDTH/4 - 100, HEIGHT/2 + 50))

        # Display choice icons
        player_icon = self.get_choice_icon(self.player_choice)
        computer_icon = self.get_choice_icon(self.computer_choice)

        WINDOW.blit(player_icon, (WIDTH/4 - 40, HEIGHT/2 + 90))
        WINDOW.blit(computer_icon, (3*WIDTH/4 - 90, HEIGHT/2 + 90))

    def get_choice_icon(self, choice):
        if choice == "ROCK":
            return self.rock_img
        elif choice == "PAPER":
            return self.paper_img
        else:
            return self.scissors_img

    def run(self):
        clock = pygame.time.Clock()

        while True:
            WINDOW.fill(WHITE)

            # Draw scores and games remaining
            score_text = FONT.render(f"Player: {self.player_score} | Computer: {self.computer_score}", True, BLACK)
            games_text = FONT.render(f"First to {self.winning_score} wins!", True, BLUE)
            WINDOW.blit(score_text, (WIDTH/2 - 100, 30))
            WINDOW.blit(games_text, (WIDTH/2 - 100, 70))

            if self.game_state == "PLAYING":
                # Draw instruction
                instruction = FONT.render("Make your choice:", True, BLACK)
                WINDOW.blit(instruction, (WIDTH/2 - 80, 150))

                # Draw buttons with icons
                rock_btn = self.draw_button_with_icon("ROCK", 100, 200, 150, 150, False, self.rock_img)
                paper_btn = self.draw_button_with_icon("PAPER", 325, 200, 150, 150, False, self.paper_img)
                scissors_btn = self.draw_button_with_icon("SCISSORS", 550, 200, 150, 150, False, self.scissors_img)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if rock_btn.collidepoint(mouse_pos):
                            self.play_round("ROCK")
                        elif paper_btn.collidepoint(mouse_pos):
                            self.play_round("PAPER")
                        elif scissors_btn.collidepoint(mouse_pos):
                            self.play_round("SCISSORS")

            elif self.game_state == "SHOWING_RESULT":
                if self.result == "WIN":
                    self.show_result_screen("YOU WIN THIS ROUND!", GREEN)
                elif self.result == "LOSE":
                    self.show_result_screen("COMPUTER WINS THIS ROUND!", RED)
                else:
                    self.show_result_screen("IT'S A TIE!", BLACK)

                if time.time() - self.result_timer > 2:
                    if self.player_score >= self.winning_score or self.computer_score >= self.winning_score:
                        self.game_state = "GAME_OVER"
                    else:
                        self.game_state = "PLAYING"

            elif self.game_state == "GAME_OVER":
                winner_text = "YOU WIN THE GAME!" if self.player_score > self.computer_score else "COMPUTER WINS THE GAME!"
                color = GREEN if self.player_score > self.computer_score else RED

                self.show_result_screen(winner_text, color)

                # Draw play again button
                play_again = FONT.render("Click anywhere to play again", True, BLUE)
                play_again_rect = play_again.get_rect(center=(WIDTH/2, HEIGHT - 100))
                WINDOW.blit(play_again, play_again_rect)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.__init__()  # Reset the game
                        self.game_state = "PLAYING"

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            clock.tick(60)

    def play_round(self, player_choice):
        self.player_choice = player_choice
        self.computer_choice = random.choice(self.choices)

        if self.player_choice == self.computer_choice:
            self.result = "TIE"
        elif ((self.player_choice == "ROCK" and self.computer_choice == "SCISSORS") or
              (self.player_choice == "PAPER" and self.computer_choice == "ROCK") or
              (self.player_choice == "SCISSORS" and self.computer_choice == "PAPER")):
            self.result = "WIN"
            self.player_score += 1
        else:
            self.result = "LOSE"
            self.computer_score += 1

        self.game_state = "SHOWING_RESULT"
        self.result_timer = time.time()

if __name__ == "__main__":
    game = Game()
    game.run()
