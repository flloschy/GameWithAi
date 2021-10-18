import pygame, sys, time

from Manager import *


class Data:
    def __init__(self):
        self.cards = Cards()
        self.textures = Textures()
        self.colors = Colors()
        self.settings = Settings()
        self.counts = Counts()

class mainGame:
    def __init__(self):
        self.data = Data()
        self.WIN = pygame.display.set_mode((self.data.settings.width, self.data.settings.height))
        self.cursor = pygame.Rect(0, 0, 1, 1)
        self.l = False
        self.m = False
        self.r = False
        pygame.display.set_caption('UNO!')
        pygame.display.set_icon(self.data.textures.wild)

    def update(self):
        pygame.display.update()
        self.WIN.fill((100, 200, 40))
        if len(self.data.cards.userCards) == 0:
            time.sleep(3)
            exit()

    def isVallid(self, card, ai=False):
        if len(self.data.cards.lastplayedcards) != 0:
            last = self.data.cards.lastplayedcards[-1]
        else:
            return True

        if last['color'] == card['color'] or last['num'] == card['num']:
            return True

        if last['red'] and card['color'] == 'red':
            return True
        elif last['blue'] and card['color'] == 'blue':
            return True
        elif last['yellow'] and card['color'] == 'yellow':
            return True
        elif last['green'] and card['color'] == 'green':
            return True

        return False

    def drawCards(self):
        def hand():
            cardwidth = 55
            allCards = self.data.cards.userCards
            x = (self.data.settings.width//2) - (len(allCards)*cardwidth//2) - 2
            y = self.data.settings.height - 120
            drawlater = []

            for card in allCards:
                if self.cursor.x in range(x, x+cardwidth):
                    if self.cursor.y in range(y, y+101):
                        if not (card in drawlater):
                            drawlater = [{'card': card, 'x': x, 'y': y}]
                            x += cardwidth
                            continue
                if not card['color'].__contains__('wild'):
                    exec(f"self.WIN.blit(self.data.textures.{card['color']}{card['num']}, ({x}, {y}))")
                else:
                    exec(f"self.WIN.blit(self.data.textures.{card['color']}, ({x}, {y}))")
                x += cardwidth

            if drawlater:
                for card in drawlater:
                    if not card['card']['color'].__contains__('wild'):
                        exec(f"self.WIN.blit(self.data.textures.{card['card']['color']}{card['card']['num']}, ({card['x']+((self.cursor.x-card['x'])//2)-20}, {card['y']-10}))")
                        if self.l:
                            if self.isVallid(card['card']):
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.cards.removeCard(card['card'])
                                break
                    else:
                        exec(f"self.WIN.blit(self.data.textures.{card['card']['color']}, ({card['x']+((self.cursor.x-card['x'])//2)-20}, {card['y']-10}))")
                        r = pygame.Rect(card['x']+cardwidth//2, card['y']+cardwidth//2, 10, 10)
                        g = pygame.Rect(card['x']+cardwidth//2-15, card['y']+cardwidth//2, 10, 10)
                        b = pygame.Rect(card['x']+cardwidth//2, card['y']+cardwidth//2-15, 10, 10)
                        y = pygame.Rect(card['x']+cardwidth//2-15, card['y']+cardwidth//2-15, 10, 10)
                        pygame.draw.rect(self.WIN, (255, 0, 0), r)
                        pygame.draw.rect(self.WIN, (0, 255, 0), g)
                        pygame.draw.rect(self.WIN, (0, 0, 255), b)
                        pygame.draw.rect(self.WIN, (250, 160, 40), y)
                        if self.l:
                            if self.cursor.colliderect(r):
                                card['card']['red'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.cards.removeCard(card['card'])
                                break
                            elif self.cursor.colliderect(g):
                                card['card']['green'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.cards.removeCard(card['card'])
                                break
                            elif self.cursor.colliderect(b):
                                card['card']['blue'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.cards.removeCard(card['card'])
                                break
                            elif self.cursor.colliderect(y):
                                card['card']['yellow'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.cards.removeCard(card['card'])
                                break


        def stack():
            last = self.data.cards.lastplayedcards
            x = self.data.settings.height//2 - 30
            y = self.data.settings.width//2 + self.data.settings.width//4 - 50
            if len(last) == 0:
                self.WIN.blit(self.data.textures.white, (x, y))
            else:
                maxindex = len(last)-1
                for index, c in enumerate(last):
                    if not c['color'].__contains__('wild'):
                        exec(f"self.WIN.blit(self.data.textures.{c['color']}{c['num']}, ({x}, {y}))")
                    else:
                        exec(f"self.WIN.blit(self.data.textures.{c['color']}, ({x}, {y}))")
                        if maxindex == index:
                            if c['red']:
                                pygame.draw.rect(self.WIN, (250, 0, 0), pygame.Rect(x-20, y, 10, 101))
                            elif c['blue']:
                                pygame.draw.rect(self.WIN, (0, 0, 255), pygame.Rect(x-20, y, 10, 101))
                            elif c['yellow']:
                                pygame.draw.rect(self.WIN, (250, 160, 40), pygame.Rect(x-20, y, 10, 101))
                            elif c['green']:
                                pygame.draw.rect(self.WIN, (0, 255, 0), pygame.Rect(x-20, y, 10, 101))
                    y -= 5




        hand()
        stack()

        # def test(self):
        #     x = 40
        #     y = 80
        #     for card in self.data.cards.userCards:
        #         if x+200 >= self.data.settings.width:
        #             y += 80
        #             x = 40
        #         exec(f"self.WIN.blit(self.data.textures.{card['color']}{card['num']}, ({x}, {y}))")
        #         x += 40

    def pickupButton(self):
        buttonWidth = len(self.data.cards.userCards) *55 + 60
        buttonHeight = 30
        x = (self.data.settings.width//2) -(buttonWidth//2) - 2
        y = self.data.settings.height -120 -buttonHeight*2

        pygame.draw.rect(self.WIN, (50, 50, 100), pygame.Rect(x, y, buttonWidth, buttonHeight))
        if self.l:
            if self.cursor.colliderect(pygame.Rect(x, y, buttonWidth, buttonHeight)):
                self.data.cards.giveCards()

    def unoButton(self):
        buttonWidth = 60
        buttonHeight = 10
        x = (self.data.settings.width//2) -(buttonWidth//2) - 2
        y = self.data.settings.height -120 -buttonHeight*2 - 50
        pygame.draw.rect(self.WIN, (100, 50, 50), pygame.Rect(x, y, buttonWidth, buttonHeight))
        if self.l:
            if self.cursor.colliderect(pygame.Rect(x, y, buttonWidth, buttonHeight)):
                if len(self.data.cards.userCards) == 1:
                    print("UNO!")
                else:
                    print("Noooo!")


game = mainGame()
game.data.cards.giveCards(am=8)

ticks = 0
while True:
    ticks += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit(1)
    x, y = pygame.mouse.get_pos()
    if ticks % 100 == 0:
        game.l, game.m, game.r = pygame.mouse.get_pressed()
    game.cursor.x = x
    game.cursor.y = y

    game.drawCards()
    game.pickupButton()
    game.unoButton()
    game.l, game.m, game.r = False, False, False
    game.update()















































































































