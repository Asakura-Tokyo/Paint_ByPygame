""" draw_line_onmousemove.py """
import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEBUTTONUP, KEYDOWN

pygame.init()
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    mousepos = []
    mousedown = False

    SURFACE.fill((255, 255, 255))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True
            elif event.type == MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousedown = False
                mousepos.clear()
            elif event.type == KEYDOWN:
                SURFACE.fill((255, 255, 255))

        if len(mousepos) > 1:
            pygame.draw.lines(SURFACE, (255, 0, 0), False, mousepos,5)

        pygame.display.update()
        FPSCLOCK.tick(100)

if __name__ == '__main__':
    main()
