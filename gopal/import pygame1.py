import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch Falling Items")

# Load background image
background_image = pygame.image.load("background.jpg")  # Make sure you have a 'background.jpg' file in the same folder as your script
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize the background to fit the screen

# Basket settings
BASKET_WIDTH = 80
BASKET_HEIGHT = 20
basket = pygame.Rect(SCREEN_WIDTH // 2 - BASKET_WIDTH // 2, SCREEN_HEIGHT - 40, BASKET_WIDTH, BASKET_HEIGHT)

# Item settings
ITEM_WIDTH = 30
ITEM_HEIGHT = 30
falling_items = []

# Font for text
font = pygame.font.SysFont("Arial", 24)

# Game variables
score = 0
game_over = False
speed = 5  # Initial speed for falling items


def spawn_item():
    x_pos = random.randint(0, SCREEN_WIDTH - ITEM_WIDTH)
    y_pos = -ITEM_HEIGHT  # Start above the screen
    falling_items.append(pygame.Rect(x_pos, y_pos, ITEM_WIDTH, ITEM_HEIGHT))


def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


def game_over_screen():
    game_over_text = font.render("Game Over! Press Q to Quit or R to Restart", True, WHITE)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(game_over_text, text_rect)


def reset_game():
    """Reset game variables to start a new game."""
    global score, game_over, falling_items
    score = 0
    game_over = False
    falling_items = []


# Game loop
clock = pygame.time.Clock()
while True:
    screen.blit(background_image, (0, 0))  # Draw the background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Press Q to quit the game after game over
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_r:  # Press R to restart the game after game over
                reset_game()  # Reset game variables

    if not game_over:
        # Move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.left > 0:
            basket.x -= 7
        if keys[pygame.K_RIGHT] and basket.right < SCREEN_WIDTH:
            basket.x += 7

        # Spawn new items every 30 frames (around 0.5 seconds)
        if random.randint(1, 30) == 1:
            spawn_item()

        # Move items
        for item in falling_items[:]:
            item.y += speed
            if item.colliderect(basket):
                falling_items.remove(item)  # Item is caught
                score += 1  # Increase score
            elif item.top > SCREEN_HEIGHT:
                falling_items.remove(item)  # Item goes out of screen
                game_over = True  # Game over if an item falls off the screen

        # Display score and basket
        display_score()
        pygame.draw.rect(screen, YELLOW, basket)  # Draw the basket

        # Draw falling items
        for item in falling_items:
            pygame.draw.rect(screen, WHITE, item)

    else:
        # Game Over condition
        background_image = pygame.image.load(r'C:\Users\1shiv\OneDrive\Desktop\gopal\gang.jpg')  # Use raw string to avoid escape sequence issues
        background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        

    # Update screen
    pygame.display.update()

    # Maintain frame rate
    clock.tick(FPS)
