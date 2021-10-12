class Settings:
    def __init__(self):
        self.width = 900
        self.height = 500

        while True:
            in1 = input("Random Colors? (True/False)\n-->   ")
            try: bool(in1); break
            except: pass
        self.ranCol = bool(in1)

        while True:
            in2 = input("Random Numbers? (True/False)\n-->   ")
            try: bool(in2); break
            except: pass
        self.ranNum = bool(in2)

        self.fps = 60
        self.ai = False
        self.trainai = False
    
    def width(self): return self.width
    def height(self): return self.height
    def ranCol(self): return self.ranCol
    def ranNum(self): return self.ranNum
    def fps(self): return self.fps
    def ai(self): return self.ai
    def trainai(self): return self.trainai