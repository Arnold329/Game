import random, pygame, time

pygame.init()



screen_width, screen_height = 100, 100
screen = pygame.display.set_mode((screen_width, screen_height))
        
def display_die(nums, x, y):
    random_num = int(random.choice(nums))
    die_face_to_display = pygame.image.load("./images/dice/die_" +str(random_num) + ".png")
    screen.blit(die_face_to_display, (x, y))
    pygame.display.update()
    pygame.time.wait(500)
    return random_num
    
def roll_dice(nums, x, y):
    random_num = int(random.choice(nums))
    rolls = 0
    result = 0
    running = True
    while running:
        while rolls < 8:
            result = display_die(nums, x, y)
            rolls += 1
        return result
        

    

    
    
    
    

