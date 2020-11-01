from random import choices
from src.package_game_elements import *

class Spawning():
    def __init__(self, game):
        self.game = game
        self.level = 0
        self.wave = 0
        self.velocity = 1

    def spawn_alien(self, target=0):
        alien = Alien(self.game, target, self.velocity)
        self.game.aliens.add(alien)

    def spawning_run(self):
        if not self.game.aliens:
            if self.wave == 0:
                self.spawn_alien(1)
                self.spawn_bonus(0.5)
            elif self.wave == 1 or self.wave == 5:
                for e in range(0, self.level + 2):
                    i = choices([0, 1], [75, 25], k=1)
                    self.spawn_alien(i[0])
                self.spawn_bonus(0.2)
            elif self.wave == 2 or self.wave == 3 or self.wave == 4:
                for e in range(0, self.level + 3):
                    i = choices([0, 1], [75, 25], k=1)
                    self.spawn_alien(int(i[0]))
            self.wave += 1

            print('v:', self.wave, 'd', self.level)
            self.wave = 0 if self.wave == 5 else self.wave
            if self.wave == 0:
                if not self.level > 7:
                    self.level = self.level + 1
                    self.velocity += 1
                    self.game.player.velocity += 1
                    self.game.velo_bg += 1

        else:
            return None
    def spawn_bonus(self, shift):
        self.game.bonus = Bonus(self.game, shift, 'Heal')
        self.game.bonuses.add(self.game.bonus)