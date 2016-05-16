#ennemis


import pygame
import constants
import levels
from spritesheet_functions import SpriteSheet
from platforms import MovingPlatform
from player import Player
class Enemy(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    walking_frames_l = []

    direction = "L"

    level = None

    def __init__(self):
        """ Fonction initial (constructeur) """

        # Appelle le constructeur
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("data/ennemi4.png")

        # Charge toutes les images à droite
        image = sprite_sheet.get_image(0, 0, 40, 36)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(40, 0, 40, 36)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(80, 0, 40, 36)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(120, 0, 40, 36)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Choisi avec quelle image on commence
        self.image = self.walking_frames_l[0]
 
        # Deplacement image
        self.rect = self.image.get_rect()
        self.change_x = -5
            
    def update(self):
        # Setup la gravité
        self.calc_grav()

        # Mouvement ajusté pour le décalage de l'environnement
        self.rect.x += self.change_x
        pos = self.rect.x 
        if self.direction == "L":
            self.change_x = -5
            frame = (pos // 40) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
    # Gravité
    def calc_grav(self):
        
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        #Si on est au sol
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
        
