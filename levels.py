import pygame
 
import constants
import platforms
 
class Level():
    """ Cette super class definie tout le level et comporte deux 
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
        self.world_shift_y = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
    # Update tout dans le level
    def update(self):
        """ Update tout """
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Affiche tout du level """
 
        # Affiche l'arrière plan
        # On ne bouge l'arrière plan tant que les platformes n'ont pas bougées
        screen.fill(constants.BLACK)
        screen.blit(self.background,(self.world_shift // 3,0))
 
        # Affiche toutes les sprites (platformes) quz l'on a
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

    def shift_world_y(self, shift_y):
        """Scroll quand on monte vers le haut et vers le bas"""

        self.world_shift_y += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for enemy in self.enemy_list:
            enemy.rect.y += shift_y

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        self.background = pygame.image.load("data/test_bg.png").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500
        
        
        #______CONSTRUCTION LEVEL ______
        """ Cette partie du code construit le level
            en y ajoutant des plaformes statiques avec
            la méthode "tiled
        """    

        x_paltforme = 0 # Pour le positionnement x des sprites 
        y_paltforme  = 0 # Pour le positionnement y des sprites
        
        level = [] #Niveau final vide
        decors = []

        # NIVEAU 1 
        level_tiled = [
        "                                               P",
        "P                                              P",
        "PPPP   P   2      2                            P",
        "PPP                                            P",
        "P                                              P",
        "P                                              P",
        "P                                         PPPPPP",
        "P                                              P",
        "PABCD     122    PP       ABCD                 P",
        "PEFGH                     EFGH                 P",]

        # Lecture du level_P
        for row in level_tiled: 
            for col in row:
                # Pour chaque lettre rencontrée, ajoute sa sprite correspondante:
                if col == "P": 
                    level.append([platforms.STONE_AD, x_paltforme, y_paltforme])                
                if col == "A":
                    level. append([platforms.STONE_BA, x_paltforme, y_paltforme])
                if col == "B":
                    level. append([platforms.STONE_BB, x_paltforme, y_paltforme])
                if col == "C":
                    level. append([platforms.STONE_BC, x_paltforme, y_paltforme])
                if col == "D":
                    level. append([platforms.STONE_BD, x_paltforme, y_paltforme])
                if col == "E":
                    level. append([platforms.STONE_CA, x_paltforme, y_paltforme])
                if col == "F":
                    level. append([platforms.STONE_CB, x_paltforme, y_paltforme])
                if col == "G":
                    level. append([platforms.STONE_CC, x_paltforme, y_paltforme])
                if col == "H":
                    level. append([platforms.STONE_CD, x_paltforme, y_paltforme])
                if col == "1":
                    level. append([platforms.PLATFORM1G, x_paltforme, y_paltforme])
                if col == "2":
                    level. append([platforms.PLATFORM1R, x_paltforme, y_paltforme])
                                    
                                              

                x_paltforme += 61 # Décale de la hauteur de la sprite platforme 
            y_paltforme += 61 # Décale de la largeur de la sprite platforme
            x_paltforme = 0 # Remets xp à 0   
         
        # Lecture de la platform
        # Lecture de toutes les platformes dans le level à l'aide du fichier platforms.py
        for platform in level:
            block = platforms.Platform(platform[0]) # Nomenclature de la platforme : GRASS, STONE ...
            block.rect.x = platform[1] # Position x de la platforme
            block.rect.y = platform[2] # Position y de la platforme
            block.player = self.player # Prend en compte le Player
            self.platform_list.add(block) #Ajoute ce qui a été précèdement

        for decor in decors:
            block2 = platforms.Decors(decors[0])
            block2.rect.x = platform[1]
            block2.rect.y = platform[2]
            block2.player = None
            self.platform_list.add(block2)
            
        # PLATFORMES MOBILES
        
        # PLATFORMES HORIZONTALES
        # Lecture d'une seule platforme mobile H à l'aide du fichier platforms.py
        block = platforms.MovingPlatform(platforms.PLATFORM1R) # Nomenclature de la platforme : GRASS, STONE ...
        block.rect.x            = 1830 # Position initiale x de la platforme #1350
        block.rect.y            = 488 # Position initiale y de la platforme #280
        block.boundary_left     = 1830 # Jusqu'a où va le mouvement à gauche (en x) #1350
        block.boundary_right    = 1900 # Jusqu'a où va le mouvement à droite #1600
        block.change_x          = 1 # Changement
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #PLATFORMES VERTICALES
        """
        block = platforms.MovingPlatform(platforms.STONE_PT)
        block.rect.x = 1000
        block.rect.y = 200
        block.boundary_top = 200
        block.boundary_bottom = 200
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        """

 

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
