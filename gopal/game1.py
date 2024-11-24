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
YELLOW = (255, 255, 0)  # Coin color (Yellow)
ORANGE = (255, 165, 0)  # Basket color
RED_BUTTON = (255, 0, 0)  # Color for the restart button
GIFT_COLOR = (0, 255, 0)  # Gift color (Green)

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

# Item settings (Now coins, changed to circles)
ITEM_RADIUS = 10  # Set the radius of the falling coins
falling_items = []

# Font for text
font = pygame.font.SysFont("Arial", 24)

# Game variables
score = 0
coins = 0  # Track coins
game_over = False
speed = 5  # Initial speed for falling items

# Restart button settings
RESTART_BUTTON_WIDTH = 120
RESTART_BUTTON_HEIGHT = 50

