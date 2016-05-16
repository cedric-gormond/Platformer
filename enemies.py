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

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("data/ennemi4.png")

        # Load all the right facing images, then flip them
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

        # Set the image the Enemy starts with
        self.image = self.walking_frames_l[0]
 
        # Reference the image rect.
        self.rect = self.image.get_rect()
        #self.rect.bottomleft = loc
        self.change_x = -5
            
    def update(self):
        # Gravity
        self.calc_grav()

        # Left/Right Movement adjusted for world shift
        self.rect.x += self.change_x
        pos = self.rect.x #+ self.level.world_shift
        if self.direction == "L":
            #if self.level.world_shift > 0:
            self.change_x = -5
            frame = (pos // 40) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
    # Gravity
    def calc_grav(self):
        
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
        
