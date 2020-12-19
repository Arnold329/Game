import pygame, random, sys, time
pygame.init()


class Blackjack():
    def __init__(self):
        self.running = True
        self.offset = -100
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        self.suite = "1234"
        self.player_cards = []
        self.dealer_cards = []
        self.player_cards_num = []
        self.dealer_cards_num = []
        self.player_total = 0
        self.dealer_total = 0
        self.player_card_count = 0
        self.dealer_card_count = 0
        self.screen_width, self.screen_height = 1600, 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.card_distance_x, self.card_distance_y = 200, 600
        self.background = pygame.image.load("./images/blackjack_screen.png")
        self.screen_mid_x, self.screen_mid_y = 400, 400
        self.message_font = pygame.font.Font("./fonts/Square.ttf", 40)



    def display_message(self, text, x, y):       
        render_message =  self.message_font.render(text, True, (self.WHITE))
        self.screen.blit(render_message, (x, y))
        pygame.display.update()
        
    def event_loop(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    self.player_hit_card()
                if event.key == pygame.K_s:
                    self.dealer_ai()

    def display_deck(self):
        deck = pygame.image.load("./images/cards/card_back.png")
        self.screen.blit(deck, (self.screen_mid_x, self.screen_mid_y))
        pygame.mixer.music.load("./sounds/card_shuffling.wav")
        pygame.mixer.music.play()
        pygame.time.wait(5000)
        
    def initiate(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.background, (0,0))
        self.roll_cards()
        self.display_deck()
        self.display_cards()


    def display(self):
        self.initiate()
        winner = ""
        while self.running:
            if self.determine_player_blackjack():
                return "Player"
            elif self.determine_dealer_blackjack():
                return "Computer"
            self.event_loop()
            pygame.display.update()
        winner = self.determine_winner()
        if winner == "Tie":
            self.display_message("It was a Tie this time", 1000, 600)
        else:
            self.display_message(winner + " Won!", 1000, 600)
        pygame.time.wait(2000)
        return winner
            
        
                
    def roll_cards(self):
        roll = 0
        while roll < 2:
            player_randnum = int (random.choice(self.num))
            player_randsuites = random.choice(self.suite)
            self.player_cards_num.append(player_randnum)
            player_randcard = pygame.image.load("./images/cards/card_" + str(player_randnum) + "_" + str(player_randsuites) + ".png")
            self.player_cards.append(player_randcard)
            if player_randnum > 10:
                self.player_total += 10
            else: 
                self.player_total += player_randnum
            
            dealer_randnum = int (random.choice(self.num))
            dealer_randsuites = random.choice(self.suite)
            self.dealer_cards_num.append(dealer_randnum)
            dealer_randcard = pygame.image.load("./images/cards/card_" + str(dealer_randnum) + "_" + str(dealer_randsuites) + ".png")
            self.dealer_cards.append(dealer_randcard)
            if dealer_randnum > 10:
                self.dealer_total += 10
            else: 
                self.dealer_total += dealer_randnum
            
            roll += 1   
        self.dealer_cards[1] = pygame.image.load("./images/cards/card_back.png")

            
    def reveal_card(self):
        randnum =  self.dealer_cards_num[1]
        randsuites = random.choice(self.suite)
        dealer_hidden_card = pygame.image.load("./images/cards/card_" + str(randnum) + "_" + str(randsuites) + ".png")
        self.screen.blit(dealer_hidden_card, (self.card_distance_x + 100, self.card_distance_y - 400))
        pygame.display.update()
        pygame.time.wait(1000)
        
    def player_hit_card(self):
        player_randnum = int (random.choice(self.num))
        player_randsuites = random.choice(self.suite)
        player_randcard = pygame.image.load("./images/cards/card_" + str(player_randnum) + "_" + str(player_randsuites) + ".png")
        self.player_cards.append(player_randcard)
        self.screen.blit(player_randcard, (self.card_distance_x + (len(self.player_cards) * 100), self.card_distance_y))
        
    def dealer_hit_card(self):
        dealer_randnum = int (random.choice(self.num))
        dealer_randsuites = random.choice(self.suite)
        dealer_randcard = pygame.image.load("./images/cards/card_" + str(dealer_randnum) + "_" + str(dealer_randsuites) + ".png")
        self.dealer_cards.append(dealer_randcard)
        self.dealer_total += dealer_randnum
        self.screen.blit(dealer_randcard, (self.card_distance_x + (len(self.dealer_cards) * 100), self.card_distance_y - 400))

                
    def display_cards(self):
        
        self.screen.blit(self.player_cards[0], (self.card_distance_x + (0 * 100), self.card_distance_y))
        pygame.display.update()
        pygame.time.wait(1000)
        
        self.screen.blit(self.dealer_cards[0], (self.card_distance_x + (0 * 100), self.card_distance_y - 400))
        pygame.display.update()
        pygame.time.wait(1000)
        
        self.screen.blit(self.player_cards[1], (self.card_distance_x + (1 * 100), self.card_distance_y))
        pygame.display.update()
        pygame.time.wait(1000)
        
        self.screen.blit(self.dealer_cards[1], (self.card_distance_x + (1 * 100), self.card_distance_y - 400))
        pygame.display.update()
        pygame.time.wait(1000)



    def determine_player_blackjack(self):
        if 1 in self.player_cards_num:
            if 11 in self.player_cards_num:
                return True
            elif 12 in self.player_cards_num:
                return True
            elif 13 in self.player_cards_num:
                return True
            elif 10 in self.player_cards_num:
                return True
    
    def determine_dealer_blackjack(self):
        if 1 in self.dealer_cards_num:
            if 11 in self.dealer_cards_num:
                return True
            elif 12 in self.dealer_cards_num:
                return True
            elif 13 in self.dealer_cards_num:
                return True
            elif 10 in self.dealer_cards_num:
                return True


    def determine_winner(self):
        winner = ""
        player_bust = self.determine_bust(self.player_total)
        computer_bust = self.determine_bust(self.dealer_total)
        if player_bust == False:
            if computer_bust == False:
                if self.player_total > self.dealer_total:
                    winner = "Player"
                else:
                    winner = "Computer"
        elif player_bust:
            if computer_bust:
                winner = "Tie"
            else:
                winner = "Computer"
        return winner

    def determine_bust(self, count):
        if count > 21:
            return True

    def dealer_ai(self):
        self.reveal_card()
        while self.dealer_total < 16:
            self.dealer_hit_card()
        if self.dealer_total > 16:
            self.determine_bust(self.dealer_total)
        self.running = False
