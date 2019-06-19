#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:28:50 2019

@author: saeed
"""

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
    
myMap = [
  [1, 1, 1, 1, 1],
  [1, 1, 2, 1, 1],
  [1, 2, 0, 2, 1],
  [1, 1, 2, 1, 1],
  [1, 1, 2, 1, 1],
  [1, 2, 0, 2, 1],
  [1, 1, 2, 1, 1],
  [1, 1, 1, 1, 1]
]

'''
Visualizing the Map
'''
# create discrete colormap
cmap = colors.ListedColormap(['red', 'white', 'orange'])
bounds = [0,1,2,3]
# show the map
fig, ax = plt.subplots()
ax.imshow(myMap, cmap=cmap)


'''
Initializing the grid
'''
grid = Grid(matrix=myMap)
start = grid.node(1, 1)
end = grid.node(4, 7)


'''
Finding a good path
'''
finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)


'''
Plotting the path on the map
'''
x = [ x[0] for x in path]
y = [ y[1] for y in path]
ax.plot(x, y, 'c', linewidth=2)
ax.plot(x[0], y[0], 'go')
ax.plot(x[-1], y[-1], 'ro')

