import pygame
import random

# Initialize the pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Pacman settings
pacman_size = 50
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5

# Ghost settings
ghost_size = 50
ghost_speed = 3

# Create a ghost at a random position
def create_ghost():
    ghost_x = random.randint(0, screen_width - ghost_size)
    ghost_y = random.randint(0, screen_height - ghost_size)
    return [ghost_x, ghost_y]

ghosts = [create_ghost() for _ in range(5)]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Keep Pacman inside the screen
    pacman_x = max(0, min(screen_width - pacman_size, pacman_x))
    pacman_y = max(0, min(screen_height - pacman_size, pacman_y))

    # Move ghosts
    for ghost in ghosts:
        ghost[0] += random.choice([-ghost_speed, ghost_speed])
        ghost[1] += random.choice([-ghost_speed, ghost_speed])
        # Keep ghosts inside the screen
        ghost[0] = max(0, min(screen_width - ghost_size, ghost[0]))
        ghost[1] = max(0, min(screen_height - ghost_size, ghost[1]))

    # Check for collisions
    pacman_rect = pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost[0], ghost[1], ghost_size, ghost_size)
        if pacman_rect.colliderect(ghost_rect):
            print("Game Over!")
            running = False

    # Drawing
    screen.fill(black)
    pygame.draw.rect(screen, yellow, (pacman_x, pacman_y, pacman_size, pacman_size))
    for ghost in ghosts:
        pygame.draw.rect(screen, white, (ghost[0], ghost[1], ghost_size, ghost_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
