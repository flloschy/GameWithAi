import random, pygame, time, Settings, CreateBoard
from Colors import Colors
pygame.init()

class GameLogic:
    def __init__(self):
        self.settings = Settings.Settings()
        self.board = CreateBoard.Board(randomNum=self.settings.ranNum, randomCol=self.settings.ranCol).Create()
    
    def getSettings(self): return self.settings
    def getBoard(self): return self.board

class Window:
    def __init__(self):
        self.logic = GameLogic()
        self.WIN = pygame.display.set_mode((self.logic.settings.width, self.logic.settings.height))
        pygame.display.set_caption('Quixx')



w = Window()
time.sleep(10)