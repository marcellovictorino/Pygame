import pygame
import random
from ClassBlob import Blob

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


def draw_environment(blobs_list):
    game_display.fill(WHITE)
    for blob_dict in blobs_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_boundary()
    pygame.display.update()
    

def main():
    red_blob = dict(enumerate([Blob(RED, WIDTH, HEIGHT) for i in range(STARTING_REDBLOBS)]))# Creating Object
    blue_blob = dict(enumerate([Blob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUEBLOBS)]))# Creating Object
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