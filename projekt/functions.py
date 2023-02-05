import random
import time
import pygame


# functions for drawing on screeen
class DrawingFunctions:
    def drawBox(self, y, x, screen, matrix, size, font):
        # calculates the starting cordinates of each square and draws it
        box_x = size * x + 5
        box_y = size * y + 5
        img2 = font.render(matrix[y][x], True, (255,0,0))

        pygame.draw.rect(screen, (255,255,255), pygame.Rect(box_x, box_y, size-5, size-5))
        screen.blit(img2, (box_x+10, box_y))


    def drawMatrix(self, screen, matrix, size, font):
        for y in range(0, 9):
            for x in range(0, 9):
                self.drawBox(y, x, screen, matrix, size, font)



# functions for every sudoku oriented function
class SudokuFunctions:
    def __init__(self, screen):
        self.screen = screen


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



    def clicked_box(self, y, x, matrix, size, font):
        start_x = 700
        start_y = 400

        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(start_x, start_y, 200, 200))
        aviable = self.checkAviable(y, x, matrix)

        pos_x = 0
        pos_y = 0

        for item in aviable:
            kms_x = start_x+5+pos_x*size
            kms_y = start_y+5+pos_y*size
            
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(kms_x, kms_y, size-5, size-5))

            number = font.render(item, True, (255,0,0))
            self.screen.blit(number, (kms_x+5, kms_y+5))

            pos_x += 1
            if pos_x % 3 == 0:
                pos_y += 1
                pos_x = 0

    def solve_sudoku(self, matrix):
        def solve(y, x):
            if matrix[y][x] == "":
                aviable = self.checkAviable(y, x, matrix)

                for item in aviable:
                    matrix[y][x] = item

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
                
            if matrix[y][x] == "":
                return False
            else:
                return True
        
        print(solve(0,0))
        return matrix



# pos_x = start_x+5+size*j
# pos_y = start_y+5+size*(i // 3)

# pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(pos_x, pos_y, size-5, size-5))