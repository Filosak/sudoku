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
SFunctions = SudokuFunctions()
DFunctions = DrawingFunctions()
font = pygame.font.SysFont(None, 24)
run = True
width = 1000
height = 600
sudoku_matrix = SFunctions.createMatrix(3)
rectangle_pos = []



# draws the sudoku on screen
pygame.draw.rect(window, (0,0,0), pygame.Rect(0, 0, 600, 600))

for y in range(0, 9):
    for x in range(0, 9):
        rectangle_pos.append(DFunctions.drawBox(y, x, width-400, window, sudoku_matrix))
pygame.display.update()

print(rectangle_pos)



# to do
# find a way to check what square is clicked and its y and x possition in matrix so we can
# change it after user chose what number to put in

# button for resseting the suddoku board and matrix

# way to visualiaze the sudoku solver algorithm
# button for solving

# way to find a difference between set numbers from the start and the numbers user put in






while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

pygame.quit()


# pygame.draw.rect(window, (255,255,255), pygame.Rect(30, 30, 60, 60))