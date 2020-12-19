import pygame
import math
import random

enemyImgFile = pygame.image.load("./media/level0/ufo.png")

def create_enemy_list(total_enemy, enemyImg, x, y, x_change, y_change):
    empty_list(enemyImg)
    empty_list(x)
    empty_list(y)
    empty_list(x_change)
    empty_list(y_change)

    for i in range(total_enemy):
        enemyImg.append(enemyImgFile)
        x.append(random.randint(0, 735))
        y.append(random.randint(50, 150))
        x_change.append(4)
        y_change.append(40)
        
def empty_list (arr):
    i = 0
    while i < len(arr):
        arr.pop(i)