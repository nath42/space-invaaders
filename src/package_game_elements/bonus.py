import pygame
from random import randint, uniform, choices
from time import time


class Bonus(pygame.sprite.Sprite):
    def __init__(self, game, shift, tag=None, activated=0):
        super().__init__()
        self.game = game
        self.player = self.game.player
        self.type = 1  # 1:Bonus/0:Malus
        self.length = 0
        self.spawn_rate = 1
        self.tag = tag
        self.image = pygame.image.load("../assets/img/jeu/heal.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image_bonus_on = pygame.image.load("../assets/img/jeu/heal.png")
        self.image_effect = pygame.image.load('../assets/img/jeu/heal.png')

        self.rect = self.image.get_rect()
        self.rect.x = randint(100, 800)
        self.rect.y = randint(-300, -50)
        self.velocity = 7
        self.shift = shift if self.rect.x <= 400 else (shift * (-1))
        self.activated = activated
        self.time = time()

    def whichtype(self):
        if self.tag == 'Heal' and self.activated == 1:
            self.image = pygame.image.load("../assets/img/jeu/heal.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.image_bonus_on = pygame.image.load("../assets/img/jeu/heal.png")
            self.image_bonus_on = pygame.transform.scale(self.image_bonus_on, (100, 100))
            #self.image_effect = pygame.image.load('../assets/img/jeu/V1.png')
            self.heal()
            self.length = 5
            self.time = time()
            self.type = 1
            self.game.audio.make_sound('sound_heal')

    def left_display(self):

        if not (self.tag == None) and self.activated == 1:
            self.game.screen.blit(self.image_bonus_on, (50, 450))
            if self.type == 1:
                font_bonus = pygame.font.Font(None, 40)
                text_bonus = font_bonus.render(str(self.tag)+ ' Bonus', 1, (255, 255, 255))
                self.game.screen.blit(text_bonus, (20, 400))
            else:
                pass
        if time() - self.time >= self.length and self.activated == 1:
            self.activated = 0
            self.remove()

    def forward(self):
        # Le déplacement ne se fait si il n'y a pas de collision avec un joueur
        if not(self.game.check_collision(self.game.player, self.game.bonuses)) and self.activated == 0:
            self.rect.y += self.velocity
            self.rect.x += self.shift
        elif self.activated == 0:
            print('flag')
            self.activated = 1
            self.rect.x += 3000
            self.whichtype()

    def remove(self):
        self.game.bonuses.remove(self)

    def heal(self):
        #self.game.screen.blit(self.image_effect, (50, 500))
        self.player.health += (0.3 * self.player.max_health)

    def shield(self):# bouclier autour du vaisseau d'une durée de 30s
        pass

    def slowness(self):#malus: speed vaisseau ---
        pass

    def speed(self):#Bonus; speed projectile + speed vaisseau
        pass

    def flashlight(self): #Malus: met un espèse de voile noir sur l'écran, sauf sur un petit cercle autour du joueur
        pass

    def explosion(self): #Malus, bombe
        pass
