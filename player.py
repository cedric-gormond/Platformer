"""
FICHIER : MAIN
PROJET : "A coup d'pelle !" 
NOMS :TADDEI Louis, FRANCOIS Zoé, GORMOND Cédric

Ce fichier est le 'coeur' principal du programme. Pour lancer le jeu, il faut executer ce fichier.

DESCRIPTION DU FICHIER:
Importation de plusieurs fichiers.py
Comporte une fonction main() qui contient toutes les initialisations et la boucle
permettant de faire tourner le jeu. Cette boucle ressence toutes les commandes entrées
et par l'utilisateur. Tout au long de la boucle, on fait appel à plusieurs fichier et 
à plusieurs fonctions propres au module pygame.

"""
#Importation des modules
import pygame
import constants
import levels
from player import Player # importation du fichier plyer en tant que Player

def main():
    """ Main Program """
    pygame.init()

    #Défini les dimensions
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT] #[nom_du_fichier.VARIABLE]
    screen = pygame.display.set_mode(size)

    #Titre de la fenetre
    pygame.display.set_caption("Platformer prototype")

    # Créer le joueur en important le fichier (voir importations)
    player = Player()

    # Créer les niveaux (listes)
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Met en player le niveau actuel
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Relais permettant le maintien de la boucle tant que la variable est False
    gameExit = False

    # Temps du raffraichissement de l'écran (voir FPS)
    clock = pygame.time.Clock()

    # -------- Programme : MAIN LOOP -----------
    while not gameExit:
        for event in pygame.event.get(): # Quand l'utilisation fait quelque chose
            if event.type == pygame.QUIT: # Si il clique sur 'Fermer'
                done = True # La variable relais prends la valeur True et permet la sortie

            #Quand l'utilisateur appuie sur une touche
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            #Quand l'utilisateur relâche la touche
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update le joueur
        active_sprite_list.update()

        # Affiche tous les items du niveau
        current_level.update()

        # Mvt caméra si le joueur va à droite (ici nul)
        if player.rect.x >= 0:
            diff = player.rect.x - 300 # on peut mettre (constants.SCREEN_WIDTH/2)
            player.rect.x = 300 #(constants.SCREEN_WIDTH/2)
            current_level.shift_world(-diff)

        # Mvt caméra si le joueur va à gauche (ici nul)
        if player.rect.x <= 0:
            diff = 300 - player.rect.x #(constants.SCREEN_WIDTH/2)
            player.rect.x = 300 #(constants.SCREEN_WIDTH/2)
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

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
