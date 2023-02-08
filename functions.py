# import all the libraries
import random
import time
import pygame


# functions for drawing on screeen
class DrawingFunctions:


    # stores size of a box and the font for text
    def __init__(self, font, size):
        self.font = font
        self.size = size


    # function for drawing text into the box we want
    def drawText(self, y, x, screen, color, matrix):
        # calculates the starting possition (x, y) of the text we want
        box_x = self.size * x + 5 + (x // 3) * 5
        box_y = self.size * y + 5 + (y // 3) * 5
        
        # renders text into the box
        text = self.font.render(matrix[y][x], True, color)
        screen.blit(text, (box_x+10, box_y))


    # draw the basic box for the number to go in
    def drawBox(self, y, x, screen, matrix, color, box_color=(255,255,255)):
        # calculates the starting possition (x, y) of the box we want
        box_x = self.size * x + 5 + (x // 3) * 5
        box_y = self.size * y + 5 + (y // 3) * 5

        # renders the box with the text in the box
        pygame.draw.rect(screen, box_color, pygame.Rect(box_x, box_y, self.size-5, self.size-5))
        self.drawText(y, x, screen, color ,matrix)


    # function for drawing the whole matrix when creating a new matrix
    def drawMatrix(self, screen, matrix, color=(0,0,0)):
        for y in range(0, 9):
            for x in range(0, 9):
                self.drawBox(y, x, screen, matrix, color)





class SudokuFunctions:


    def __init__(self, screen):
        self.screen = screen


    def deleteRandom(self, matrix):
        tries = 3

        def check(y, x):
            if y == 8 and x == 8:
                return 1
            if x == 8:
                return Solver(y+1, 0)
            else:
                return Solver(y, x+1)

        def Solver_loop(y, x, aviable):
            final = 0

            for item in aviable:
                matrix[y][x] = item
                final += check(y, x)

            matrix[y][x] = ""
            return final
        
        def Solver(y, x):
            aviable = self.checkAviable(y, x, matrix)

            if matrix[y][x] == "":
                return Solver_loop(y, x, aviable)
            else:
                return check(y, x)

        while tries > 0:
            y = random.randint(0, 8)
            x = random.randint(0, 8)

            placeholder = matrix[y][x]
            matrix[y][x] = ""

            flag = Solver(0, 0)

            if flag > 1:
                matrix[y][x] = placeholder
                tries -= 1
        
        return matrix


    def checkAviable(self, y, x, matrix): 
        aviable = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        box_y = (y // 3) * 3 
        box_x = (x // 3) * 3

        for i in range(box_y, box_y+3):
            for j in range(box_x, box_x+3):
                curr = matrix[i][j]

                if curr in aviable:
                    aviable.remove(curr)

        for i in range(0, 9):
            curr = matrix[i][x]
            if curr in aviable:
                aviable.remove(curr)

        for i in range(0, 9):
            curr = matrix[y][i]
            if curr in aviable:
                aviable.remove(curr) 

        return aviable


    def createMatrix(self):
        matrix = [[""] * 9 for _ in range(9)]

        def check(y, x):
            if y == 8 and x == 8: return True
            if x == 8: return Solver(y+1, 0)
            else: return Solver(y, x+1)

        def Solver_loop(y, x, aviable):
            for _ in range(0, len(aviable)):
                matrix[y][x] = random.choice(aviable)
                aviable.remove(matrix[y][x])

                if check(y, x) == False:
                    continue
                else:
                    return True
            return False
        
        def Solver(y, x):
            aviable = self.checkAviable(y, x, matrix)

            if matrix[y][x] == "":
                if Solver_loop(y, x, aviable) == True:
                    return True

                matrix[y][x] = ""
                return False
            else:
                return check(y, x)

        Solver(0, 0)
        self.deleteRandom(matrix)
        return matrix


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