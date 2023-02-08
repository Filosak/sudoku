import pygame
import random
import time
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


# functions






# game
while run:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()

            if y // block_size < 9 and x // block_size < 9:
                pls_y = y // block_size
                pls_x = x // block_size
                
                if original_matrix[pls_y][pls_x] == "":
                    if active:
                        DFunctions.drawBox(active[1], active[0], window, sudoku_matrix, (255,0,0), (255,255,255))
                    active = [pls_x, pls_y]    
                    DFunctions.drawBox(pls_y, pls_x, window, sudoku_matrix, (255,0,0), (0,0,255))

                    curr_rectangles = SFunctions.clicked_box(pls_y, pls_x, sudoku_matrix, block_size, font)


            elif reset_button.collidepoint(x, y) == True:
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(700, 400, block_size*3+5, block_size*3))

                sudoku_matrix = SFunctions.createMatrix()
                DFunctions.drawMatrix(window, sudoku_matrix)
                original_matrix = [row[:] for row in sudoku_matrix]
                active = None
                
            
            elif solve_button.collidepoint(x, y) == True:
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(700, 400, block_size*3+5, block_size*3))
                SFunctions.solve_sudoku(sudoku_matrix, font, block_size)


            for rect, num in curr_rectangles[1:]:
                if rect.collidepoint(x, y) == True:
                    curr_y = curr_rectangles[0][0]
                    curr_x = curr_rectangles[0][1]


                    sudoku_matrix[curr_y][curr_x] = num
                    DFunctions.drawBox(curr_y, curr_x, window, sudoku_matrix, (255,0,0))
                    
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = pygame.mouse.get_pos()

            if y // block_size < 9 and x // block_size < 9:
                del_y = y // block_size
                del_x = x // block_size
                
                if original_matrix[del_y][del_x] == "":
                    sudoku_matrix[del_y][del_x] = ""
                    DFunctions.drawBox(del_y, del_x, window, sudoku_matrix, (255,0,0), (255,255,255))
                    pygame.display.update()
            

pygame.quit()