import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, time
pygame.init()
from Manager import *
from termcolor import cprint as col

class Data:
    def __init__(self):
        self.cards = Cards()
        self.textures = Textures()
        self.colors = Colors()
        self.settings = Settings()
        self.font = pygame.font.SysFont("Comic Sans MS", 30)
        self.counts = Counts()

class mainGame:
    def __init__(self):
        self.data = Data()
        self.WIN = pygame.display.set_mode((self.data.settings.width, self.data.settings.height), pygame.RESIZABLE)
        self.cursor = pygame.Rect(0, 0, 1, 1)
        self.tickl = False
        self.tickm = False
        self.tickr = False
        self.reall = False
        self.realm = False
        self.realr = False
        self.move = 'player'
        self.lastmove = None
        self.tick = 0
        self.unoPressed = False
        pygame.display.set_caption('UNO!')
        pygame.display.set_icon(self.data.textures.wild)

    def update(self):
        pygame.display.update()
        self.WIN.fill((100, 200, 40))
        if len(self.data.cards.userCards) == 0:
            if self.unoPressed:
                t1 = f" You Picked up \t{self.data.counts.userPickedup}\t Cards"
                t2 = f" Ai Picked up \t{self.data.counts.aiPickedup}\t Cards"
                if len(t1) > len(t2):   l = "- "*((len(t1) - 11)//2)
                else:                          l = "- "*((len(t2) - 11)//2)
                col(f"{l} YOU WON {l}", "yellow")
                col(f" Cards Played: \t{self.data.counts.playedcards}", "cyan")
                col(t1, "cyan")
                col(t2, "cyan")
                col(f"{l} YOU WON {l}", "yellow")
                exit()
            else:
                self.data.cards.giveCards(2)
        
        if len(self.data.cards.aiCards) == 0:
            t1 = f" You Picked up \t{self.data.counts.userPickedup}\t Cards"
            t2 = f" Ai Picked up \t{self.data.counts.aiPickedup}\t Cards"
            if len(t1) > len(t2):   l = "- "*((len(t1) - 10)//2)
            else:                          l = "- "*((len(t2) - 10)//2)
            col(f"{l} AI WON {l}", "yellow")
            col(f" Cards Played: \t{self.data.counts.playedcards}", "cyan")
            col(t1, "cyan")
            col(t2, "cyan")
            col(f"{l} AI WON {l}", "yellow")
            exit()

    def isVallid(self, card):
        if self.move != 'player': return False
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
            if len(allCards)*cardwidth >= self.data.settings.width-cardwidth-cardwidth:
                while True:
                    if len(allCards)*cardwidth < self.data.settings.width-cardwidth-cardwidth:
                        break
                    cardwidth -= 1
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
                        if self.tickl:
                            if self.isVallid(card['card']):
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.counts.playedcards += 1
                                self.data.cards.removeCard(card['card'])
                                if card['card']['num'] == 'card':
                                    self.data.cards.giveCards(2, ai=True)
                                if card['card']['num'] == 'blocked':
                                    self.move = 'player'
                                else:
                                    self.move = 'ai'
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
                        pygame.draw.rect(self.WIN, (215, 224, 29), y)
                        if self.tickl:
                            if self.cursor.colliderect(r):
                                card['card']['red'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.counts.playedcards += 1
                                self.data.cards.removeCard(card['card'])
                                if card['card']['color'] == 'wild4':
                                    self.data.cards.giveCards(4, ai=True)
                                if card['card']['num'] == 'blocked':
                                    self.move = 'player'
                                else:
                                    self.move = 'ai'
                                break
                            elif self.cursor.colliderect(g):
                                card['card']['green'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.counts.playedcards += 1
                                self.data.cards.removeCard(card['card'])
                                if card['card']['color'] == 'wild4':
                                    self.data.cards.giveCards(4, ai=True)
                                if card['card']['num'] == 'blocked':
                                    self.move = 'player'
                                else:
                                    self.move = 'ai'
                                break
                            elif self.cursor.colliderect(b):
                                card['card']['blue'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.counts.playedcards += 1
                                self.data.cards.removeCard(card['card'])
                                if card['card']['color'] == 'wild4':
                                    self.data.cards.giveCards(4, ai=True)
                                if card['card']['num'] == 'blocked':
                                    self.move = 'player'
                                else:
                                    self.move = 'ai'
                                break
                            elif self.cursor.colliderect(y):
                                card['card']['yellow'] = True
                                self.data.cards.lastplayedcards.append(card['card'])
                                self.data.counts.playedcards += 1
                                self.data.cards.removeCard(card['card'])
                                if card['card']['color'] == 'wild4':
                                    self.data.cards.giveCards(4, ai=True)
                                if card['card']['num'] == 'blocked':
                                    self.move = 'player'
                                else:
                                    self.move = 'ai'
                                break

        def stack():
            cardsize = 40
            last = self.data.cards.lastplayedcards
            if len(last)*cardsize >= self.data.settings.height//3:
                while True:
                    if len(last)*cardsize < self.data.settings.height//3:
                        break
                    cardsize -= 1
            x = self.data.settings.width//2 -30
            y = self.data.settings.height -250
            if len(last) == 0:
                self.WIN.blit(self.data.textures.white, (x, y))
            elif len(last) > 20 or self.move == 'remove stack':
                if self.move != 'remove stack':
                    self.lastmove = str(self.move)
                self.move = 'remove stack'
                if self.tick % self.data.settings.fps//4 == 0:
                    self.data.cards.lastplayedcards.remove(self.data.cards.lastplayedcards[0])
                    if len(self.data.cards.lastplayedcards) == 2:
                        self.move = str(self.lastmove)
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
                            pygame.draw.rect(self.WIN, (215, 224, 29), pygame.Rect(x-20, y, 10, 101))
                        elif c['green']:
                            pygame.draw.rect(self.WIN, (0, 255, 0), pygame.Rect(x-20, y, 10, 101))
                y -= cardsize

        def aihand():
            cardwidth = 55
            allCards = self.data.cards.aiCards
            if len(allCards)*cardwidth >= self.data.settings.width-cardwidth-cardwidth:
                while True:
                    if len(allCards)*cardwidth < self.data.settings.width-cardwidth-cardwidth:
                        break
                    cardwidth -= 1
            x = (self.data.settings.width//2) - (len(allCards)*cardwidth//2) - 2
            y = 120
            for card in allCards:
                self.WIN.blit(self.data.textures.black, (x, y))
                x += cardwidth

        def openaihand():
            cardwidth = 55
            allCards = self.data.cards.aiCards
            if len(allCards)*cardwidth >= self.data.settings.width-cardwidth-cardwidth:
                while True:
                    if len(allCards)*cardwidth < self.data.settings.width-cardwidth-cardwidth:
                        break
                    cardwidth -= 1
            x = (self.data.settings.width//2) - (len(allCards)*cardwidth//2) - 2
            y = 220
            for card in allCards:
                # self.WIN.blit(self.data.textures.black, (x, y))
                if not card['color'].__contains__('wild'):
                    exec(f"self.WIN.blit(self.data.textures.{card['color']}{card['num']}, ({x}, {y}))")
                else:
                    exec(f"self.WIN.blit(self.data.textures.{card['color']}, ({x}, {y}))")
                x += cardwidth

        hand()
        aihand()
        # openaihand()
        stack()

    def pickupButton(self):
        buttonWidth = 50
        buttonHeight = 50
        x = (self.data.settings.width//2) -(buttonWidth//2) + 60
        y = self.data.settings.height -120 -buttonHeight*2
        self.WIN.blit(self.data.textures.pick, (x, y))
        if self.move == 'ai': return
        if self.cursor.colliderect(pygame.Rect(x, y, buttonWidth, buttonHeight)):
            if self.reall:
                self.WIN.blit(self.data.textures.pickPressed, (x, y))
                if self.tickl:
                    self.data.cards.giveCards()
                    self.data.counts.userPickedup += 1
                    self.move = 'ai'

    def unoButton(self):
        buttonWidth = 50
        buttonHeight = 50
        x = (self.data.settings.width//2) -(buttonWidth//2) - 60
        y = self.data.settings.height -120 -buttonHeight*2
        self.WIN.blit(self.data.textures.uno, (x, y))
        l = len(self.data.cards.userCards)
        if self.cursor.colliderect(pygame.Rect(x, y, buttonWidth, buttonHeight)):
            if self.move == 'player':
                if self.tickl:
                    if l == 1:
                        self.WIN.blit(self.data.textures.unoPressed, (x, y))
                        self.unoPressed = True
                    else:
                        self.data.cards.giveCards()


        if not (l == 1 or l == 0):
            self.unoPressed = False

    def ShowTurn(self):
        if self.move == 'player':
            text = self.data.font.render('Your Turn', False, (255, 255, 255))
        elif self.move == 'ai':
            text = self.data.font.render("Ai's Turn", False, (255, 255, 255))
        elif self.move == 'remove stack':
            text = self.data.font.render("Clearing Stack", False, (255, 255, 255))
        else:
            text = self.data.font.render("???", False, (255, 255, 255))
        x, y = self.data.settings.width//2 - text.get_width()//2, 10
        text.get_width()
        self.WIN.blit(text, (x, y))

    # Hardcodedai -> not learning

    def ai(self):
        if self.move != 'ai': return


        def isVallid2(card):
            if self.move == 'player': return False
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

        def posiblecards():
            posib = []
            for card in self.data.cards.aiCards:
                if isVallid2(card):
                    posib.append(card)
                elif 'wild4' == card['color'] or 'wild' == card['color']:
                    posib.append(card)
            return posib

        def bestMove(cards):
            red = []
            yellow = []
            green = []
            blue = []
            wild = []
            for card in cards:
                if card['color'] == 'red': red.append(card)
                elif card['color'] == 'yellow': yellow.append(card)
                elif card['color'] == 'green': green.append(card)
                elif card['color'] == 'blue': blue.append(card)
                elif 'wild' == card['color'] or card['color'] == 'wild4': wild.append(card)

            rating = {len(red):'red', len(yellow):'yellow', len(green):'green', len(blue):'blue', len(wild):'wild'}
            most = rating.get(max(rating))
            
            if most == 'red':
                for r in red:
                    if r['num'] == 'card':
                        return r
                else:
                    for r in red:
                        if r['num'] == 'blocked':
                            return r
                    else: 
                        return random.choice(red)
            elif most == 'yellow':
                for y in yellow:
                    if y['num'] == 'card':
                        return y
                else:
                    for y in yellow:
                        if y['num'] == 'blocked':
                            return y
                    else:
                        return random.choice(yellow)
            elif most == 'green':
                for g in green:
                    if g['num'] == 'card':
                        return g
                else:
                    for g in green:
                        if g['num'] == 'blocked':
                            return g
                    else:
                        return random.choice(green)
            elif most == 'blue':
                for b in blue:
                    if b['num'] == 'card':
                        return b
                else:
                    for b in blue:
                        if b['num'] == 'blocked':
                            return b
                    else:
                        return random.choice(blue)
            elif most == 'wild':
                r = sorted(set(rating.values()), reverse=True)[-2]
                for w in wild:
                    if w['color'] == 'wild4':
                        if r[1] == 'red':
                            w['red'] = True
                            return w
                        elif r[1] == 'yellow':
                            w['yellow'] = True
                            return w
                        elif r[1] == 'green':
                            w['green'] = True
                            return w
                        elif r[1] == 'blue':
                            w['blue'] = True
                            return w
                else:
                    if len(wild) != 0:
                        c = random.choice(wild)
                        if r[1] == 'red':
                            c['red'] = True
                            return c
                        elif r[1] == 'yellow':
                            c['yellow'] = True
                            return c
                        elif r[1] == 'green':
                            c['green'] = True
                            return c
                        elif r[1] == 'blue':
                            c['blue'] = True
                            return c
                        else:
                            r = random.randint(0, 3)
                            if r == 0:
                                c['blue'] = True
                            elif r == 1:
                                c['yellow'] = True
                            elif r == 2:
                                c['yellow'] = True
                            elif r == 3:
                                c['green'] = True
                            return c
                    else:
                        return 'pickup'

            return random.choice(cards)

        def getMove():
            cards = posiblecards()
            if len(cards) == 0:
                return 'pickup'
            return bestMove(cards)

        def play():
            move = getMove()
            if move == 'pickup':
                self.data.cards.giveCards(ai=True)
                self.data.counts.aiPickedup += 1
                self.move = 'player'
            else:
                self.data.cards.removeCard(move, ai=True)
                self.data.cards.lastplayedcards.append(move)
                self.data.counts.playedcards += 1
                if move['color'] == 'wild4':
                    self.data.cards.giveCards(4)
                elif move['num'] == 'card':
                    self.data.cards.giveCards(2)
                if move['num'] == 'blocked':
                    self.move = 'ai'
                else:
                    self.move = 'player'

        play()



def main():
    game = mainGame()
    game.data.cards.giveCards(am=8)
    game.data.cards.giveCards(am=8, ai=True)
    game.tick = 0
    lastswitch = 0
    last = False
    clock = pygame.time.Clock()
    while True:
        clock.tick(game.data.settings.fps)
        game.tick += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                exit()
            if event.type == pygame.VIDEORESIZE:
                game.data.settings.height = event.h
                game.data.settings.width = event.w
        x, y = pygame.mouse.get_pos()
        if last != any(pygame.mouse.get_pressed()):
            game.tickl, game.tickm, game.tickr = pygame.mouse.get_pressed()
            last = any((game.tickl, game.tickm, game.tickr))
        game.reall, game.realm, game.realr = pygame.mouse.get_pressed()
        game.cursor.x = x
        game.cursor.y = y

        game.drawCards()
        game.pickupButton()
        game.unoButton()
        if game.tick % game.data.settings.fps == 0:
            game.ai()
        game.tickl, game.tickm, game.tickr = False, False, False
        game.ShowTurn()
        game.update()

if __name__ == '__main__':
    main()
