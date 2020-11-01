import pygame
#from src.package_user_elements import *


# creer une classe pour gerer cet evenement
class CometFallEvent:

    # lors du chargement --> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 1
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 11):
            # apparaitre une premiere boule de feu
            self.game.audio.make_sound('sound_comet')
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'evenement est totalement chargée

         print("Pluie de comètes !")
         self.meteor_fall()
         self.fall_mode = True # activer l'event

    def reset_percent(self):
        self.percent = 0

    def update_bar(self, surface):

        #ajouter du pourcentage à la barre
        self.add_percent()

        # barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        # barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11),[0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])