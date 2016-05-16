import pygame
import constants
import sys
from player import Player
pygame.mixer.music.load("data/sound/game_over.wav")
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
                return (121, 28, 248)
            else:
                return (150, 131, 236)
        
        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

pygame.init()
screen = pygame.display.set_mode((800, 600))
menu_font = pygame.font.Font(None, 50)
texte1 = [Option("RAGEQUIT", (305, 350))]
texte2 = [Option("REJOUER", (310, 250))]
background_image = pygame.image.load("data/fond.jpg")

if True :
    pygame.mixer.music.play(-1, 0.0)
while True:
    pygame.event.pump()
    screen.blit(background_image, [0,0])
    for Option in texte1:
        if Option.rect.collidepoint(pygame.mouse.get_pos()):
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            Option.hovered = True
            if Option.rect.collidepoint(pygame.mouse.get_pos()) and pressed1==1:
                pygame.display.quit()
                pygame.mixer.music.stop()
        else:
            Option.hovered = False
        Option.draw()
    
    for Option in texte2:
        if Option.rect.collidepoint(pygame.mouse.get_pos()):
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            Option.hovered = True
            if Option.rect.collidepoint(pygame.mouse.get_pos()) and pressed1==1:
                pygame.mixer.music.stop()
                import platform_scroller
                import main_menu
                platform_scroller.main()
                
        else:
            Option.hovered = False
        Option.draw()
    pygame.display.update()
