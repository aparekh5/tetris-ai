import typing
import pygame
rotations = [
    [[(1, 0), (1, 1), (1, 2), (1, 3)], [(0, 1), (1, 1), (2, 1), (3, 1)]], # line
    [[(1, 0), (2, 0), (1, 1), (2, 1)]], # block
    [[(1, 0), (1, 1), (2, 1), (1, 2)], [(0, 1), (1, 1), (2, 1), (1, 2)], [(1, 0), (0, 1), (1, 1), (1, 2)], [(1, 0), (0, 1), (1, 1), (2, 1)]] ,
    [[(1, 0), (2, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)], ],
    [[(0, 0), (1, 0), (1, 1), (2, 1)], [(1, 0), (0, 1), (1, 1), (0, 2)]]
]
colors = [(242, 107, 17), (80, 200, 120), (199, 0, 57), (255, 234, 0), (0,191,255)]

class Blocks:
    def __init__(self, block_type: int, start_pos:typing.Tuple[int, int]= (0, 0), block_size=40):
        self.block_type = block_type
        self.rotation = 0
        self.block_size = block_size
        self.rotations = rotations[block_type]
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.rectangles = []
        for i in self.rotations[self.rotation%len(self.rotations)]:
            size = (self.block_size, self.block_size)
            x_left = (self.x+(i[0]*self.block_size))
            y_down = self.y+(i[1]*self.block_size)
            self.rectangles.append(pygame.Rect((x_left, y_down), size))
    
    def render(self, screen):
        for r in self.rectangles:
            pygame.draw.rect(screen, colors[self.block_type], r, width=0)
    
    def rotate(self, board):
        self.rotation+=1
        new_rotation = self.rotations[self.rotation%len(self.rotations)]

        newRects = []
        size = (self.block_size, self.block_size)
        for i in range(0, 4):
            x_left = (self.x+new_rotation[i][0])*self.block_size
            y_down = (self.y+new_rotation[i][1])*self.block_size
            newRects.append(pygame.Rect((x_left, y_down), size))
        if board.check_collision(newRects):
            self.rotation -=1
            return
        else: 
            self.rectangles = newRects
    def down(self):
        self.y+=1
        for rect in self.rectangles:
            rect.move_ip(0, self.block_size)
   
   
    def left(self, board):
        self.x-=1
        newRects = []

        for rect in self.rectangles:
            newRects.append(rect.move(0-self.block_size, 0))
        if not board.check_collision(newRects):
            self.rectangles = newRects



    def right(self, board):
        self.x-=1
        newRects = []
        for rect in self.rectangles:
            newRects.append(rect.move(0+self.block_size, 0))
        if not board.check_collision(newRects):
            self.rectangles = newRects