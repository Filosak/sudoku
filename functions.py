import random
import time
import pygame


# functions for drawing on screeen
class DrawingFunctions:
    def __init__(self, font, size):
        self.font = font
        self.size = size

    def drawText(self, y, x, screen, color, matrix):
        box_x = self.size * x + 5 + (x // 3) * 5
        box_y = self.size * y + 5 + (y // 3) * 5

        text = self.font.render(matrix[y][x], True, color)
        screen.blit(text, (box_x+10, box_y))


    def drawBox(self, y, x, screen, matrix, color, box_color=(255,255,255)):
        box_x = self.size * x + 5 + (x // 3) * 5
        box_y = self.size * y + 5 + (y // 3) * 5

        pygame.draw.rect(screen, box_color, pygame.Rect(box_x, box_y, self.size-5, self.size-5))
        self.drawText(y, x, screen, color ,matrix)


    def drawMatrix(self, screen, matrix, color=(0,0,0)):
        for y in range(0, 9):
            for x in range(0, 9):
                self.drawBox(y, x, screen, matrix, color)



# functions for every sudoku oriented function
class SudokuFunctions:
    def __init__(self, screen):
        self.screen = screen


    # creates new sudoku matrix and returns it
    def createMatrix(self, chance):
        matrix = [[""] * 9 for _ in range(9)]
        
        def Solver(y, x):
            aviable = self.checkAviable(y, x, matrix)

            if matrix[y][x] == "":
                for i in range(0, len(aviable)):
                    curr = random.choice(aviable)

                    matrix[y][x] = curr
                    aviable.remove(curr)

                    if y == 8 and x == 8:
                        return True
                    if x == 8:
                        flag = Solver(y+1, 0)
                    else:
                        flag = Solver(y, x+1)

                    if flag == False:
                        continue
                    else:
                        return True
            else:
                if y == 8 and x == 8:
                    return True
                if x == 8:
                    return Solver(y+1, 0)
                else:
                    return Solver(y, x+1)

            matrix[y][x] = ""
            return False

        Solver(0, 0)

        for y in range(0, 9):
            for x in range(0, 9):
                if random.randint(0,10) <= chance:
                    matrix[y][x] = ""

        return matrix


    # returns array of aviable numbers ["1", "2", "5", "8"]
    def checkAviable(self, y, x, matrix): 
        aviable = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # checks in what 3x3 box were currently in # y = 5 x = 4 box_y = 3 box_x = 3
        box_y = (y // 3) * 3 
        box_x = (x // 3) * 3

        for i in range(box_y, box_y+3):
            for j in range(box_x, box_x+3):
                curr = matrix[i][j]

                if curr in aviable:
                    aviable.remove(curr)

        # checks verticaly and horizontaly aviable nums
        for i in range(0, 9):
            curr = matrix[i][x]
            if curr in aviable:
                aviable.remove(curr)
        for i in range(0, 9):
            curr = matrix[y][i]
            if curr in aviable:
                aviable.remove(curr) 

        return aviable



    def clicked_box(self, y, x, matrix, size, font):
        start_x = 700
        start_y = 400

        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(start_x, start_y, size*3+5, size*3))
        aviable = self.checkAviable(y, x, matrix)

        pos_x = 0
        pos_y = 0

        final = []
        final.append([y, x])

        for item in aviable:
            kms_x = start_x+5+pos_x*size
            kms_y = start_y+5+pos_y*size

            curr_rect = pygame.Rect(kms_x, kms_y, size-5, size-5)
            pygame.draw.rect(self.screen, (255,255,255), curr_rect)

            number = font.render(item, True, (255,0,0))
            self.screen.blit(number, (kms_x+5, kms_y+5))

            pos_x += 1
            if pos_x % 3 == 0:
                pos_y += 1
                pos_x = 0
            
            final.append([curr_rect, item])

        return final


    def solve_sudoku(self, matrix, font, size):
        def solve(y, x):
            if matrix[y][x] == "":
                aviable = self.checkAviable(y, x, matrix)

                for item in aviable:
                    matrix[y][x] = item
                    DrawingFunctions(font, size).drawBox(y, x, self.screen, matrix, (255,0,0))

                    if x == 8 and y == 8:
                        return True
                    elif x == 8:
                        flag = solve(y+1, 0)
                    else:
                        flag = solve(y, x+1)

                    if flag == False:
                        matrix[y][x] = ""
                        continue
                    else:
                        return True
            else:
                if x == 8 and y == 8:
                    return True
                elif x == 8:
                    return solve(y+1, 0)
                else:
                    return solve(y, x+1)
            
            DrawingFunctions(font, size).drawBox(y, x, self.screen, matrix, (255,0,0))
            pygame.display.update()
            if matrix[y][x] == "":
                return False
            else:
                return True
        
        solve(0,0)
        return matrix