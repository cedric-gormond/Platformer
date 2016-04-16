"""
Ce fichier gère toutes les fonctions et la gestion des images du personnage.
A CORRIGER:
Bug des sprites au niveau des sauts
Utiliser des sprites plus petites

A FAIRE:
Utiliser des attaques avec appuyant sur une touche (utilisation sprites + animation) 

"""
import pygame

import constants
import levels

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ Cette classe représente tous les paramètres du joueur (personnage)"""

    # -- Attributs --
    # Initialise les vecteurs mouvements
    change_x = 0
    change_y = 0

    # Créer les listes contenant les images/sprites caractéristiques aux mouvements
    walking_frames_l = []
    walking_frames_r = []
    standing_frame = []
    standing_frame_l = []
    jumping_frame = []
    jumping_frame_l = []

    # Direction initiale du joueur
    direction = "S"

    # Level
    level = None

    # -- Méthodes --
    def __init__(self):
        """ Fonction initial (constructeur) """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("data/decoupage_orange.png")

        #Standing
        image = sprite_sheet.get_image(0,0,135,135)
        self.standing_frame.append(image)

        #Standing_l
        image = sprite_sheet.get_image(0,0,135,135)
        image = pygame.transform.flip(image, True, False)
        self.standing_frame_l.append(image)

        # Charge toutes les images à droite
        image = sprite_sheet.get_image(135, 0, 135, 135)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(270, 0,135, 135)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(405, 0,135, 135)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(540, 0,135, 135)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(675, 0, 135, 135)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(810, 0, 135, 135)
        self.walking_frames_r.append(image)


        # Load all the right facing images, then flip them
        image = sprite_sheet.get_image(135, 0, 135, 135)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(270, 0, 135, 135)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(405, 0, 135, 135)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(540, 0, 135, 135)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(675, 0, 135, 135)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(810, 0, 135, 135)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        #Jumping
        image = sprite_sheet.get_image(945,0,135,135)
        self.jumping_frame.append(image)

        #Jumping_l
        image = sprite_sheet.get_image(945,0,135,135)
        image = pygame.transform.flip(image, True, False)
        self.jumping_frame_l.append(image)

        # Set the image the player starts with
        self.image = self.standing_frame[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        """ Mouvements du personnage """
        # Gravité
        self.calc_grav()

        # Mouvements avec direction
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift

        #Mvt à droite
        if self.direction == "R":
            frame = (pos // 25) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]

        #Standing
        elif self.direction == "S":
            self.image = self.standing_frame[0]

        #Standing gauche
        elif self.direction == "S_L":
            self.image = self.standing_frame_l[0] 
        #Saut
        elif self.direction == "J" :
            self.image = self.jumping_frame[0]

        #Stand gauche
        elif self.direction == "J_L":
            self.image = self.jumping_frame_l[0]

        #Sinon : mvt à gauche
        else:
            frame = (pos // 25) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .75

        # See if we are on the ground.
        """
        A corriger de nombreux problèmes de conditions"""
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            
            if self.direction == "J" and self.change_x != 0:
                self.direction = "R"
            elif self.direction == "J_L" and self.change_x != 0:
                self.direction = "L"
              
            if self.direction == "J": #a modifier
                self.direction = "S"
            elif self.direction == "J_L":
                self.direction = "S_L"
        
    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        if self.direction == "R" or self.direction == "S" or self.direction == "J":
            self.direction = "J"  
        else:
            self.direction = "J_L"
        self.rect.y += 3
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 3


        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -13

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -12
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 12
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        if self.direction == "R" or self.direction == "J":
            self.direction = "S"
        elif self.direction == "L" or self.direction == "J_L":
            self.direction = "S_L"
            
#Construire la fonction shoot
class Fireball(object):
    """Construire"""

    tir_x = 0
    tir_y = 0

    shooting_frames = []
    explosion_frames = []

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("data/tir.png")

        image = sprite_sheet.get_image(0,0,135,135)
        self.standing_frame.append(image)
