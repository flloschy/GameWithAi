import pygame
pygame.font.init()


class Settings:
    def __init__(self):
        self.width = 900
        self.height = 500

        while True:
            in1 = input("Random Colors? (True/False)\n-->   ")
            # in1 = "n"
            if in1 == "True" or in1 == "y" or in1 == "False" or in1 == "n":
                if in1 == "True" or in1 == "y":
                    in1 = True; break
                else:
                    in1 = False; break
        self.ranCol = in1

        while True:
            in2 = input("Random Numbers? (True/False)\n-->   ")
            # in2 = "n"
            if in2 == "True" or in2 == "y" or in2 == "False" or in2 == "n":
                if in2 == "True" or in2 == "y":
                    in2 = True; break
                else:
                    in2 = False; break
        self.ranNum = in2

        self.fps = 60
        self.ai = False
        self.trainai = False
        self.centeroffset = 4
        self.alpha = 255//8
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

