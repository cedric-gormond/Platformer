import pygame
 
import constants
import platforms
 
class Level():
    """ Cette super classe definie tout le level et comporte deux 
        classes filles définissant chaque level """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
 
        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None
 
        # Image arrière plan
        self.background = None
 
        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("data/background_03.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        
        
        #______CONSTRUCTION LEVEL ______
        """ Cette partie du code construit le level
            en y ajoutant des plaformes statiques avec
            la méthode des 
        """    

        x_p = 0 # Pour le positionnement x des sprites 
        y_p = 0 # Pour le positionnement y des sprites
        
        level = [] #Niveau final vide

        # LE NIVEAU 
        level_p = [
        "PPPPPPPP",
        "P      P",]

        # Lecture du level_P
        for row in level_p: 
            for col in row:
                if col == "P":
                    level.append([platforms.GRASS_LEFT, x_p, y_p])
                x_p += 70 # Décale de la hauteur de la sprite platforme 
            y_p += 70 # Décale de la largeur de la sprite platforme
            x_p = 0 # Remets xp à 0   
         
        # Lecture de la platform
        for platform in level:
            block = platforms.Platform(platform[0]) # Nomenclature de la platforme : GRASS, STONE ...
            block.rect.x = platform[1] # Position x de la platforme
            block.rect.y = platform[2] # Position y de la platforme
            block.player = self.player # Prend en compte le Player
            self.platform_list.add(block) #Ajoute ce qui a été précèdement
        
        #_______PLATFORMES MOBILES______
        # Ajoute comme pour la méthode précedante une platforme mobile
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE) # Nomenclature de la platforme : GRASS, STONE ...
        block.rect.x = 1350 # Position x de la platforme
        block.rect.y = 280 # Position y de la platforme
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
 
 
# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("/data/background_02.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000
 
        # Array with type of platform, and x, y location of the platform.
        level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
                  [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
                  [platforms.STONE_PLATFORM_RIGHT, 640, 550],
                  [platforms.GRASS_LEFT, 800, 400],
                  [platforms.GRASS_MIDDLE, 870, 400],
                  [platforms.GRASS_RIGHT, 940, 400],
                  [platforms.GRASS_LEFT, 1000, 500],
                  [platforms.GRASS_MIDDLE, 1070, 500],
                  [platforms.GRASS_RIGHT, 1140, 500],
                  [platforms.STONE_PLATFORM_LEFT, 1120, 280],
                  [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
 
 
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
 
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
