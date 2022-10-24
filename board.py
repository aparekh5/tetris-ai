import pygame
from typing import Tuple 
from blocks import Blocks

black = 0, 0, 0

class Board:
    def __init__(self, size: Tuple[int, int] = (10, 18), block_size:int =40):
        self.screen = pygame.display.set_mode((size[0]*block_size, size[1]*block_size))
        self.filled =[[False for j in range(0, size[1])] for i in range(0, size[0])]
        self.screen.fill(black)
        self.block_size = block_size
        self.frozenBlocks = []
        self.blocksDict = {}

    def render(self):
        self.screen.fill(black)
        for b in self.frozenBlocks:
            b.render(self.screen)
        
    def check_collision(self, rectangles):
        hasCollision = False
        for rect in rectangles:
            x = int(rect.x / self.block_size) 
            y = int(rect.y / self.block_size) 
            if (x >= len(self.filled) or y >= len(self.filled[0])) or (x < 0 or y <0) :
                hasCollision = True
                break 
            if self.filled[x][y]:
                hasCollision =  True
                break

        return hasCollision
        
    # def check_left_collision(self, b:Blocks):
    #     hasCollision = False
    #     for rect in b.rectangles:
    #         x = int(rect.x / self.block_size) -1
    #         y = int(rect.y / self.block_size) 
    #         if (x >= len(self.filled) or y >= len(self.filled[0])) or (x < 0 or y <0) :
    #             hasCollision = True
    #             break 
    #         if self.filled[x][y]:
    #             hasCollision =  True
    #             break

    #     return hasCollision
    
    # def check_right_collision(self, b:Blocks):
    #     hasCollision = False
    #     for rect in b.rectangles:
    #         x = int(rect.x / self.block_size)  +1
    #         y = int(rect.y / self.block_size)
    #         if (x >= len(self.filled) or y >= len(self.filled[0])) or (x < 0 or y <0) :
    #             hasCollision = True
    #             break 
    #         if self.filled[x][y]:
    #             hasCollision =  True
    #             break
        
    #     return hasCollision

    def check_block_collision(self, b:Blocks):
        hasCollision = False
        for rect in b.rectangles:
            x = int(rect.x / self.block_size)  
            y = int(rect.y / self.block_size) + 1
            if (x >= len(self.filled) or y >= len(self.filled[0])) or (x < 0 or y <0) :
                hasCollision = True
                break 
            if self.filled[x][y]:
                hasCollision =  True
                break
        
        if hasCollision:
            self.frozenBlocks.append(b)
        else:
            return False
        for rect in b.rectangles:
            x = int(rect.x / self.block_size)
            y = int(rect.y / self.block_size)
            self.filled[x][y] = True
        return True

        