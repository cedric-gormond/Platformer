"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    standing_frame = []
    standing_frame_l = []
    jumping_frame = []
    jumping_frame_l = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("data/decoupage.png")

        #Standing
        image = sprite_sheet.get_image(0,0,135,135)
        self.standing_frame.append(image)

        #Standing_l
        image = sprite_sheet.get_image(0,0,135,135)
        image = pygame.transform.flip(image, True, False)
        self.standing_frame_l.append(image)

        # Charge toutes les images à droite
        """
        image = sprite_sheet.get_image(x spritesheet, y spritesheet, largeur de la sprite, hauteur de sprite)
        """
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
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 25) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]

        elif self.direction == "S":
            self.image = self.standing_frame[0]

        elif self.direction == "S_L":
            self.image = self.standing_frame_l[0] 

        elif self.direction == "J" :
            self.image = self.jumping_frame[0]

        elif self.direction == "J_L":
            self.image = self.jumping_frame_l[0]

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
            self.change_y += .70

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

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
