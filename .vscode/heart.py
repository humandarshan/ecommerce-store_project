import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Eagle")

SKY = (135, 206, 235)
BLACK = (20, 20, 20)
WHITE = (245, 245, 245)
YELLOW = (240, 190, 40)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(SKY)

    # Left wing
    pygame.draw.arc(screen, BLACK, (120,180,350,220), 3.5, 5.6, 6)

    # Right wing
    pygame.draw.arc(screen, BLACK, (530,180,350,220), 3.8, 5.9, 6)

    # Body
    pygame.draw.ellipse(screen, BLACK, (450,250,120,220))

    # Head
    pygame.draw.circle(screen, WHITE, (510,240), 35)

    # Eye
    pygame.draw.circle(screen, BLACK, (520,235), 4)

    # Beak
    pygame.draw.polygon(screen, YELLOW,
                        [(545,245), (575,238), (545,230)])

    # Tail
    pygame.draw.polygon(screen, BLACK,
                        [(470,455), (430,520), (500,490)])
    pygame.draw.polygon(screen, BLACK,
                        [(550,455), (590,520), (520,490)])

    pygame.display.flip()
    clock.tick(60) 