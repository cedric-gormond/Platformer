
import pygame
import constants
import levels
from spritesheet_functions import SpriteSheet

class Pudi(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    level = None

    def __init__(self):
        """ Fonction initial (constructeur) """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load("data/pudi0.jpg")
        self.image = image
        
        # Reference the image rect.
        self.rect = self.image.get_rect()
        
    
        def calc_grav(self):
        
         if self.change_y == 0:
              self.change_y = 1
         else:
             self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
    def pudi1(self):
        self.image=pygame.image.load("data/pudi1.jpg")
    def pudi2 (self):
        self.image=pygame.image.load("data/pudi2.jpg")    
    def pudi3(self):
        self.image=pygame.image.load("data/pudi3.jpg")
        
