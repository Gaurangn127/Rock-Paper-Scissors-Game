import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Rock-Paper-Scissors Simulation")

# Define classes for sprites
class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("rock.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = -self.speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = -self.speed_y

class Paper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image =pygame.image.load("paper.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = -self.speed_y

class Scissors(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image =pygame.image.load("scissors.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.randint(-1, 1)
        self.speed_y = random.randint(-1, 1)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y = -self.speed_y

# Create sprite groups
all_sprites = pygame.sprite.Group()
rock_sprites = pygame.sprite.Group()
paper_sprites = pygame.sprite.Group()
scissors_sprites = pygame.sprite.Group()

# Create rocks, papers, and scissors and add them to sprite groups
for i in range(50):
    rock = Rock(random.randint(0, screen_width), random.randint(0, screen_height))
    paper = Paper(random.randint(0, screen_width), random.randint(0, screen_height))
    scissors = Scissors(random.randint(0, screen_width), random.randint(0, screen_height))
    rock_sprites.add(rock)
    paper_sprites.add(paper)
    scissors_sprites.add(scissors)
    all_sprites.add(rock, paper, scissors)

# set up the clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Check for collisions and transform sprites
    rock_collisions = pygame.sprite.groupcollide(rock_sprites, paper_sprites, False, False)
    for rock, paper in rock_collisions.items():
        new_paper = Paper(rock.rect.x, rock.rect.y)
        paper_sprites.add(new_paper)
        all_sprites.add(new_paper)
        rock.kill()

    paper_collisions = pygame.sprite.groupcollide(paper_sprites, scissors_sprites, False, False)
    for paper, scissors in paper_collisions.items():
        new_scissors = Scissors(paper.rect.x, paper.rect.y)
        scissors_sprites.add(new_scissors)
        all_sprites.add(new_scissors)
        paper.kill()

    scissors_collisions = pygame.sprite.groupcollide(scissors_sprites, rock_sprites, False, False)
    for scissors, rock in scissors_collisions.items():
        new_rock = Rock(scissors.rect.x, scissors.rect.y)
        rock_sprites.add(new_rock)
        all_sprites.add(new_rock)
        scissors.kill()

    # Draw sprites
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update screen
    pygame.display.flip()

    clock.tick(60)

# Quit Pygame
pygame.quit()