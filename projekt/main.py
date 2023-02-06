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
DFunctions = DrawingFunctions(font)
run = True
width = 1000
height = 600
block_size = (width-400) // 9
chance = 2
sudoku_matrix = SFunctions.createMatrix(chance)




# draws the sudoku on screen
pygame.draw.rect(window, (0,0,0), pygame.Rect(0, 0, 600, 600))
DFunctions.drawMatrix(window, sudoku_matrix, block_size)

# draws all buttons on screen
reset_button = pygame.Rect(700, 100, 200, 100)
pygame.draw.rect(window, (0,0,0), reset_button)
window.blit(font.render("Reset", True, (255,0,0)), (720, 120))

solve_button = pygame.Rect(700, 250, 200, 100)
pygame.draw.rect(window, (0,0,0), solve_button)
window.blit(font.render("Solve", True, (255,0,0)), (720, 270))



# to do
# focus
# board creation change to that it creates already solved sudoku and just deltes few number
# so theres 100% of solvable sudoku

# find a way to check what square is clicked and its y and x possition in matrix so we can
# change it after user chose what number to put in

# way to visualiaze the sudoku solver algorithm

# way to find a difference between set numbers from the start and the numbers user put in


pygame.display.update()
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()

            if y // block_size < 9 and x // block_size < 9:
                SFunctions.clicked_box(y // block_size, x // block_size, sudoku_matrix, block_size, font)
                pygame.display.update()

            if reset_button.collidepoint(x, y) == True:
                sudoku_matrix = SFunctions.createMatrix(chance)
                DFunctions.drawMatrix(window, sudoku_matrix, block_size)
                pygame.display.update()
            
            if solve_button.collidepoint(x, y) == True:
                SFunctions.solve_sudoku(sudoku_matrix, font, block_size)
                pygame.display.update()

pygame.quit()
