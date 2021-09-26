import random, copy

import pygame
from pygame.constants import RESIZABLE

# Grid dimensions
WIDTH = 120
HEIGHT = WIDTH
speciescount = 2

def GenerateBoard():
    '''
    Get first list of values
    '''

    # Nested list of cells
    board = []
    extras = 25 ###### Extra random numbers for board seed to generate more blanks
    for x in range(WIDTH):
        row = []
        for y in range(HEIGHT):
            # Determine if cell is alive or dead randomly
            ran = random.randint(0,(speciescount+extras))
            if ran == 0:
                row.append(' ')  # dead
            elif ran == 1:
                row.append('1')  # 1
            elif ran == 2:
                row.append('2')
            # Extra spacing to start more seperate
            else:
                row.append(' ')

        board.append(row)
    
    return board

class Species:

    # Shared board among instances of the Species class
    board = GenerateBoard()
    nextboard = []

    def __init__(self, type):
        self.breed = type # corresponds to number of species.... '1','2','3',...

    def Cycle(self):
        '''
        One iteration of game of life
        '''

        Species.nextboard = copy.deepcopy(Species.board)
        
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # Get neigboring coordinates:
                # % WIDTH maintains within bounds
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y + 1) % HEIGHT
                belowCoord = (y - 1) % HEIGHT

                # Count living neigbors
                numNeigbors = 0
                if Species.nextboard[leftCoord][aboveCoord] == self.breed or Species.nextboard[leftCoord][aboveCoord] != ' ':   # top left
                    numNeigbors += 1
                if Species.nextboard[x][aboveCoord] == self.breed or Species.nextboard[x][aboveCoord] != ' ':                   # top
                    numNeigbors += 1
                if Species.nextboard[rightCoord][aboveCoord] == self.breed or Species.nextboard[rightCoord][aboveCoord] != ' ': # top right
                    numNeigbors += 1
                if Species.nextboard[leftCoord][y] == self.breed or Species.nextboard[leftCoord][y] != ' ':                     # left coord
                    numNeigbors += 1
                if Species.nextboard[rightCoord][y] == self.breed or Species.nextboard[rightCoord][y] != ' ':                   # right coord
                    numNeigbors += 1
                if Species.nextboard[leftCoord][belowCoord] == self.breed or Species.nextboard[leftCoord][belowCoord] != ' ':   # bottom left
                    numNeigbors += 1
                if Species.nextboard[x][belowCoord] == self.breed or Species.nextboard[x][belowCoord] != ' ':                   # below
                    numNeigbors += 1
                if Species.nextboard[rightCoord][belowCoord] == self.breed or Species.nextboard[rightCoord][belowCoord] != ' ': # bottom right
                    numNeigbors += 1


                # Determine space remains alive

                # Stay alive
                if Species.nextboard[x][y] == self.breed and (numNeigbors == 2 or numNeigbors == 3):
                    # Same species with 2 or 3 neigbors stay alive
                    Species.nextboard[x][y] == self.breed

                # Come to Life
                elif Species.nextboard[x][y] == ' ' and numNeigbors == 3:
                    # Dead cells with 3 same neigbors come alive
                    Species.nextboard[x][y] = self.breed

                # Over or UnderCrowding
                elif numNeigbors > 3 or numNeigbors <= 1:
                    # If the number of neigbors is more than 3 or less than one for any species, die
                    Species.nextboard[x][y] = ' '

                # Set board for next iteration
                Species.board = Species.nextboard



if __name__ == "__main__":

    # Give 2 species tags '1' and '2'
    redbois = Species('1')
    bluebois = Species('2')

    # Board constants
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    LITERED = (150, 0, 150)
    GREEN = (0, 255, 0)
    BLUE  = (0, 0, 255)
    MARGIN = 1
    # Square sizes
    sq_wid = 5
    sq_ht = sq_wid

    # Display Size
    dispWidth = WIDTH*(sq_wid + MARGIN) + MARGIN
    dispHeight = HEIGHT*(sq_ht +MARGIN) + MARGIN

    # Generate board
    pygame.init()
    screen = pygame.display.set_mode((dispWidth, dispHeight), RESIZABLE)
    pygame.display.set_caption("Game of Lives")
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Cycling loop
    running = True
    while running:
        
        # Fill screen with black
        screen.fill(BLACK)

        # Iterate through 1 generation
        redbois.Cycle()
        bluebois.Cycle()

        # Stop if you close the window
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  # If user clicked close
                running = False

        # Animate the screen
        for row in range(WIDTH):
            for col in range(HEIGHT):
                color = BLACK
                # Color in squares
                # Red
                if Species.board[row][col] == '1':
                    color = LITERED
                    pygame.draw.rect( screen, color, [(MARGIN + sq_wid) * col + MARGIN,
                                                    (MARGIN + sq_ht) * row + MARGIN,
                                                    sq_wid, sq_ht] )
                # Blue
                elif Species.board[row][col] == '2':
                    color = BLUE
                    pygame.draw.rect( screen, color, [(MARGIN + sq_wid) * col + MARGIN,
                                                    (MARGIN + sq_ht) * row + MARGIN,
                                                    sq_wid, sq_ht] )
        # Set framerate and update
        clock.tick(20)
        pygame.display.flip()

    # Quit when finished
    pygame.quit()
