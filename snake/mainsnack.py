import pygame
import random
import sys

# -----------------------------
# Paramètres du jeu
# -----------------------------
window = 500        # Taille de la fenêtre (carrée : 500x500)
tile_size = 50      # Taille des cases de la grille

# Plage de positions possibles pour aligner serpent/nourriture sur la grille
position_range = (tile_size // 2, window - tile_size // 2, tile_size)

# Générer une position aléatoire alignée sur la grille
get_random_position = lambda: [random.randrange(*position_range), random.randrange(*position_range)]

# -----------------------------
# Initialisation du serpent
# -----------------------------
snake = pygame.Rect([0, 0, tile_size - 2, tile_size - 2])  # rectangle pour la tête
snake.center = get_random_position()  # position de départ aléatoire

length = 1                          # longueur initiale
snake_dir = (0, 0)                  # direction initiale (immobile)
segments = [snake.copy()]           # segments du serpent (liste de Rect)

time, time_step = 0, 110            # gestion du timing (ms)

# -----------------------------
# Nourriture (pomme)
# -----------------------------
food = snake.copy()
food.center = get_random_position()

# Charger une image de pomme rouge (assure-toi que "apple.png" existe dans ton projet)
apple_img = pygame.image.load("snake/apple.png")
apple_img = pygame.transform.scale(apple_img, (tile_size, tile_size))  # redimensionner à la taille de la grille

# -----------------------------
# Initialisation de Pygame
# -----------------------------
pygame.init()
screen = pygame.display.set_mode([window, window])
pygame.display.set_caption("Snake by MyKidCodingAcademie 🐍🍎")
clock = pygame.time.Clock()

# Police pour afficher "PERDU"
font = pygame.font.SysFont("Arial", 40, bold=True)

# -----------------------------
# Boucle principale du jeu
# -----------------------------
while True:
    # ---- Gestion des événements ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion du clavier
        if event.type == pygame.KEYDOWN:
            # On interdit le demi-tour (ex: aller à droite puis directement à gauche)
            if event.key == pygame.K_UP and snake_dir != (0, tile_size):
                snake_dir = (0, -tile_size)
            if event.key == pygame.K_DOWN and snake_dir != (0, -tile_size):
                snake_dir = (0, tile_size)
            if event.key == pygame.K_LEFT and snake_dir != (tile_size, 0):
                snake_dir = (-tile_size, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-tile_size, 0):
                snake_dir = (tile_size, 0)

    # ---- Déplacement du serpent (toutes les 110ms) ----
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)         # Déplacement de la tête
        segments.append(snake.copy())    # Ajouter un nouveau segment
        segments = segments[-length:]    # Garder la longueur correcte

    # ---- Conditions de perte ----
    # 1. Si le serpent sort de l'écran
    out_of_bounds = (
        snake.left < 0 or snake.right > window or
        snake.top < 0 or snake.bottom > window
    )

    # 2. Si le serpent se mord la queue
    self_eating = snake.collidelist(segments[:-1]) != -1

    if out_of_bounds or self_eating:
        # Afficher "PERDU"
        screen.fill("black")
        text = font.render("PERDU !", True, (255, 0, 0))
        screen.blit(text, (window // 2 - text.get_width() // 2, window // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Attendre 2 secondes

        # Réinitialiser le jeu
        snake.center = get_random_position()
        food.center = get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]

    # ---- Quand le serpent mange la pomme ----
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # ---- Affichage ----
    screen.fill("black")  # fond noir

    # Afficher la pomme (image au lieu d’un carré rouge)
    screen.blit(apple_img, food.topleft)

    # Afficher le serpent
    for segment in segments:
        pygame.draw.rect(screen, "green", segment)

    pygame.display.flip()
    clock.tick(60)  # limite FPS (fluide)
