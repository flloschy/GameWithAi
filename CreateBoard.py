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

    def Create(self):
        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            possibleColors = [
                                {'pos': 0,'hex': Colors.red(), 'left': 3},
                                {'pos': 1, 'hex': Colors.yellow(), 'left': 3},
                                {'pos': 2, 'hex': Colors.green(), 'left': 3},
                                {'pos': 3, 'hex': Colors.red(), 'left': 2}
                                ]
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    possibleColors[Col['pos']]['left'] -= 1
                                    self.line1.append({'num': num, 'color': 'red', 'hex': Col['hex']})
                                    break
                                else:
                                    possibleColors.remove(Col)
                                    continue
                                
                            break
                        else:
                            self.line1.append({'num': num, 'color': 'red', 'hex': Colors.red()})
                            break
            else:
                if self.randomCol:
                    possibleColors = [
                        {'hex': Colors.red(), 'left': 3},
                        {'hex': Colors.yellow(), 'left': 3},
                        {'hex': Colors.green(), 'left': 3},
                        {'hex': Colors.red(), 'left': 2}
                        ]
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line1.append({'num': n, 'color': 'red', 'hex': Col['hex']})
                            break
                        else:
                            possibleColors.remove(Col)
                            continue
                        
                else:
                    self.line1.append({'num': n, 'color': 'red', 'hex': Colors.red()})
                    break

        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            possibleColors = [
                                {'hex': Colors.red(), 'left': 3},
                                {'hex': Colors.yellow(), 'left': 3},
                                {'hex': Colors.green(), 'left': 3},
                                {'hex': Colors.red(), 'left': 2}
                                ]
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    Col['left'] -= 1
                                    self.line2.append({'num': num, 'color': 'red', 'hex': Col['hex']})
                                    break
                                else:
                                    possibleColors.remove(Col)
                                    continue
                                
                            break
                        else:
                            self.line2.append({'num': num, 'color': 'red', 'hex': Colors.yellow()})
                            break
            else:
                if self.randomCol:
                    possibleColors = [
                        {'hex': Colors.red(), 'left': 3},
                        {'hex': Colors.yellow(), 'left': 3},
                        {'hex': Colors.green(), 'left': 3},
                        {'hex': Colors.red(), 'left': 2}
                        ]
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line2.append({'num': n, 'color': 'red', 'hex': Col['hex']})
                            break
                        else:
                            possibleColors.remove(Col)
                            continue
                        
                else:
                    self.line2.append({'num': n, 'color': 'red', 'hex': Colors.yellow()})
                    break

        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            possibleColors = [
                                {'hex': Colors.red(), 'left': 3},
                                {'hex': Colors.yellow(), 'left': 3},
                                {'hex': Colors.green(), 'left': 3},
                                {'hex': Colors.red(), 'left': 2}
                                ]
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    Col['left'] -= 1
                                    self.line3.append({'num': num, 'color': 'red', 'hex': Col['hex']})
                                    break
                                else:
                                    possibleColors.remove(Col)
                                    continue
                                
                            break
                        else:
                            self.line3.append({'num': num, 'color': 'red', 'hex': Colors.green()})
                            break
            else:
                if self.randomCol:
                    possibleColors = [
                        {'hex': Colors.red(), 'left': 3},
                        {'hex': Colors.yellow(), 'left': 3},
                        {'hex': Colors.green(), 'left': 3},
                        {'hex': Colors.red(), 'left': 2}
                        ]
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line3.append({'num': n, 'color': 'red', 'hex': Col['hex']})
                            break
                        else:
                            possibleColors.remove(Col)
                            continue
                        
                else:
                    self.line3.append({'num': n, 'color': 'red', 'hex': Colors.green()})
                    break

        possibleNumbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for n in range(0, 11):
            if self.randomNum:
                while True:
                    num = random.randint(2, 12)
                    if num in possibleNumbers:
                        possibleNumbers.remove(num)
                        if self.randomCol:
                            possibleColors = [
                                {'hex': Colors.red(), 'left': 3},
                                {'hex': Colors.yellow(), 'left': 3},
                                {'hex': Colors.green(), 'left': 3},
                                {'hex': Colors.red(), 'left': 2}
                                ]
                            while True:
                                Col = random.choice(possibleColors)
                                if Col['left'] != 0:
                                    Col['left'] -= 1
                                    self.line4.append({'num': num, 'color': 'red', 'hex': Col['hex']})
                                    break
                                else:
                                    possibleColors.remove(Col)
                                    continue
                                
                            break
                        else:
                            self.line4.append({'num': num, 'color': 'red', 'hex': Colors.blue()})
                            break
            else:
                if self.randomCol:
                    possibleColors = [
                        {'hex': Colors.red(), 'left': 3},
                        {'hex': Colors.yellow(), 'left': 3},
                        {'hex': Colors.green(), 'left': 3},
                        {'hex': Colors.red(), 'left': 2}
                        ]
                    while True:
                        Col = random.choice(possibleColors)
                        if Col['left'] != 0:
                            Col['left'] -= 1
                            self.line4.append({'num': n, 'color': 'red', 'hex': Col['hex']})
                            break
                        else:
                            possibleColors.remove(Col)
                            continue
                        
                else:
                    self.line4.append({'num': n, 'color': 'red', 'hex': Colors.blue()})
                    break

        return [self.line1, self.line2, self.line3, self.line4]
