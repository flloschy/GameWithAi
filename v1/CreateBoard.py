import random
from Colors import Colors

class Board:
    def __init__(self, randomNum:bool=False, randomCol:bool=False):
        self.randomNum = randomNum
        self.randomCol = randomCol
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []
        self.line5 = []

    def Create(self):
        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        possibleColors = [
            {'pos': 0, 'hex': Colors.red(), 'left': 3},
            {'pos': 1, 'hex': Colors.yellow(), 'left': 3},
            {'pos': 2, 'hex': Colors.green(), 'left': 3},
            {'pos': 3, 'hex': Colors.blue(), 'left': 2}
        ]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    possibleColors[Col['pos']]['left'] -= 1
                                    self.line1.append({'num': num, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                                    break
                                else:
                                    continue
                            break
                        else:
                            self.line1.append({'num': num, 'color': 'red', 'hex': Colors.red(), 'ticked': False, 'blocked': False})
                            break
            else:
                if self.randomCol:
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line1.append({'num': n+2, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                            break
                        else:
                            continue
                else:
                    self.line1.append({'num': n+2, 'color': 'red', 'hex': Colors.red(), 'ticked': False, 'blocked': False})

        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        possibleColors = [
            {'pos': 0, 'hex': Colors.red(), 'left': 3},
            {'pos': 1, 'hex': Colors.yellow(), 'left': 3},
            {'pos': 2, 'hex': Colors.green(), 'left': 2},
            {'pos': 3, 'hex': Colors.blue(), 'left': 3}
        ]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    Col['left'] -= 1
                                    self.line2.append({'num': num, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                                    break
                                else:
                                    continue
                            break
                        else:
                            self.line2.append({'num': num, 'color': 'red', 'hex': Colors.yellow(), 'ticked': False, 'blocked': False})
                            break
            else:
                if self.randomCol:
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line2.append({'num': n+2, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                            break
                        else:
                            continue
                else:
                    self.line2.append({'num': n+2, 'color': 'red', 'hex': Colors.yellow(), 'ticked': False, 'blocked': False})

        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        possibleColors = [
            {'pos': 0, 'hex': Colors.red(), 'left': 3},
            {'pos': 1, 'hex': Colors.yellow(), 'left': 2},
            {'pos': 2, 'hex': Colors.green(), 'left': 3},
            {'pos': 3, 'hex': Colors.blue(), 'left': 3}
        ]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    Col['left'] -= 1
                                    self.line3.append({'num': num, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                                    break
                                else:
                                    continue
                            break
                        else:
                            self.line3.append({'num': num, 'color': 'red', 'hex': Colors.green(), 'ticked': False, 'blocked': False})
                            break
            else:
                if self.randomCol:
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line3.append({'num': n+2, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                            break
                        else:
                            continue
                else:
                    self.line3.append({'num': n+2, 'color': 'red', 'hex': Colors.green(), 'ticked': False, 'blocked': False})

        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        possibleColors = [
            {'pos': 0, 'hex': Colors.red(), 'left': 2},
            {'pos': 1, 'hex': Colors.yellow(), 'left': 3},
            {'pos': 2, 'hex': Colors.green(), 'left': 3},
            {'pos': 3, 'hex': Colors.blue(), 'left': 3}
        ]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    Col['left'] -= 1
                                    self.line4.append({'num': num, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                                    break
                                else:
                                    continue
                            break
                        else:
                            self.line4.append({'num': num, 'color': 'red', 'hex': Colors.blue(), 'ticked': False, 'blocked': False})
                            break
            else:
                if self.randomCol:
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line4.append({'num': n+2, 'color': 'red', 'hex': Col['hex'], 'ticked': False, 'blocked': False})
                            break
                        else:
                            continue
                else:
                    self.line4.append({'num': n+2, 'color': 'red', 'hex': Colors.blue(), 'ticked': False, 'blocked': False})



        # for n in range(0, 11):
        #     if random.randint(0, 1) == 0:
        #         self.line5.append({'num': n+2, 'color': 'red', 'hex': Colors.blue(), 'ticked': True, 'blocked': False})
        #     else:
        #         self.line5.append({'num': n+2, 'color': 'red', 'hex': Colors.blue(), 'ticked': False, 'blocked': True})

        # for x in self.line1:
        #     if random.randint(0, 1) == 1:
        #         x['ticked'] = True
        #     elif random.randint(0, 1) == 1:
        #         x['blocked'] = True

        # for x in self.line3:
        #     if random.randint(0, 1) == 1:
        #         x['ticked'] = True
        #     elif random.randint(0, 1) == 1:
        #         x['blocked'] = True

        return [self.line1, self.line2, self.line3, self.line4]
