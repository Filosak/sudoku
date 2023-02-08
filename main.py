# import of libraries
import pygame
import random
import time


# import of every needed functions from functions.py
from functions import SudokuFunctions
from functions import DrawingFunctions


# setting up pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('test caption')
window = pygame.display.set_mode((1000, 610))
window.fill((255, 255, 255))


# variables
SFunctions = SudokuFunctions(window)
font = pygame.font.SysFont("calibri", 72)
run = True
width = 1000
height = 615
block_size = (width-400) // 9
sudoku_matrix = SFunctions.createMatrix()
original_matrix = [row[:] for row in sudoku_matrix]
DFunctions = DrawingFunctions(font, block_size)
curr_rectangles = []
active = None


# draws the sudoku on screen
pygame.draw.rect(window, (0,0,0), pygame.Rect(0, 0, 610, 615))
DFunctions.drawMatrix(window, sudoku_matrix)

# draws all buttons on screen
reset_button = pygame.Rect(700, 100, 200, 100)
pygame.draw.rect(window, (0,0,0), reset_button)
window.blit(font.render("Reset", True, (255,0,0)), (720, 120))

solve_button = pygame.Rect(700, 250, 200, 100)
pygame.draw.rect(window, (0,0,0), solve_button)
window.blit(font.render("Solve", True, (255,0,0)), (720, 270))

pygame.display.update()



# game
while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            pos_y = y // block_size
            pos_x = x // block_size

            # if user left clicks
            if event.button == 1:
                
                # checks if the click happened inside the board
                if pos_y < 9 and pos_x < 9:
                    # checks if the number is from the user or it was there initialy
                    if original_matrix[pos_y][pos_x] == "":
                        # if any other square is selected it will be changed to white again
                        if active:
                            DFunctions.drawBox(active[1], active[0], window, sudoku_matrix, (255,0,0), (255,255,255))

                        # active square is changed and re-colored
                        active = [pos_x, pos_y]    
                        DFunctions.drawBox(pos_y, pos_x, window, sudoku_matrix, (255,0,0), (0,0,255))
                        curr_rectangles = SFunctions.clicked_box(pos_y, pos_x, sudoku_matrix, block_size, font)


                # checks if user clicked on the reset button
                elif reset_button.collidepoint(x, y) == True:
                    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(700, 400, block_size*3+5, block_size*3))
                    
                    # changes every variable so it matches to the new matrix
                    sudoku_matrix = SFunctions.createMatrix()
                    DFunctions.drawMatrix(window, sudoku_matrix)
                    original_matrix = [row[:] for row in sudoku_matrix]
                    active = None
                    
                
                # checks if the solve button is being clicked
                elif solve_button.collidepoint(x, y) == True:
                    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(700, 400, block_size*3+5, block_size*3))
                    SFunctions.solve_sudoku(sudoku_matrix, font, block_size)


                # checks if user is clicking on eny of the aviable numbers 
                for rect, num in curr_rectangles[1:]:
                    if rect.collidepoint(x, y) == True:
                        curr_y = curr_rectangles[0][0]
                        curr_x = curr_rectangles[0][1]

                        sudoku_matrix[curr_y][curr_x] = num
                        DFunctions.drawBox(curr_y, curr_x, window, sudoku_matrix, (255,0,0))

            # checks if user is right clicking
            elif event.button == 3:
                if pos_y < 9 and pos_x < 9:
                    if original_matrix[pos_y][pos_x] == "":

                        sudoku_matrix[pos_y][pos_x] = ""
                        DFunctions.drawBox(pos_y, pos_x, window, sudoku_matrix, (255,0,0), (255,255,255))

            # updates window after any change
            pygame.display.update()
            
# ends the window when user clicks esc
pygame.quit()



