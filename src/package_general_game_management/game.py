#imports de modules éxtérieurs
import pygame
import json
from random import uniform
#imports de packages locaux :
import src.package_general_game_management
from src.package_user_elements import *

pygame.init()

class Game():
    def __init__(self):
        # Définir si notre jeu a commencé ou non
        self.is_playing = 'home'

        self.audio = src.package_general_game_management.Audio(self)
        self.comet_event = src.package_general_game_management.CometFallEvent(self)
        # Générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self, 1)
        self.all_players.add(self.player)

        self.pressed = {}

        # Groupe d'aliens
        self.aliens = pygame.sprite.Group()

        # Groupe de bonus
        self.bonuses = pygame.sprite.Group()

        self.screen = pygame.display.set_mode((1000, 600))
        self.background = pygame.image.load("../assets/img/fond.png")
        self.background_position = 0
        self.background_bis_position = -600

        self.score = 0

        self.type_vaisseau = 1

        self.velo_bg = 1

        self.spawning = src.package_general_game_management.Spawning(self)

        self.paused = False

        self.highestscore = 0

        self.username = 'None2'

        with open('../data/user/local_saves.json', 'r') as file:
            self.data = json.load(file)

        if self.username in self.data:
            self.highestscore = self.data[self.username]['highestscore']


        self.highestscore_tampon = self.data[self.username]['highestscore']


    def start(self, type_vaisseau):
        self.is_playing = 'game'
        self.type_vaisseau = type_vaisseau
        if self.type_vaisseau == 1:
            self.player = Player(self, 1)
        if self.type_vaisseau == 2:
            self.player = Player(self, 2)
        if self.type_vaisseau == 3:
            self.player = Player(self, 3)

    def game_over(self, t=0):
        # Remettre le jeu à neuf, retirer les monstres, remettre le joueur à 100 vies et remettre le jeu en attente
        self.aliens = pygame.sprite.Group()
        self.spawning.wave = 0
        self.spawning.level = 0
        self.comet_event.reset_percent()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = 'game_over_menu' if self.is_playing == 'game' else 'game'
        self.save_score(t)

    def save_score(self, t=0):
        if self.score > self.highestscore:
            self.highestscore = self.score
        if t==0:
            self.data[self.username]['highestscore'] = self.highestscore

            with open("../data/user/local_saves.json", 'w') as file:
                file.write(json.dumps(self.data, indent=4))

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # Gestion du spawn des objets
        self.spawning.spawning_run()


        # récupérer les bonus de notre jeu
        for bonus in self.bonuses:
            bonus.forward()
            # affichage du bonus en cours, si il y en a un
            bonus.left_display()
        # Récuperer les monstres de notre jeu
        for alien in self.aliens:
            alien.forward()
            alien.update_health_bar(screen)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recuperer les comètes du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Vérifier que si l'alien sort de l'écran, on le supprime et un alien réapparait
        if alien.rect.y > 600:
            alien.remove()
        try:
            # Vérifier que si le bonus sort de l'écran on le suppr
            if bonus.rect.y > 600:
                print('trouvé<;')
                bonus.remove()
        except UnboundLocalError:
            pass

        # appliquer l'ensemble des images des comètes
        self.comet_event.all_comets.draw(screen)


        # appliquer l'ensemble des images de mon groupe de monstre
        self.aliens.draw(screen)

        self.bonuses.draw(screen)

        # appliquer le score
        font_score = pygame.font.Font(None, 52)
        text_score = font_score.render(str(self.score), 1, (40, 120, 230))
        screen.blit(text_score, (880, 530))

        # Vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if self.pressed.get(pygame.K_UP) and self.player.rect.y > 450:
            self.player.move_up()
        if self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 500:
            self.player.move_down()

        if self.check_collision(self.player, self.comet_event.all_comets):
            self.player.damage(9999)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def fond_dynamique(self):
        if not self.paused:
            self.background_position += self.velo_bg
            if self.background_position != 0:
                background_bis_position = self.background

            self.background_bis_position += self.velo_bg
            if self.background_bis_position > 0:
                self.background_position = 0
                self.background_bis_position = -600

        self.screen.blit(self.background, (0, self.background_position))
        if not self.paused:
            self.screen.blit(background_bis_position, (0, self.background_bis_position))

    def update_score(self, x):
        self.score = int(self.score + ((100*x)*uniform(0.8, 1.8)))

    def set_username(self):
        self.data[self.username] = {
            "control": {
                "right": "K_RIGHT",
                "left": "K_LEFT",
                "up": "K_UP",
                "down": "K_DOWN"
            },
            "language": "french",
            "luminosity": 100,
            "resolution": [
                1000,
                600
            ],
            "volume": [
                100,
                100,
                100
            ],
            "last_vaisseau_chosen": "v1",
            "highestscore": 0
        }



