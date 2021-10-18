import pygame, time, Settings, CreateBoard, sys, diceing
from termcolor import cprint as col
from Colors import Colors
pygame.font.init()
pygame.init()
col("Loaded Modules...", "yellow")

class GameLogic:
    def __init__(self):
        col("Loading Settings...", "yellow")
        self.settings = Settings.Settings()
        col("Creating Board...", "yellow")
        self.board = CreateBoard.Board(randomNum=self.settings.ranNum, randomCol=self.settings.ranCol).Create()
        self.dice = False
        self.lastdice = 0
        col("Loading dice...", "yellow")
        self.diceing = diceing.Diceing()
        col("Loading dice textures...", "yellow")
        self.textures = diceing.cubes()
        self.passed = 0
        self.combis = []
    
    def canCheck(self, num):
        if self.combis:
            for p in self.combis:
                if num['hex'] == Colors.green() or num['hex'] == Colors.blue():
                    if p['number'] == 14-num['num']:
                        if p['col'] == num['hex'] or p['col'] == None:
                            if not num['blocked']:
                                return True
                else:
                    if p['number'] == num['num']:
                        if p['col'] == num['hex'] or p['col'] == None:
                            if not num['blocked']:
                                return True


        return False

    def possible(self):
        list = []

        list.append({'number': self.diceing.white1+self.diceing.white2, 'col': None})

        list.append({'number': self.diceing.white1 + self.diceing.blue, 'col': Colors.blue()})
        list.append({'number': self.diceing.white1 + self.diceing.red, 'col': Colors.red()})
        list.append({'number': self.diceing.white1 + self.diceing.yellow, 'col': Colors.yellow()})
        list.append({'number': self.diceing.white1 + self.diceing.blue, 'col': Colors.green()})

        list.append({'number': self.diceing.white2 + self.diceing.blue, 'col': Colors.blue()})
        list.append({'number': self.diceing.white2 + self.diceing.red, 'col': Colors.red()})
        list.append({'number': self.diceing.white2 + self.diceing.yellow, 'col': Colors.yellow()})
        list.append({'number': self.diceing.white2 + self.diceing.blue, 'col': Colors.green()})

        self.combis = list

    def fixBoard(self):
        blockList = []
        for line in self.board:
            for p in line:
                if p['ticked'] == True:
                    blockList.append([line, p])

        temp = self.board.copy()
        temp.reverse()
        for line in temp:
            for p in line:
                for q in blockList:
                    if q[0] == line:
                        if q[1] == p:
                            for l in self.board:
                                if l == line:
                                    for i in l:
                                        if i != p:
                                            i['blocked'] = True
                                        else:
                                            break




