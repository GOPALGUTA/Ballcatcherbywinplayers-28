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
RED = (255, 0, 0)  # Color for the restart button

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch Falling Items")

# Load background image (ensure the image is downloaded and placed in the same directory as the script)
background_image = pygame.image.load("background.jpg")  # Make sure you have 'background.jpg' in your project folder
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize the background to fit the screen

# Basket settings
BASKET_WIDTH = 80
BASKET_HEIGHT = 20
basket = pygame.Rect(SCREEN_WIDTH // 2 - BASKET_WIDTH // 2, SCREEN_HEIGHT - 40, BASKET_WIDTH, BASKET_HEIGHT)

# Item settings
ITEM_RADIUS = 15  # Radius for the falling balls (circle)
falling_items = []

# Font for text
font = pygame.font.SysFont("Arial", 24)

# Game variables
score = 0
game_over = False
speed = 5  # Initial speed for falling items

# Restart button settings
RESTART_BUTTON_WIDTH = 120
RESTART_BUTTON_HEIGHT = 50
restart_button = pygame.Rect(SCREEN_WIDTH // 2 - RESTART_BUTTON_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, RESTART_BUTTON_WIDTH, RESTART_BUTTON_HEIGHT)

# Function to spawn items (falling balls)
def spawn_item():
    x_pos = random.randint(0, SCREEN_WIDTH - ITEM_RADIUS * 2)  # Random X position for the circle
    y_pos = -ITEM_RADIUS * 2  # Start above the screen
    falling_items.append(pygame.Rect(x_pos, y_pos, ITEM_RADIUS * 2, ITEM_RADIUS * 2))  # Use a rectangle for positioning

# Function to display score
def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to display game over screen
def game_over_screen():
    game_over_text = font.render("Game Over! Press Q to Quit", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))
    
    # Draw restart button
    pygame.draw.rect(screen, RED, restart_button)  # Button background
    restart_text = font.render("Restart", True, WHITE)
    screen.blit(restart_text, (restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2))

# Function to reset the game state
def reset_game():
    global score, game_over, speed, falling_items, basket
    score = 0
    game_over = False
    speed = 5
    falling_items = []
    basket = pygame.Rect(SCREEN_WIDTH // 2 - BASKET_WIDTH // 2, SCREEN_HEIGHT - 40, BASKET_WIDTH, BASKET_HEIGHT)

# Game loop
clock = pygame.time.Clock()
while True:
    screen.blit(background_image, (0, 0))  # Draw the background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
            if game_over and restart_button.collidepoint(event.pos):  # Check if restart button is clicked
                reset_game()  # Reset the game

        # Check if the user presses 'Q' to quit the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

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
                game_over = True  # End the game

        # Display score and basket
        display_score()
        pygame.draw.rect(screen, YELLOW, basket)  # Draw the basket

        # Draw falling items as circles (balls)
        for item in falling_items:
            pygame.draw.circle(screen, WHITE, item.center, ITEM_RADIUS)  # Draw a circle at the center of the item

    # Game Over condition
    if game_over:
        game_over_screen()

    # Update screen
    pygame.display.update()

    # Maintain frame rate
    clock.tick(FPS)

