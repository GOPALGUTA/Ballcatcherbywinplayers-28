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

# Load images for basket and falling items (replace with your own image paths)
basket_image = pygame.image.load("basket.png")  # Basket image
basket_image = pygame.transform.scale(basket_image, (80, 20))  # Resize basket to fit the screen

# Basket settings
BASKET_WIDTH = 80
BASKET_HEIGHT = 20
basket = pygame.Rect(SCREEN_WIDTH // 2 - BASKET_WIDTH // 2, SCREEN_HEIGHT - 40, BASKET_WIDTH, BASKET_HEIGHT)

# Item settings
ITEM_RADIUS = 15  # Radius of the falling items (now circular)
falling_items = []

# Font for text
font = pygame.font.SysFont("Arial", 24)

# Game variables
score = 0
game_over = False
speed = 5  # Initial speed for falling items

# Function to spawn a new item
def spawn_item():
    x_pos = random.randint(0, SCREEN_WIDTH - ITEM_RADIUS * 2)  # Avoid spawning off-screen
    y_pos = -ITEM_RADIUS * 2  # Start above the screen
    falling_items.append(pygame.Rect(x_pos, y_pos, ITEM_RADIUS * 2, ITEM_RADIUS * 2))

# Function to display the score
def display_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to show the game over screen
def game_over_screen():
    game_over_text = font.render("Game Over! Press Q to Quit", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

# Game loop
clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)  # Fill the screen with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
            game_over = True

    # Display score and basket
    display_score()
    screen.blit(basket_image, basket.topleft)  # Draw the basket using the image

    # Draw falling items as circles
    for item in falling_items:
        pygame.draw.circle(screen, WHITE, item.center, ITEM_RADIUS)

    # Game Over condition
    if game_over:
        game_over_screen()

    # Update the screen
    pygame.display.update()

    # Maintain frame rate
    clock.tick(FPS)

