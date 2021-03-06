import pygame
from pygame.locals import *
import Spritesheet as Sprite
from Level import Level
from entities.Mario import Mario
from Input import Input
from Dashboard import Dashboard

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    max_frame_rate = 60

    running = True
    level = Level(screen)
    mario = Mario(0,0,level,screen)
    input = Input(mario)
    clock = pygame.time.Clock()
    dashboard = Dashboard("./img/font.png",8,screen)

    while (running):
        pygame.display.set_caption("{:.2f} FPS".format(clock.get_fps()))
        level.drawLevel(mario.camera)
        dashboard.update()
        running = input.checkForInput()
        mario.drawMario()
        pygame.display.update()
        clock.tick(max_frame_rate)
    main()

if __name__ == "__main__":
    main()



