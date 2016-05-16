import pygame
import constants
import sys
import platform_scroller as Main
pygame.init()
pygame.mixer.music.load("data/sound/main_menu_music.wav")

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
            return (255, 239, 96)
        else:
            return (145, 110, 0)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

background = pygame.image.load("data/main_menu.png")
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
menu_font = pygame.font.Font(None, 65)
texte1 = [Option("QUITTER", (295, 457))]
texte2 = texte2 = [Option("COMMENCER L'AVENTURE", (110, 340))]
if True :
     pygame.mixer.music.play(-1, 0.0)
while True:
    pygame.event.pump()
    screen.blit(background, [0,0])
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
                Main.main()
                
                
        else:
            Option.hovered = False
        Option.draw()
    pygame.display.update()
