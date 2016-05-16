import pygame
import constants
import sys

background_image = pygame.image.load("data/menu_victory_bg.png")
pygame.init()
pygame.mixer.music.load("data/sound/cloud-kingdom.wav")
class Menu_victoire:
    
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

pygame.init()
screen = pygame.display.set_mode((800, 600))
menu_font = pygame.font.Font(None, 65)
texte1 = [Menu_victoire("QUITTER", (295, 457))]
texte2 = [Menu_victoire("REJOUER", (295, 340))]

if True :
    pygame.mixer.music.play(-1, 0.0)
while True:
    pygame.event.pump()
    screen.blit(background_image, [0,0])
    for Menu_victoire in texte1:
        if Menu_victoire.rect.collidepoint(pygame.mouse.get_pos()):
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            Menu_victoire.hovered = True
            if Menu_victoire.rect.collidepoint(pygame.mouse.get_pos()) and pressed1==1:
                pygame.display.quit()
                pygame.mixer.music.stop()
        else:
            Menu_victoire.hovered = False
        Menu_victoire.draw()
    
    for Menu_victoire in texte2:
        if Menu_victoire.rect.collidepoint(pygame.mouse.get_pos()):
            (pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
            Menu_victoire.hovered = True
            if Menu_victoire.rect.collidepoint(pygame.mouse.get_pos()) and pressed1==1:
                pygame.mixer.music.stop()
                import platform_scroller
                import main_menu
                platform_scroller.main()
                
        else:
            Menu_victoire.hovered = False
        Menu_victoire.draw()
    pygame.display.update()
