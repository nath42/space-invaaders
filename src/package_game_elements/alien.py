import pygame
import random

#creer une classe qui va gerer la notion de mosntre sur notre jeu
class Alien(pygame.sprite.Sprite):
    def __init__(self, game, target, velocity):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("../assets/img/jeu/alien.png")
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 800) if target == 0 else self.game.player.rect.x
        self.rect.y = random.randint(-300, -50)
        self.velocity = velocity

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        # Vérifier si son nouveau nombre de point de vie est inférieur ou égal à 0
        if self.health <= 0:
            # Réapparaitre comme un nouveau monstre
            self.remove()


        # si la barre d'evenement est chargé à son max
        if self.game.comet_event.is_full_loaded():
            # retirer du jeu
            self.game.aliens.remove(self)

            # appel de la méthode pour essayer de declencher la pluie de comete
            self.game.comet_event.attempt_fall()

    def remove(self):
        self.game.aliens.remove(self)

    def update_health_bar(self, surface):

        # Définir la position de notre jauge de vie ainsi que sa largeur et son épaisseur
        bar_position = [self.rect.x - 25, self.rect.y - 10, self.health, 5]
        # Définir la position de l'arriere plan de notre jauge de vie
        back_bar_position = [self.rect.x - 25, self.rect.y - 10, self.max_health, 5]

        # Dessiner notre barre de vie
        pygame.draw.rect(surface, (45, 36, 30), back_bar_position)
        pygame.draw.rect(surface, (235, 0, 0), bar_position)

    def forward(self):
        # Le déplacement ne se fait si il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self.game.player, self.game.aliens):
            self.rect.y += self.velocity
        else:
            # Infliger des degats (au joueur)
            self.game.player.damage(self.attack)
            print('test')