class Window:
    def __init__(self):
        self.logic = GameLogic()
        col("Starting Window...", "yellow")
        self.WIN = pygame.display.set_mode((self.logic.settings.width, self.logic.settings.height))
        pygame.display.set_caption('Quixx')
    
    def update(self):
        pygame.display.update()
        time.sleep(1/self.logic.settings.fps)
        self.WIN.fill((50,50,50))

    def drawBoard(self, mX, mY, lmb):
        x = 5
        y = 5
        c = 0
        t = self.logic.settings.centeroffset
        alpha = self.logic.settings.alpha
        for line in self.logic.board:
            c += 1
            if c <= 2:
                for num in line:
                    if x in range(mX, mX+50):
                        if y in range(mY, mY+50):
                            if lmb:
                                if self.logic.canCheck(num):
                                    num['ticked'] = True
                            s = pygame.Surface((60,60))
                            s.set_alpha(alpha)
                            s.fill(num['hex'])
                            self.WIN.blit(s, (x-5, y-5))
                    pygame.draw.rect(
                        self.WIN,
                        num['hex'],
                        pygame.Rect(x, y, 50, 50)
                    )
                    text = self.logic.settings.font.render(str(num['num']), False, (0, 0, 0))
                    width, height = self.logic.settings.font.size(str(num['num'])) 
                    self.WIN.blit(text, (x+width//t, y-height//t))
                
                    if num['ticked']:
                        self.WIN.blit(self.logic.textures.Checked, (x, y))
                    elif num ['blocked']:
                        self.WIN.blit(self.logic.textures.Blocked, (x, y))
                    
                    x += 60
            else:
                for num in line:
                    if x in range(mX, mX+50):
                        if y in range(mY, mY+50):
                            if lmb:
                                if self.logic.canCheck(num):
                                    num['ticked'] = True
                            s = pygame.Surface((60,60))
                            s.set_alpha(alpha)
                            s.fill(num['hex'])
                            self.WIN.blit(s, (x-5, y-5))
                    pygame.draw.rect(
                        self.WIN,
                        num['hex'],
                        pygame.Rect(x, y, 50, 50)
                    )
                    text = self.logic.settings.font.render(str(14-num['num']), False, (0, 0, 0))
                    width, height = self.logic.settings.font.size(str(14-num['num'])) 
                    self.WIN.blit(text, (x+width//t, y-height//t))

                    if num['ticked']:
                        self.WIN.blit(self.logic.textures.Checked, (x, y))
                    elif num ['blocked']:
                        self.WIN.blit(self.logic.textures.Blocked, (x, y))
                    
                    x += 60
            x = 5
            y += 60

        self.logic.fixBoard()

    def drawDiceButton(self, mX, mY, lmb):
        x, y = 680, 5
        buttonx, buttony = 110, 50
        hoverx, hovery = 120, 60
        if not self.logic.dice:
            if mX in range(x, x+buttonx):
                if mY in range(y, y+buttony):
                    if lmb:
                        pygame.draw.rect(
                            self.WIN,
                            Colors.dicebuttonpressed(),
                            pygame.Rect(x, y, buttonx, buttony)
                        )
                        self.logic.dice = True
                        self.logic.lastdice = time.time()
                        self.logic.diceing.redice()
                    else:
                        s = pygame.Surface((hoverx, hovery))
                        s.set_alpha(self.logic.settings.alpha)
                        s.fill(Colors.dicebutton())
                        self.WIN.blit(s, (x-5, y-5))
            pygame.draw.rect(
                self.WIN,
                Colors.dicebutton(),
                pygame.Rect(x, y, buttonx, buttony)
            )
            text = self.logic.settings.font.render("DICE", False, (0,0,0))
            self.WIN.blit(text, (x+15, y+2))
        else:
            if mX in range(x, x+buttonx):
                if mY in range(y, y+buttony):
                    s = pygame.Surface((hoverx, hovery))
                    s.set_alpha(self.logic.settings.alpha)
                    s.fill(Colors.dicebuttonpressed())
                    self.WIN.blit(s, (x-5, y-5))
            pygame.draw.rect(
                self.WIN,
                Colors.dicebuttonpressed(),
                pygame.Rect(x, y, buttonx, buttony)
            )
            text = self.logic.settings.font.render("DICE", False, (255,255, 255))
            self.WIN.blit(text, (x+15, y+2))

        if time.time() - self.logic.lastdice < 1:
            self.logic.diceing.redice()
            self.logic.combis = []
        else:
            self.logic.dice = False
            self.logic.possible()

    def drawPassButtonText(self, x, y, col):
        TEXT = "nextround"
        text_x, text_y = x+16, y-12
        for char in TEXT:
            text = self.logic.settings.font.render(char, False, col)
            self.WIN.blit(text, (text_x, text_y))
            text_y += 25

    def drawPassButton(self, mX, mY, lmb):
        x, y = 810, 5
        buttonx, buttony = 50, 180+50
        hoverx, hovery = 60, 190+50
        pygame.draw.rect(
            self.WIN,
            Colors.passbutton(),
            pygame.Rect(x, y, buttonx, buttony)
        ) 
        if mX in range(x, x+buttonx):
            if mY in range(y, y+buttony):
                if lmb:
                    s = pygame.Surface((hoverx, hovery))
                    s.set_alpha(self.logic.settings.alpha)
                    s.fill(Colors.passbuttonpressed())
                    self.WIN.blit(s, (x-5, y-5))
                    pygame.draw.rect(
                        self.WIN,
                        Colors.passbuttonpressed(),
                        pygame.Rect(x, y, buttonx, buttony)
                    )
                    self.drawPassButtonText(x, y, (255, 255, 255))
                else:
                    s = pygame.Surface((hoverx, hovery))
                    s.set_alpha(self.logic.settings.alpha)
                    s.fill(Colors.passbutton())
                    self.WIN.blit(s, (x-5, y-5))
                    pygame.draw.rect(
                        self.WIN,
                        Colors.passbutton(),
                        pygame.Rect(x, y, buttonx, buttony)
                    )
                    self.drawPassButtonText(x, y, (0, 0, 0))
            else:
                self.drawPassButtonText(x, y, (0, 0, 0))
        else:
            self.drawPassButtonText(x, y, (0, 0, 0))

    def drawDice(self):
        blue_x, blue_y= 680, 65
        if self.logic.diceing.blue == 1: 
            self.WIN.blit(self.logic.textures.blue1, (blue_x, blue_y))
        elif self.logic.diceing.blue == 2: 
            self.WIN.blit(self.logic.textures.blue2, (blue_x, blue_y))
        elif self.logic.diceing.blue == 3: 
            self.WIN.blit(self.logic.textures.blue3, (blue_x, blue_y))
        elif self.logic.diceing.blue == 4: 
            self.WIN.blit(self.logic.textures.blue4, (blue_x, blue_y))
        elif self.logic.diceing.blue == 5: 
            self.WIN.blit(self.logic.textures.blue5, (blue_x, blue_y))
        elif self.logic.diceing.blue == 6: 
            self.WIN.blit(self.logic.textures.blue6, (blue_x, blue_y))

        red_x, red_y = 680, 125
        if self.logic.diceing.red == 1:
            self.WIN.blit(self.logic.textures.red1, (red_x, red_y))
        elif self.logic.diceing.red == 2:
            self.WIN.blit(self.logic.textures.red2, (red_x, red_y))
        elif self.logic.diceing.red == 3:
            self.WIN.blit(self.logic.textures.red3, (red_x, red_y))
        elif self.logic.diceing.red == 4:
            self.WIN.blit(self.logic.textures.red4, (red_x, red_y))
        elif self.logic.diceing.red == 5:
            self.WIN.blit(self.logic.textures.red5, (red_x, red_y))
        elif self.logic.diceing.red == 6:
            self.WIN.blit(self.logic.textures.red6, (red_x, red_y))

        yellow_x, yellow_y = 740, 65
        if self.logic.diceing.yellow == 1:
            self.WIN.blit(self.logic.textures.Yellow1, (yellow_x, yellow_y))
        elif self.logic.diceing.yellow == 2:
            self.WIN.blit(self.logic.textures.Yellow2, (yellow_x, yellow_y))
        elif self.logic.diceing.yellow == 3:
            self.WIN.blit(self.logic.textures.Yellow3, (yellow_x, yellow_y))
        elif self.logic.diceing.yellow == 4:
            self.WIN.blit(self.logic.textures.Yellow4, (yellow_x, yellow_y))
        elif self.logic.diceing.yellow == 5:
            self.WIN.blit(self.logic.textures.Yellow5, (yellow_x, yellow_y))
        elif self.logic.diceing.yellow == 6:
            self.WIN.blit(self.logic.textures.Yellow6, (yellow_x, yellow_y))

        green_x, green_y = 740, 125
        if self.logic.diceing.green == 1:
            self.WIN.blit(self.logic.textures.green1, (green_x, green_y))
        elif self.logic.diceing.green == 2:
            self.WIN.blit(self.logic.textures.green2, (green_x, green_y))
        elif self.logic.diceing.green == 3:
            self.WIN.blit(self.logic.textures.green3, (green_x, green_y))
        elif self.logic.diceing.green == 4:
            self.WIN.blit(self.logic.textures.green4, (green_x, green_y))
        elif self.logic.diceing.green == 5:
            self.WIN.blit(self.logic.textures.green5, (green_x, green_y))
        elif self.logic.diceing.green == 6:
            self.WIN.blit(self.logic.textures.green6, (green_x, green_y))

        white1_x, white1_y = 680, 185
        if self.logic.diceing.white1 == 1:
            self.WIN.blit(self.logic.textures.White1, (white1_x, white1_y))
        elif self.logic.diceing.white1 == 2:
            self.WIN.blit(self.logic.textures.White2, (white1_x, white1_y))
        elif self.logic.diceing.white1 == 3:
            self.WIN.blit(self.logic.textures.White3, (white1_x, white1_y))
        elif self.logic.diceing.white1 == 4:
            self.WIN.blit(self.logic.textures.White4, (white1_x, white1_y))
        elif self.logic.diceing.white1 == 5:
            self.WIN.blit(self.logic.textures.White5, (white1_x, white1_y))
        elif self.logic.diceing.white1 == 6:
            self.WIN.blit(self.logic.textures.White6, (white1_x, white1_y))

        white2_x, white2_y = 740, 185
        if self.logic.diceing.white2 == 1:
            self.WIN.blit(self.logic.textures.White1, (white2_x, white2_y))
        elif self.logic.diceing.white2 == 2:
            self.WIN.blit(self.logic.textures.White2, (white2_x, white2_y))
        elif self.logic.diceing.white2 == 3:
            self.WIN.blit(self.logic.textures.White3, (white2_x, white2_y))
        elif self.logic.diceing.white2 == 4:
            self.WIN.blit(self.logic.textures.White4, (white2_x, white2_y))
        elif self.logic.diceing.white2 == 5:
            self.WIN.blit(self.logic.textures.White5, (white2_x, white2_y))
        elif self.logic.diceing.white2 == 6:
            self.WIN.blit(self.logic.textures.White6, (white2_x, white2_y))




w = Window()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit(1)
    x, y = pygame.mouse.get_pos()
    l, m, r = pygame.mouse.get_pressed()
    w.drawBoard(x-50, y-50, l)
    w.drawDiceButton(x, y, l)
    w.drawPassButton(x, y, l)
    w.drawDice()
    w.update()