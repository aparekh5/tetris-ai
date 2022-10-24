import sys, pygame
import time
from blocks import  Blocks
from board import Board
import random
pygame.init()


# 10, 24
size = width, height = 400, 960
speed = [0, 40]
black = 0, 0, 0
white = 255, 255, 255


board = Board()
block = Blocks(0)

clock = pygame.time.Clock()
block.render(board.screen)
ticker = 1
while 1:
    ticker += 1
    # speed = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: block.rotate(board)
            if event.key == pygame.K_LEFT:
                block.left(board)
            if event.key == pygame.K_RIGHT:
                block.right(board)
            if event.key == pygame.K_DOWN:             
                if not board.check_block_collision(block):
                    board.render()
                    block.down()
                    block.render(board.screen)


    if ticker % 12 == 0:
        if not board.check_block_collision(block):
            board.render()

            block.down()
            block.render(board.screen)
            # board.render()
        else: 
            block = Blocks(random.randint(0, 4))

    # board.render()
    # block.rotate()
    # pygame.draw.polygon(board.screen, *block.get() )
    pygame.display.flip()
    clock.tick(25)
