import pygame
import random
import ast
pygame.init()


class Colors:
    def __init__(self):
        self.red = (235, 107, 84)
        self.yellow = (235, 227, 84)
        self.green = (84, 235, 94)
        self.blue = (84, 152, 235)

class Textures:
    def __init__(self):
        self.blue0 = pygame.image.load("./v2/Textures/Blue/0.png")
        self.blue1 = pygame.image.load("./v2/Textures/Blue/1.png")
        self.blue2 = pygame.image.load("./v2/Textures/Blue/2.png")
        self.blue3 = pygame.image.load("./v2/Textures/Blue/3.png")
        self.blue4 = pygame.image.load("./v2/Textures/Blue/4.png")
        self.blue5 = pygame.image.load("./v2/Textures/Blue/5.png")
        self.blue6 = pygame.image.load("./v2/Textures/Blue/6.png")
        self.blue7 = pygame.image.load("./v2/Textures/Blue/7.png")
        self.blue8 = pygame.image.load("./v2/Textures/Blue/8.png")
        self.blue9 = pygame.image.load("./v2/Textures/Blue/9.png")
        self.blueblocked = pygame.image.load("./v2/Textures/Blue/Blocked.png")
        self.bluecard = pygame.image.load("./v2/Textures/Blue/Cards.png")
        self.bluereverse = pygame.image.load("./v2/Textures/Blue/Reverse.png")

        self.green0 = pygame.image.load("./v2/Textures/Green/0.png")
        self.green1 = pygame.image.load("./v2/Textures/Green/1.png")
        self.green2 = pygame.image.load("./v2/Textures/Green/2.png")
        self.green3 = pygame.image.load("./v2/Textures/Green/3.png")
        self.green4 = pygame.image.load("./v2/Textures/Green/4.png")
        self.green5 = pygame.image.load("./v2/Textures/Green/5.png")
        self.green6 = pygame.image.load("./v2/Textures/Green/6.png")
        self.green7 = pygame.image.load("./v2/Textures/Green/7.png")
        self.green8 = pygame.image.load("./v2/Textures/Green/8.png")
        self.green9 = pygame.image.load("./v2/Textures/Green/9.png")
        self.greenblocked = pygame.image.load("./v2/Textures/Green/Blocked.png")
        self.greencard = pygame.image.load("./v2/Textures/Green/Cards.png")
        self.greenreverse = pygame.image.load("./v2/Textures/Green/Reverse.png")

        self.red0 = pygame.image.load("./v2/Textures/Red/0.png")
        self.red1 = pygame.image.load("./v2/Textures/Red/1.png")
        self.red2 = pygame.image.load("./v2/Textures/Red/2.png")
        self.red3 = pygame.image.load("./v2/Textures/Red/3.png")
        self.red4 = pygame.image.load("./v2/Textures/Red/4.png")
        self.red5 = pygame.image.load("./v2/Textures/Red/5.png")
        self.red6 = pygame.image.load("./v2/Textures/Red/6.png")
        self.red7 = pygame.image.load("./v2/Textures/Red/7.png")
        self.red8 = pygame.image.load("./v2/Textures/Red/8.png")
        self.red9 = pygame.image.load("./v2/Textures/Red/9.png")
        self.redblocked = pygame.image.load("./v2/Textures/Red/Blocked.png")
        self.redcard = pygame.image.load("./v2/Textures/Red/Cards.png")
        self.redreverse = pygame.image.load("./v2/Textures/Red/Reverse.png")

        self.yellow0 = pygame.image.load("./v2/Textures/Yellow/0.png")
        self.yellow1 = pygame.image.load("./v2/Textures/Yellow/1.png")
        self.yellow2 = pygame.image.load("./v2/Textures/Yellow/2.png")
        self.yellow3 = pygame.image.load("./v2/Textures/Yellow/3.png")
        self.yellow4 = pygame.image.load("./v2/Textures/Yellow/4.png")
        self.yellow5 = pygame.image.load("./v2/Textures/Yellow/5.png")
        self.yellow6 = pygame.image.load("./v2/Textures/Yellow/6.png")
        self.yellow7 = pygame.image.load("./v2/Textures/Yellow/7.png")
        self.yellow8 = pygame.image.load("./v2/Textures/Yellow/8.png")
        self.yellow9 = pygame.image.load("./v2/Textures/Yellow/9.png")
        self.yellowblocked = pygame.image.load("./v2/Textures/Yellow/Blocked.png")
        self.yellowcard = pygame.image.load("./v2/Textures/Yellow/Cards.png")
        self.yellowreverse = pygame.image.load("./v2/Textures/Yellow/Reverse.png")

        self.wild = pygame.image.load("./v2/Textures/More/Wild.png")
        self.wild4 = pygame.image.load("./v2/Textures/More/Wild+4.png")
        self.white = pygame.image.load("./v2/Textures/More/White.png")
        self.black = pygame.image.load("./v2/Textures/More/CardBackside.png")

        self.uno = pygame.image.load("./v2/Textures/Buttons/UnoButton.png")
        self.unoPressed = pygame.image.load("./v2/Textures/Buttons/UnoButtonPressed.png")
        self.pick = pygame.image.load("./v2/Textures/Buttons/PickUp.png")
        self.pickPressed = pygame.image.load("./v2/Textures/Buttons/PickUpPressed.png")

class Cards:
    def __init__(self):
        self.userCards = []
        self.aiCards = []
        self.lastplayedcards = []

    def giveCards(self, am:int=1, ai=False):
        colors = ['blue', 'red', 'yellow', 'green',
                    'blue', 'red', 'yellow', 'green',
                    'blue', 'red', 'yellow', 'green',
                    'blue', 'red', 'yellow', 'green',
                    'wild', 'wild4']
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'blocked', 'card', 'card'] #'reverse'
        for _ in range(0, am):
            card = {'color': random.choice(colors), 'num': random.choice(num), 'blue': False, 'green': False, 'red': False, 'yellow': False}
            if ai:
                self.aiCards.append(card)
            else:
                self.userCards.append(card)

    def removeCard(self, card, ai=False):
        try:
            if ai:
                self.aiCards.remove(card)
            else:
                self.userCards.remove(card)
        except: pass

    def get(self):
        return [ast.literal_eval(f"{self.aiCards}"), ast.literal_eval(f"{self.lastplayedcards}")]

class Settings:
    def __init__(self):
        self.fps = 20
        self.height = 1000
        self.width = 1000

class Counts:
    def __init__(self):
        self.playedcards = 0
        self.userPickedup = 0
        self.aiPickedup = 0
