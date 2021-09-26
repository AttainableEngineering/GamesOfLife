# Connway's Game of Life
import random, copy

import pygame
from pygame.constants import RESIZABLE

# Grid dimensions
WIDTH = 120
HEIGHT = WIDTH

# Board constants
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LITEBLUE = (0, 100, 200)

MARGIN = 1
# Square sizes
sq_wid = 5
sq_ht = sq_wid

# Display Size
dispWidth = WIDTH*(sq_wid + MARGIN) + MARGIN
dispHeight = HEIGHT*(sq_ht +MARGIN) + MARGIN

# Create screen
pygame.init()
screen = pygame.display.set_mode((dispWidth, dispHeight), RESIZABLE)
pygame.display.set_caption("Game of Life")
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#clock.tick(120)

# Looping condition
done = False

# Nested list of cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        # Determine if cell is alive or dead randomly
        if random.randint(0,1) == 0:
            column.append('#')  # alive
        else:
            column.append(' ')  # dead
    nextCells.append(column)

# Game loop
while not done:

    screen.fill(BLACK)
    
    # End game if you press close
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  # If user clicked close
            done = True

    for row in range(WIDTH):
        for col in range(HEIGHT):
            color = BLACK
            if nextCells[row][col] == '#':
                color = GREEN # adjust square color
            # Animate green squares
            pygame.draw.rect( screen, color, [(MARGIN + sq_wid) * col + MARGIN,
                                            (MARGIN + sq_ht) * row + MARGIN,
                                            sq_wid, sq_ht] )
    # Set clock time and update screen
    clock.tick(20) 
    pygame.display.flip()

    # Make a copy of the cells to use
    currentCells = copy.deepcopy(nextCells)

    # Calculate next step's cells based on current cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neigboring coords:
            # % WIDTH maintains within bounds
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y + 1) % HEIGHT
            belowCoord = (y - 1) % HEIGHT

            # Count living neigbors
            numNeigbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':    # top left
                numNeigbors += 1
            if currentCells[x][aboveCoord] == '#':            # top
                numNeigbors += 1
            if currentCells[rightCoord][aboveCoord] == '#':   # top right
                numNeigbors += 1
            if currentCells[leftCoord][y] == '#':             # left coord
                numNeigbors += 1
            if currentCells[rightCoord][y] == '#':            # right coord
                numNeigbors += 1
            if currentCells[leftCoord][belowCoord] == '#':    # bottom left
                numNeigbors += 1
            if currentCells[x][belowCoord] == '#':            # below
                numNeigbors += 1
            if currentCells[rightCoord][belowCoord] == '#':   # bottom right
                numNeigbors += 1

            # Set cell based on Conway's game of life rules
            if currentCells[x][y] == '#' and (numNeigbors == 2 or numNeigbors == 3):
                # Living cells with 2 or 3 neigbors stay alive
                nextCells[x][y] == '#'
            elif currentCells[x][y] == ' ' and numNeigbors == 3:
                # Dead cells with 3 neigbors become alive
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead
                nextCells[x][y] = ' '

# Quit when finished
pygame.quit()