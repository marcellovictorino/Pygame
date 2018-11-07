import pygame
import random

STARTING_BLUEBLOBS = 10
STARTING_REDBLOBS = 3

WIDTH = 800
HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
COLORS = [WHITE,BLACK,RED,GREEN,BLUE]

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

class Blob:
    def __init__(self, color):
        self.color = color
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8) # specific to Pygame. Play around to see results

    def move(self):
        self.move_x = random.randrange(-2,3)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

        if self.x < 0:
            self.x = 0
        elif self.x > WIDTH:
            self.x = WIDTH

        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT:
            self.y = HEIGHT


def draw_environment(blobs_list):
    game_display.fill(WHITE)
    for blob_dict in blobs_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
    pygame.display.update()
    

def main():
    red_blob = dict(enumerate([Blob(RED) for i in range(STARTING_REDBLOBS)]))# Creating Object
    blue_blob = dict(enumerate([Blob(BLUE) for i in range(STARTING_BLUEBLOBS)]))# Creating Object
        # Blob(color=RED) # Creating Object

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw_environment([red_blob, blue_blob])
        clock.tick(60)

if __name__ == '__main__':
    main()