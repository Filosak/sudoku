import pygame
import random
import time
from functions import SudokuFunctions
from functions import DrawingFunctions

# setting up pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('test caption')
window = pygame.display.set_mode((1000, 600))
window.fill((255, 255, 255))


# variables
SFunctions = SudokuFunctions(window)
font = pygame.font.SysFont("calibri", 72)
run = True
width = 1000
height = 600
block_size = (width-400) // 9
chance = 6
sudoku_matrix = SFunctions.createMatrix(chance)
DFunctions = DrawingFunctions(font, block_size)
curr_rectangles = []


# draws the sudoku on screen
pygame.draw.rect(window, (0,0,0), pygame.Rect(0, 0, 600, 600))
DFunctions.drawMatrix(window, sudoku_matrix)

# draws all buttons on screen
reset_button = pygame.Rect(700, 100, 200, 100)
pygame.draw.rect(window, (0,0,0), reset_button)
window.blit(font.render("Reset", True, (255,0,0)), (720, 120))

solve_button = pygame.Rect(700, 250, 200, 100)
pygame.draw.rect(window, (0,0,0), solve_button)
window.blit(font.render("Solve", True, (255,0,0)), (720, 270))



# to do
# find a way to check what square is clicked and its y and x possition in matrix so we can
# change it after user chose what number to put in


pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()

            if y // block_size < 9 and x // block_size < 9:
                curr_rectangles = SFunctions.clicked_box(y // block_size, x // block_size, sudoku_matrix, block_size, font)


            if reset_button.collidepoint(x, y) == True:
                sudoku_matrix = SFunctions.createMatrix(chance)
                DFunctions.drawMatrix(window, sudoku_matrix)

            
            if solve_button.collidepoint(x, y) == True:
                SFunctions.solve_sudoku(sudoku_matrix, font, block_size)


            for rect, num in curr_rectangles[1:]:
                if rect.collidepoint(x, y) == True:
                    curr_y = curr_rectangles[0][0]
                    curr_x = curr_rectangles[0][1]


                    sudoku_matrix[curr_y][curr_x] = num
                    DFunctions.drawBox(curr_y, curr_x, window, sudoku_matrix, (255,0,0))




            pygame.display.update()

pygame.quit()