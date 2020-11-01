import pygame

pygame.init()
import json

class Home:
    def __init__(self, screen, game):
        self.game = game

        self.BLUE = (40, 120, 230)
        self.GREEN = (40, 230, 120)


        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Comic Sans MS,Arial', 42)
        self.prompt = self.font.render('Enter your username', True, self.BLUE)
        self.prompt_rect = self.prompt.get_rect()
        self.prompt_rect.x = 310
        self.prompt_rect.y = screen.get_height() // 2

        self.user_input_value = ""
        self.user_input = self.font.render(self.user_input_value, True, self.GREEN)
        self.user_input_rect = self.user_input.get_rect()
        self.user_input_rect.x = 360
        self.user_input_rect.y = 390

        # Charger le title
        self.banner = pygame.image.load("../assets/img/menu_principal/baniere.png")
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = 0


        # Charger la zone d'entrage du username pour lancer la partie
        self.selection_button = pygame.image.load("../assets/img/menu_principal/home.png")
        self.selection_button = pygame.transform.scale(self.selection_button, (450, 180))
        self.selection_button_rect = self.selection_button.get_rect()
        self.selection_button_rect.x = 300
        self.selection_button_rect.y = screen.get_height() // 2 + 50

        # Charger le bouton quit
        self.quit_button = pygame.image.load("../assets/img/menu_principal/quit.png")
        self.quit_button = pygame.transform.scale(self.quit_button, (150, 85))
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.x = 10
        self.quit_button_rect.y = 510

        self.data = dict()


    '''
    def check_nickname(self, nickname):

        with open('../assets/fichier.json', 'r') as file:
            self.data = json.load(file)

        if nickname in self.data:
            self.game.data = self.data
        else:
            self.data.append('nickname')
            {
                control: {right:K_RIGHT, left:K_LEFT, up:K_UP, down:K_DOWN}
                langue: 'french'
                luminosity: 100
                resolution: (1000, 600)
                volume: [100, 100, 100]
                last_vaisseau_chosen: 'V1'
                highestscore:
            }
            self.game.data = self.data

            #file.write(json.dumps(self.data, indent=4))

    '''
    def update(self, screen):

        screen.blit(self.banner, (self.banner_rect))
        screen.blit(self.selection_button, self.selection_button_rect)
        screen.blit(self.quit_button, self.quit_button_rect)

        screen.blit(self.prompt, self.prompt_rect)
        screen.blit(self.user_input, self.user_input_rect)


        self.clock.tick(30)


