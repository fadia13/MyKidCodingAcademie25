import pygame

# **INITIALISER PYGAME ***
pygame.init()

# ***AFFICHER L ECRAN PRINCIPAL***
screen = pygame.display.set_mode((800, 600))

# ***creer le rectangle ***
player = pygame.Rect((300, 250, 50, 50))

run = True
# ***Boucle while*** 
while run:  
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255,0,0), player)
    key = pygame.key.get_pressed()
    # si le jouyeur appuie sur la flèche de gauche 
    # if key[pygame.K_LEFT] == True:
        # Le rectangle se déplace sur la gauche d'1 pixel
        # player.move_ip(-1, 0)

         # Le rectangle se déplace sur la droite d'1 pixel
    # elif key[pygame.K_RIGHT] == True:
    #     player.move_ip(1,0)

    #      # Le rectangle se déplace vers le pixel
    # elif key[pygame.K_UP] == True:
    #     player.move_ip(0, -1)


    #      # Le rectangle se déplace vers le pixel
    # elif key[pygame.K_DOWN] == True:
    #     player.move_ip(0, 1)


    #****************** Gestion des colisions ****************
    
    if key[pygame.K_LEFT] and player.left > 0:
        player.move_ip(-1, 0)

    elif key[pygame.K_RIGHT] and player.right < 800:
        player.move_ip(1, 0)

    elif key[pygame.K_UP] and player.top > 0:
         player.move_ip(0, -1)

    elif key[pygame.K_DOWN] and player.bottom < 600:
        player.move_ip(0, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:                  
            run = False
    pygame.display.update()

pygame.quit()




