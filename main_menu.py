import pygame
import constants
import sys
import platform_scroller as Main

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
background = pygame.image.load("data/test_bg.png")
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
menu_font = pygame.font.Font(None, 40)
options = [Option("JOUER", (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)), Option("QUITTER", (constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 100))]

while True:
    pygame.event.pump()
    screen.blit(background, (0, 0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
            Main.main()
        else:
            option.hovered = False
        option.draw()
    pygame.display.update()