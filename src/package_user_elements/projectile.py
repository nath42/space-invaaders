import pygame

# Définir la classe qui va gerer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    # Définier le constructeur de cette classe
    def __init__(self, player, vaisseau_type):
        super().__init__()
        self.velocity = 5
        self.player = player
        
        if vaisseau_type == 1:
            self.image = pygame.image.load("../assets/img/jeu/V1_projectile.png")
            
        elif vaisseau_type == 2:
            self.image = pygame.image.load("../assets/img/jeu/V2_projectile.png")
        
        elif vaisseau_type == 3:
            self.image = pygame.image.load("../assets/img/jeu/V3_projectile.png")
        
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 30
        self.rect.y = player.rect.y

    def remove(self):
        self.player.all_projectiles.remove(self)
        #print("Projectile Supprimé")

    def move(self):
        self.rect.y -= self.velocity

        # verifier si le projectile entre en collision avec un monstre
        for alien in self.player.game.check_collision(self, self.player.game.aliens):
            # supprimer le projectile
            self.remove()
            # infliger les degats
            alien.damage(self.player.attack)
            # incrémentation du score
            self.player.game.update_score(1)

        # Vérifier si le prpjectile n'est plus présent sur l'écran
        if self.rect.y > 600:
            # Supprimer le projectile
            self.remove()