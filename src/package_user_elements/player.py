import pygame
# Créer une 1ere classe qui va représenter notre joueur
from package_user_elements import *



class Player(pygame.sprite.Sprite):
    def __init__(self, game, vaisseau_type):
        super().__init__()
        self.game = game
        
        if vaisseau_type == 1:
            self.health = 20
            self.max_health = 20
            self.attack = 1000
            self.velocity = 10
            self.image = pygame.image.load("../assets/img/jeu/V1.png")
            
        elif vaisseau_type == 2:
            self.health = 50
            self.max_health = 50
            self.attack = 10
            self.velocity = 12
            self.image = pygame.image.load("../assets/img/jeu/V2.png")
        
        elif vaisseau_type == 3:
            self.health = 75
            self.max_health = 75
            self.attack = 50
            self.velocity = 3
            self.image = pygame.image.load("../assets/img/jeu/V3.png")
        
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 450


    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # Si le joueur n'a plus de points de vie
            self.game.audio.end_music()
            self.game.audio.start_music('over')
            self.game.game_over()

    def update_health_bar(self, surface):
        # Déssiner notre barre de vie
        pygame.draw.rect(surface, (45, 36, 30), [self.rect.x - 24, self.rect.y + 100, self.max_health, 5])
        pygame.draw.rect(surface, (111, 219, 46), [self.rect.x - 24, self.rect.y + 100, self.health, 5])

    def launch_projectile(self, vaisseau_type):
        # Créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self, vaisseau_type))
        self.game.audio.make_sound('sound_laser')

    def move_right(self):
        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.aliens):
            self.rect.x += self.velocity

    def move_left(self):
        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.aliens):
            self.rect.x -= self.velocity

    def move_up(self):
        # Si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.aliens):
            self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

