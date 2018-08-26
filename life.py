import sys
import random
import time
import os
from ctypes import *

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]

def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

    c = s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)


#Variables
width = 10
height = 10
itter = 0
x = 0
#

#algorythm for the grid, using 2d array
class Habitat:
    def __init__(self,h,w):
        self.grid = []
        for i in range(h):
            self.grid.append(0)
        i = 0
        for i in range(h):
            self.grid[i] = [0]*w
    def show(self):
        global height
        i = 0
        print_at(2,0,"")
        for i in range(height):
            print(self.grid[i])

    def population(self,h,w):
        for i in range(h):
            for j in range(w):
                if i%2 == 0:
                    if j%2==0:
                        self.grid[i][j] = 1
                else:
                    if j%2 != 0:
                        self.grid[i][j] = 1
    def life_death(self,h,w):
        x = 0
        i = 0
        j = 0
        for i in range(h):
            for j in range(w):
                if self.grid[i][j] == 1:
                    x = x + 1
        return x
#
arena = Habitat(height,width)

class Organizm:
    def __init__(self,h,w):
        self.state = []
        self.n = 0
        for i in range(h):
            self.state.append(0)
        i = 0
        for i in range(h):
            self.state[i] = [0]*w

#grid changed to arena.grid
    def samathi(self,h,w):
        i = 0
        for i in range(h):
            j = 0
            for j in range(w):
                if arena.grid[i][j] == 1:
                    self.state[i][j] = "alive"
                else:
                    self.state[i][j] = "dead"

    def evolution(self,h,w):
        global itter
        global x
        i = 0
        for i in range(h):
            j = 0
            for j in range(w):
                if self.state[i][j] == "alive":
                    self.neighbours(i,j)
                    if self.n == 2 or self.n == 3 :
                        continue
                    elif (self.n < 2) or (self.n > 3):
                        arena.grid[i][j] = 0
                elif self.state[i][j] == "dead":
                    self.neighbours(i,j)
                    if self.n == 3:
                        arena.grid[i][j] = 1

#some code changed to function

        arena.show()
        self.samathi(h,w)
        time.sleep(0.2)
        if arena.grid == x:
            sys.exit()
        x = [[j for j in i] for i in arena.grid]
        itter += 1
        if itter == 80:
            sys.exit()
        self.evolution(h,w)

    def neighbours(self,h,w):
        global height
        global width
        self.n = 0
########
        if (h == 0 or h == height-1) and (w == 0 or w == width-1) :
            if h==0 and w==0:
                for i in range(h,h+2):
                    for j in range(w,w+2):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
            elif h==0 and w==width-1 :
                for i in range(h,h+2):
                    for j in range(w-1,w+1):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
            elif h==height-1 and w==0:
                for i in range(h-1,h+1):
                    for j in range(w,w+2):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
            elif h==height-1 and w==width-1:
                for i in range(h-1,h+1):
                    for j in range(w-1,w+1):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
########
        elif  (w == 0 or w == width-1) and (h != 0 or h != height-1):
            if w == 0:
                for i in range(h-1,h+2):
                    for j in range(w,w+2):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
            elif w == width-1:
                for i in range(h-1,h+2):
                    for j in range(w-1,w+1):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
        
########
        elif (h == 0 or h == height-1) and (w != 0 or w != width - 1):
            if h == 0:
                for i in range(h,h+2):
                    for j in range(w-1,w+2):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
            elif h == height-1:
                for i in range(h-1,h+1):
                    for j in range(w-1,w+2):
                        if i == h and j == w:
                            continue
                        else:
                            if self.state[i][j] == "alive":
                                self.n = self.n + 1
########
        else:
            for i in range(h-1,h+2):
                for j in range(w-1,w+2):
                    if i == h and j == w:
                        continue
                    else:
                        if self.state[i][j] == "alive":
                            self.n = self.n + 1

arena.grid[0][0] = 1
arena.grid[0][2] = 1
arena.grid[1][2] = 1
arena.grid[1][1] = 1
arena.grid[2][1] = 1
#arena.population(height,width)
arena.show()
cell = Organizm(height,width)
cell.samathi(height,width)
cell.evolution(height,width)
