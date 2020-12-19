import pygame, sys
from blackjack_final import Blackjack
pygame.init()

class message():
    def __init__(self):
        self.running = True
        self.screen_width, self.screen_height = 1600, 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.message_font = pygame.font.Font("./fonts/Square.ttf", 40)
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.blackjack_game = Blackjack()
        self.winner = ""
        
    def display_end_message(self, winner):
        if winner == "Player":
            message = "You Won!"
        else:
            message = "Better Luck Next Time!"       
        
        render_message =  message_font(message, True, (self.WHITE))
        screen.blit(render_message, (400, 200))
        pygame.display.update()
        
    def display_message(self, text, x, y):       
        render_message =  self.message_font.render(text, True, (self.WHITE))
        self.screen.blit(render_message, (x, y))
        pygame.display.update()
        
    def loading(self):
        self.screen.fill(self.BLACK)
        render_message = self.message_font.render("Loading", True, (self.WHITE))
        self.screen.blit(render_message, (650, self.screen_height / 2))
        pygame.mixer.music.load("./sounds/loading_music.wav")
        pygame.mixer.music.play()
        pygame.display.update()
        
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.winner = self.blackjack_game.display()
                        self.running = False
        self.screen.fill(self.BLACK)
        if self.winner == "Player":
            self.screen.fill(self.BLACK)
            render_message = self.message_font.render("You Won! Good Job, Return to board soon", True, (650, self.screen_height / 2))
            pygame.display.update
        elif self.winner == "Computer":
            self.screen.fill(self.BLACK)
            render_message = self.message_font.render("Better Luck Next Time, Return to board soon", True,  (650, self.screen_height / 2))
            pygame.display.update
        pygame.mixer.music.load("./sounds/loading_music.wav")
        pygame.mixer.music.play()
        pygame.time.wait(6000)
        return self.winner
                        
    def loading_game(self):
        self.loading()
        pygame.time.wait(5000)
        self.display_message("Hit Enter to continue", 550, (self.screen_height / 2) + 200)       
        self.loop()
        
    def loading_board(self):
        self.loading()
        pygame.time.wait(5000)
        self.display_message("Hit Enter to return to game board", self.screen_width / 2, (self.screen_height / 2) + 200)       
        self.loop()
    