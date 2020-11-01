import pygame
pygame.init()


class Game_over:
    def __init__(self, game):
        self.game = game


        # Charger le bouton retry
        self.retry_button = pygame.image.load("../assets/img/menu_gameover/retry.png")
        self.retry_button = pygame.transform.scale(self.retry_button, (260, 140))
        self.retry_button_rect = self.retry_button.get_rect()
        self.retry_button_rect.x = 745
        self.retry_button_rect.y = 460

        # Charger le bouton menu
        self.menu_button = pygame.image.load("../assets/img/menu_gameover/menu.png")
        self.menu_button = pygame.transform.scale(self.menu_button, (260, 140))
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.x = 10
        self.menu_button_rect.y = 460




    def update(self, screen, game, x):

        screen.blit(self.retry_button, self.retry_button_rect)
        screen.blit(self.menu_button, self.menu_button_rect)

        if game.score >= game.highestscore:
            # appliquer le current score
            font_score = pygame.font.Font(None, 60)
            text_score = font_score.render('New highest score !! Congratulations : ' + str(game.score), 1, (255, 255, 255))
            screen.blit(text_score, (100, 200))
            # appliquer la diff de score
            font_score = pygame.font.Font(None, 60)
            text_score = font_score.render('You beated your old score from ' + str(game.score - game.highestscore_tampon) + 'points', 1, (255, 255, 255))
            screen.blit(text_score, (100, 350))
        else:
            # appliquer le current score
            font_score = pygame.font.Font(None, 60)
            text_score = font_score.render('YOU ARE SO BAD :D', 1, (255, 255, 255))
            screen.blit(text_score, (340, 100))
            # appliquer le current score
            font_score = pygame.font.Font(None, 50)
            text_score = font_score.render('You didn\'t beat your score : '+str(game.score), 1, (255, 255, 255))
            screen.blit(text_score, (250, 230))
            # appliquer la diff
            font_score = pygame.font.Font(None, 50)
            text_score = font_score.render('at '+str(game.highestscore_tampon - game.score) +' from beating your highest score', 1, (255, 255, 255))
            screen.blit(text_score, (200, 350))




