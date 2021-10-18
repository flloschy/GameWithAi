from random import randint
import pygame
class Diceing:
    def __init__(self):
        self.red = randint(1, 6)
        self.yellow = randint(1, 6)
        self.green = randint(1, 6)
        self.blue = randint(1, 6)
        self.white1 = randint(1, 6)
        self.white2 = randint(1, 6)
        self.whiteblocked = False
    
    def redice(self):
        self.red = randint(1, 6)
        self.yellow = randint(1, 6)
        self.green = randint(1, 6)
        self.blue = randint(1, 6)
        self.white1 = randint(1, 6)
        self.white2 = randint(1, 6)

class cubes:
    def __init__(self):
        self.blue1 = pygame.image.load("./Textures/Blue/Blue_1.png")
        self.blue2 = pygame.image.load("./Textures/Blue/Blue_2.png")
        self.blue3 = pygame.image.load("./Textures/Blue/Blue_3.png")
        self.blue4 = pygame.image.load("./Textures/Blue/Blue_4.png")
        self.blue5 = pygame.image.load("./Textures/Blue/Blue_5.png")
        self.blue6 = pygame.image.load("./Textures/Blue/Blue_6.png")

        self.green1 = pygame.image.load("./Textures/Green/Green_1.png")
        self.green2 = pygame.image.load("./Textures/Green/Green_2.png")
        self.green3 = pygame.image.load("./Textures/Green/Green_3.png")
        self.green4 = pygame.image.load("./Textures/Green/Green_4.png")
        self.green5 = pygame.image.load("./Textures/Green/Green_5.png")
        self.green6 = pygame.image.load("./Textures/Green/Green_6.png")

        self.red1 = pygame.image.load("./Textures/Red/Red_1.png")
        self.red2 = pygame.image.load("./Textures/Red/Red_2.png")
        self.red3 = pygame.image.load("./Textures/Red/Red_3.png")
        self.red4 = pygame.image.load("./Textures/Red/Red_4.png")
        self.red5 = pygame.image.load("./Textures/Red/Red_5.png")
        self.red6 = pygame.image.load("./Textures/Red/Red_6.png")

        self.Yellow1 = pygame.image.load("./Textures/Yellow/Yellow_1.png")
        self.Yellow2 = pygame.image.load("./Textures/Yellow/Yellow_2.png")
        self.Yellow3 = pygame.image.load("./Textures/Yellow/Yellow_3.png")
        self.Yellow4 = pygame.image.load("./Textures/Yellow/Yellow_4.png")
        self.Yellow5 = pygame.image.load("./Textures/Yellow/Yellow_5.png")
        self.Yellow6 = pygame.image.load("./Textures/Yellow/Yellow_6.png")

        self.White1 = pygame.image.load("./Textures/White/White_1.png")
        self.White2 = pygame.image.load("./Textures/White/White_2.png")
        self.White3 = pygame.image.load("./Textures/White/White_3.png")
        self.White4 = pygame.image.load("./Textures/White/White_4.png")
        self.White5 = pygame.image.load("./Textures/White/White_5.png")
        self.White6 = pygame.image.load("./Textures/White/White_6.png")

        self.Checked = pygame.image.load("./Textures/Check/Checked.png")
        self.Blocked = pygame.image.load("./Textures/Check/Blocked.png")