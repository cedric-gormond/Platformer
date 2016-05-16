import pygame
import constants
import platforms 
class Level():
    """ Cette super class definie tout le level et comporte deux 
        classes filles définissant chaque level """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
 
        # Liste les sprite dans tout le niveau
        self.platform_list = None
 
        # Image arrière plan
        self.background = None
 
        # Initialisation des variables
        self.world_shift = 0
        self.world_shift_y = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.player = player
 
    # Update tout dans le level
    def update(self):
        """ Update tout """
        self.platform_list.update()

 
    def draw(self, screen):
        """ Affiche tout du level """
 
        # Affiche l'arrière plan
        # On ne bouge l'arrière plan tant que les platformes n'ont pas bougées
        screen.fill(constants.BLUE)
        screen.blit(self.background,(self.world_shift, self.world_shift_y)) # Le background ne présente aucun décalage 
 
        # Affiche toutes les sprites (platformes) quz l'on a
        self.platform_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """
 
        # Prends en compte le décalage
        self.world_shift += shift_x
 
        # Parcour toutes les platformes et les décales en fonction du mouvement
        for platform in self.platform_list:
            platform.rect.x += shift_x

    def shift_world_y(self, shift_y):
        """Scroll quand on monte vers le haut et vers le bas"""

        self.world_shift_y += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y

# Creation des platformes dans le niveau 1
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Appelle le parent constructeur
        Level.__init__(self, player)
 
        self.background = pygame.image.load("data/bg.png").convert()
        self.background.set_colorkey(constants.WHITE)
        
        #______CONSTRUCTION LEVEL ______
        """ Cette partie du code construit le level
            en y ajoutant des plaformes statiques avec
            la méthode "tiled"
        """    

        x_paltforme = 0 # Pour le positionnement x des sprites 
        y_paltforme  = 0 # Pour le positionnement y des sprites
        
        level = [] #Niveau final vide
        # NIVEAU 1 
        level_tiled = [
        "PBCBBBCBCBCBBCBCBCBCBBBBCBCCCBBCBCBBCBCBBBCBBCBCBCBBBBBBCCCCBCBCBCBBCBCBCBCBCBCBCBCCCCCD",
        "E                                                                                      H",
        "E                                                                                      H",
        "E                                                                                      H",
        "E                                                                                      H",
        "E                                                                                      H",
        "E                                                                                      H",
        "E            212                121      1      ABBCCBCCBBBCCCBBBCBBCCBCBBD     ACCBCBCL",
        "E                                                     EFGGFFGGGFFGFFGGFFFFH     H",
        "E      2                                                  IJKKJJJJKKJJKJKJL     H",
        "E                                                                               H",
        "ECD                                                                             H",
        "EGH                                                                             H",
        "EFGCD      2    2    22                               ABCCBCBCCBBBBCBCBCCCCBBBCCL",
        "EFGFFBCD                    22                      ABFFGFL",
        "EKJL                                12              E",
        "E                                          2        E",
        "E                                                   E",
        "E                                                ABCH",
        "E                                                EFGH",
        "E                                             ABCGFGH",
        "E                                             EFGFFFG",
        "EBBCD            AD       ABCD            ACBCGFFGGFF",
        "IFFGGBCBBCCBCCCCBEHCBBBCCBEFGHCCBCCBBBBBCCGFGFGFGFFGF",]

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
                if col == "I":
                    level. append([platforms.STONE_AA, x_paltforme, y_paltforme])
                if col == "J":
                    level. append([platforms.STONE_AB, x_paltforme, y_paltforme])
                if col == "K":
                    level. append([platforms.STONE_AC, x_paltforme, y_paltforme])                
                if col == "L":
                    level.append([platforms.STONE_AD, x_paltforme, y_paltforme])
                if col == "1":
                    level. append([platforms.PLATFORM1G, x_paltforme, y_paltforme])
                if col == "2":
                    level. append([platforms.PLATFORM1R, x_paltforme, y_paltforme])
                if col == "Z":
                    level.append([platforms.PICS, x_platfrome, y_platforme])
                if col == "9":
                    level.append([platforms.PUDI, x_platfrome, y_platforme])                              

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

        #Pics : 
        #1
        block = platforms.Pic1(platforms.PICS)
        block.rect.x = 3478 # Position x du pic
        block.rect.y = 367 # Position y du pic
        block.player = self.player # Prend en compte le Player
        block.level             = self
        self.platform_list.add(block)
        
        #2
        block = platforms.Pic2(platforms.PICS)
        block.rect.x = 4150 # Position x du pic
        block.rect.y = 367 # Position y du pic
        block.player = self.player # Prend en compte le Player
        block.level  = self
        self.platform_list.add(block)
        #3
        block = platforms.Pic3(platforms.PICS)
        block.rect.x = 1342 # Position x du pic
        block.rect.y = 1342 # Position y du pic
        block.player = self.player # Prend en compte le Player
        block.level  = self
        self.platform_list.add(block)

        #Pudi: 
        block = platforms.Pudi1(platforms.PUDI)
        block.rect.x = 5047 # Position x de la sprite
        block.rect.y = 360 # Position y de la sprite
        block.player = self.player # Prend en compte le Player
        block.level  = self
        self.platform_list.add(block)

        # PLATFORMES MOBILES
        
        # PLATFORMES HORIZONTALES
        # Lecture d'une seule platforme mobile H à l'aide du fichier platforms.py
        block = platforms.MovingPlatform(platforms.PLATFORM1R) # Nomenclature de la platforme : GRASS, STONE ...
        block.rect.x            = 1070 # Position initiale x de la platforme #1350
        block.rect.y            = 428 # Position initiale y de la platforme #280
        block.boundary_left     = 970 # Jusqu'a où va le mouvement à gauche (en x) #1350
        block.boundary_right    = 1875 # Jusqu'a où va le mouvement à droite #1600
        block.change_x          = 10 # Changement
        block.player            = self.player
        block.level             = self
        self.platform_list.add(block)

