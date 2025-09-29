import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))

# donner un titre à mon jeu
pygame.display.set_caption('MyGame1')
# Objet qui permet de manipuler la fréquence des frames
# Attention clock s'écrit avec un C majuscule 
clock = pygame.time.Clock()



#****Afficher  du texte à l'écran********

test_font = pygame.font.Font('Fonts/Pixelify.ttf', 50)

#************ Variable pour afficher de la couleur ************ Attention surface avec un "S" majuscule
# test_surface = pygame.Surface((100,200))
# test_surface.fill('red')
#************ Variable pour afficher une image  ************
sky_surface = pygame.image.load('images/sky.jpg').convert()
sky_surface = pygame.transform.scale(sky_surface, (800, 250))

#************ stocker  l'image du sol **************
ground_surface = pygame.image.load('images/ground.png').convert()
text_surface = test_font.render('Mon jeu', False, 'Black')

#************ stocker  l'image  l'araignée**************
spider_surface = pygame.image.load('images/spider.png').convert_alpha()
spider_x_pos = 600 



while True:
    for event in pygame.event.get():
        # surveille si le joueur clique sur le bouton fermé "x"
        if event.type == pygame.QUIT:
        
        # On demande a pygame de fermer la fenetre 
            pygame.quit()

            # utilise l'exit provenant du module importé (ligne 2)
            exit()


    #************ Variable pour afficher de la couleur ************ 
    # screen.blit(test_surface, (0,0))

    # ********Positionner  l'image dans l'écran à l'aide de coordonnées****************
    screen.blit(sky_surface , (0,0))

     # ********Afficher l'image du sol***************
    screen.blit(ground_surface , (0, 250))

    
     # ********Afficher l'image du text***************
    screen.blit(text_surface,(300, 50))


    # ********Afficher l'image l'araignée***************
    spider_x_pos -= 4
    if spider_x_pos < -100: spider_x_pos = 800
    screen.blit(spider_surface,(spider_x_pos , 177))


    pygame.display.update()
    clock.tick(60)








