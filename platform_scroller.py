"""
FICHIER : MAIN
NOMS :TADDEI Louis, FRANCOIS Zoé, GORMOND Cédric

Ce fichier est le 'coeur' principal du programme. Pour lancer le jeu, il faut executer ce fichier.

// Essais avec un controller XBOX360

"""
#Importation des modules
import pygame
import constants
import levels
from player import Player # importation du fichier player en tant que Player
from enemies import Enemy
import main_menu as Option

def main():
    """ Main Program """
    pygame.init()
    #Défini les dimensions
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT] #[nom_du_fichier.VARIABLE]
    screen = pygame.display.set_mode(size)

    #Titre de la fenetre
    pygame.display.set_caption("The pudi pudi quest")

    # Créer le joueur en important le fichier (voir importations)
    player = Player()
    enemies = Enemy()
    
    # Police
    font = pygame.font.SysFont("calibri",48)

    # Créer les niveaux (listes)
    level_list = []
    level_list.append(levels.Level_01(player))

    # Met en player le niveau actuel
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 492
    player.rect.y = 1342
    active_sprite_list.add(player)

    enemies.rect.x = 300
    enemies.rect.y = 600
    active_sprite_list.add(enemies)
    
    #Relais permettant le maintien de la boucle tant que la variable est False
    gameExit = False

    # Temps du raffraichissement de l'écran (voir FPS)
    clock = pygame.time.Clock()

    score_text = font.render("Score: ", True, constants.WHITE)
    screen.blit(score_text, (5,5))

    #Musique d'ambiance
    pygame.mixer.music.load("data/sound/ambiance.mp3")
    pygame.mixer.music.play(-1)

    # -------- Programme : MAIN LOOP -----------
    #Main    
    while not gameExit:
        for event in pygame.event.get(): # Quand l'utilisation fait quelque chose
            if event.type == pygame.QUIT: # Si il clique sur 'Fermer'
                gameExit = True # La variable relais prends la valeur True et permet la sortie

            #Quand l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Touche echap
                    gameExit = True
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
            #Quand l'utilisateur relâche la touche
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.stop()
                if event.key == pygame.K_RIGHT:
                    player.stop()
                
                        

        # Update le joueur
        active_sprite_list.update()

        # Affiche tous les items du niveau
        current_level.update()

        # Mvt caméra si le joueur va à droite (ici nul)
        if player.rect.x >= 0: #car on veut aucun décallage (sinon on met 500)
            diff = player.rect.x - 350 # on peut mettre (constants.SCREEN_WIDTH/2)
            player.rect.x = 350 # milieu de l'écran
            current_level.shift_world(-diff)

        # Mvt caméra si le joueur va à gauche (ici nul)
        if player.rect.x <= 0:
            diff = 350 - player.rect.x #(constants.SCREEN_WIDTH/2)
            player.rect.x = 350 #mileu de l'écran
            current_level.shift_world(diff)
        
        if player.rect.y <= 200:
            diff = player.rect.y - 350
            player.rect.y = 350 
            currentb_level.shift_world_y(-diff)
        
        if player.rect.y >= 200:
            diff = 350 - player.rect.y   #(constants.SCREEN_WIDTH/2)
            player.rect.y = 350 #mileu de l'écran
            current_level.shift_world_y(diff)
             
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # FPS : limités à 60
        FPS = constants.FPS
        clock.tick(FPS)

        # Update pygame de tout se qu'on a écrit 
        pygame.display.flip()

    # Sortie du programme
    pygame.quit()
    

#Lancer la boucle main()
if __name__ == "__main__":
    main()
