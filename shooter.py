import pygame
import math
import random
import time
import enemies
import sys

pygame.init()
class shooter():
    def __init__(self):
        # Variable Definition & Asset Loading
        # Game Screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders")

        # Background
        self.background = pygame.image.load("./media/level0/background.png")

        # Sound
        pygame.mixer.music.load("./media/level0/background.wav")
        pygame.mixer.music.play(-1)

        # Player
        self.playerImg = pygame.image.load("./media/level0/spaceship.png")
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0
        self.score_value = 0

        # Enemy
        self.enemyImgFile = pygame.image.load("./media/level0/ufo.png")
        self.enemyImg = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.num_enemies = 6  # Change this to change MAX number of enemies

        # Bullet
        self.bulletImg = pygame.image.load("./media/level0/bullet.png")
        self.bulletX = 0
        self.bulletY = 480
        self.bulletX_change = 0
        self.bulletY_change = 10
        self.bullet_state = "ready"

        # Score Board
        self.score_value = 0
        self.font = pygame.font.Font("./fonts/Square.ttf", 24)
        self.textX = 10
        self.textY = 10

    def show_score(self, x, y):
        score = self.font.render("Score: " + str(self.score_value), True, (255, 255, 255))
        self.screen.blit(score, (x, y))


    def player(self, x, y):
        self.screen.blit(self.playerImg, (x, y))


    def enemy(self, x, y, i):
        self.screen.blit(self.enemyImg[i], (x, y))


    def fire_bullet(self, x, y):
        self.bullet_state = "fire"
        self.screen.blit(self.bulletImg, (x + 16, y + 10))


    def isCollision(self, enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))

        if distance < 27:
            return True
        else:
            return False


    
    def play(self):
        # Game Loop
        enemies.create_enemy_list(self.num_enemies, self.enemyImg, self.enemyX, self.enemyY, self.enemyX_change, self.enemyY_change)
        level = 0
        level_won_at = -1
        score_thresh = 10  # the threshold taht a user's score must surpass to complete the wincon
        bonus_pts = 0
        win_con = False
        running = True
        while running:

        # Game Events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.playerX_change = -3

                    if event.key == pygame.K_RIGHT:
                        self.playerX_change = 3

                    if event.key == pygame.K_SPACE:
                        if self.bullet_state is "ready":
                            bullet_sound = pygame.mixer.Sound("./media/level" + str(level) + "/laser.wav")
                            bullet_sound.play()
                            bulletX = self.playerX
                            self.fire_bullet(self.bulletX, self.bulletY)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.playerX_change = 0

        # Screen Attributes
            self.screen.fill((0, 0, 0))
    
        # Set time for message on screen "Level x Won"
            self.screen.blit(self.background, (0, 0))
        
        # Move player based on input
            self.playerX += self.playerX_change

        # Min & Max Bounds of Player Movement
            if self.playerX <= 0:
                self.playerX = 0
            elif self.playerX >= 736:
                self.playerX = 736

        # Enemy Movement
            for i in range(self.num_enemies):

            # Game Over
                if self.enemyY[i] > 440:  # trigger the end of the game
                    for j in range(self.num_enemies):
                        self.enemyY[j] = 2000
                    break

                self.enemyX[i] += self.enemyX_change[i]
                if self.enemyX[i] <= 0:
                    self.enemyX_change[i] = 4
                    self.enemyY[i] += self.enemyY_change[i]
                elif self.enemyX[i] >= 736:
                    self.enemyX_change[i] = -4
                    self.enemyY[i] += self.enemyY_change[i]

                collision = self.isCollision(self.enemyX[i], self.enemyY[i], self.bulletX, self.bulletY)
                if collision:
                    explosion_sound = pygame.mixer.Sound("./media/level0/explosion.wav")
                    explosion_sound.play()
                    self.bulletY = 480
                    self.bullet_state = "ready"
                    self.score_value += 1
                    self.enemyX[i] = random.randint(0, 800)
                    self.enemyY[i] = random.randint(50, 150)

                    self.enemy(enemyX[i], enemyY[i], i)

        # Bullet Animation
            if self.bulletY <= 0:
                self.bulletY = 480
                self.bullet_state = "ready"

            if self.bullet_state is "fire":
                self.fire_bullet(self.bulletX, self.bulletY)
                self.bulletY -= self.bulletY_change

            self.player(self.playerX, self.playerY)
            self.show_score(self.textX, self.textY)

            pygame.display.update()
                
