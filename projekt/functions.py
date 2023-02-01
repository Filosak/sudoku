import random
import time
import pygame


# functions for drawing on screeen
class DrawingFunctions:
    def drawBox(self, y, x, width, screen, matrix):
        # calculates the starting cordinates of each square and draws it
        size = (width // 9)
        box_x = size * x + 5
        box_y = size * y + 5

        font2 = pygame.font.SysFont("calibri", 72)
        img2 = font2.render(matrix[y][x], True, (255,0,0))


        rectangle = pygame.Rect(box_x, box_y, size-5, size-5)

        pygame.draw.rect(screen, (255,255,255), rectangle)
        screen.blit(img2, (box_x+10, box_y))

        return rectangle











# functions for every sudoku oriented function
class SudokuFunctions:


    # creates new sudoku matrix and returns it
    def createMatrix(self, procentage):
        sudoku_matrix = [[""] * 9 for _ in range(9)]

        for y in range(0, 9):
            for x in range(0, 9):
                if random.randint(0, 10) <= procentage:
                    aviable = self.checkAviable(y, x, sudoku_matrix)

                    if not aviable:
                        sudoku_matrix[y][x] = ""
                    else:
                        sudoku_matrix[y][x] = random.choice(aviable)

        return sudoku_matrix


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