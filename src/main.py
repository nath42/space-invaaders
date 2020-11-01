import pygame
pygame.init()
from package_general_game_management import *
from src.package_menu import *


# Générer la fenêtre de notre jeu
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((1000, 600))
surface = pygame.display.get_surface()
x, y = size = surface.get_width, surface.get_height


# Charger le jeu
game = Game()
gameover = Game_over(game)
home = Home(screen, game)
selection = Selection()
pause = Pause()
running = True
current_music = 'music_theme'
game.audio.start_music('music_theme')

# Boucle tant que cette condition est vraie
while running:

    # Appliquer l'arrière plan de notre jeu
    game.fond_dynamique()


    # Vérifier si le jeu n'a pas commencé
    if game.is_playing == 'home':
        # Ajouter mon écran de bienvenue
        game.paused = False
        current_music = 'music_theme'
        home.update(screen)
    if game.is_playing == 'selection':
        game.paused = False
        selection.update(screen, game)
    # Vérifier si notre jeu a commencé ou non
    if game.is_playing == 'game':
        game.paused = False
        # declencher les instructions de la partie
        game.update(screen)

    if game.is_playing == 'pause':
        game.paused = True
        pause.update(screen, game)

    if game.is_playing == 'game_over_menu':
        game.paused = True
        gameover.update(screen, game, x)



    pygame.display.flip()

    for event in pygame.event.get():


        # que l'event est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        # détecter si un joueur lache une touche du clavier
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                game.username = home.user_input_value
                game.is_playing = 'selection'
                game.set_username()
                game.audio.make_sound('sound_click')
                break
            elif event.key == pygame.K_BACKSPACE:
                home.user_input_value = home.user_input_value[:-1]
            else:
                home.user_input_value += event.unicode
            home.user_input = home.font.render(home.user_input_value, True, home.GREEN)
            home.user_input_rect = home.user_input.get_rect()
            home.user_input_rect.x = 360
            home.user_input_rect.y = 390


            # Détecter si la touche espace est enclenchée pour lancer un projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile(selection.type_vaisseau)

            if event.key == pygame.K_ESCAPE:
                game.audio.pause_music()
                game.audio.start_music('pause')
                game.is_playing = 'pause'

        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            game.audio.make_sound('sound_click')
            if game.is_playing == 'home':
                if home.quit_button_rect.collidepoint(event.pos):
                    running = False
                    pygame.quit()

            elif game.is_playing == 'selection':

                if selection.V1_rect.collidepoint(event.pos):
                    selection.type_vaisseau = 1
                if selection.V2_rect.collidepoint(event.pos):
                    selection.type_vaisseau = 2
                if selection.V3_rect.collidepoint(event.pos):
                    selection.type_vaisseau = 3
                if selection.play_button_rect.collidepoint(event.pos):
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')
                    game.start(selection.type_vaisseau)
                if selection.back_button_rect.collidepoint(event.pos):
                    game.is_playing = 'home'
            elif game.is_playing == 'pause':
                if pause.continue_button_rect.collidepoint(event.pos):
                    game.is_playing = 'game'
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')
                if pause.retry_button_rect.collidepoint(event.pos):
                    game.game_over(1)
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')
                if pause.menu_button_rect.collidepoint(event.pos):
                    game.audio.end_music()
                    game.audio.start_music('music_theme')
                    game.game_over(1)
                    game.is_playing = 'selection'

            elif game.is_playing == 'game_over_menu':

                if gameover.menu_button_rect.collidepoint(event.pos):
                    game.is_playing = 'selection'
                if gameover.retry_button_rect.collidepoint(event.pos):
                    game.is_playing = 'game'
                    game.audio.end_music()
                    game.audio.start_music('music_theme2')

