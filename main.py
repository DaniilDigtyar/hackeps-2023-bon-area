from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import AStarFinder
from python_tsp.exact import solve_tsp_dynamic_programming
import numpy as np
from python_tsp.heuristics import solve_tsp_local_search

productos = [(4,0), (0,0), (0,2), (3,2)]

matrix = [
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
]

grid = Grid(matrix=matrix)

distanceMatrixArray = []
startingPointPermutation= []

for i in range(len(productos)):
    productDistances = []
    itemToCalculate = productos[i]
    for x in range(len(productos)):
        if i == x:
            productDistances.append(0)
            continue
        start = grid.node(productos[i][1], productos[i][0])
        end = grid.node(productos[x][1], productos[x][0])
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        print(start)
        print(end)
        print(grid)
        path, runs = finder.find_path(start, end, grid)
        print('operations:', runs, 'path length:', len(path))
        print(grid.grid_str(path=path, start=start, end=end))
        productDistances.append(len(path)-1)
        grid.cleanup()

    distanceMatrixArray.append(productDistances)

print(distanceMatrixArray)

distance_matrix = np.array(distanceMatrixArray)
distance_matrix[:, 0] = 0
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

print(permutation)
print(distance)       

for i in range(len(productos)):
    start = grid.node(0,4)
    end = grid.node(productos[i][1], productos[i][0])
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    startingPointPermutation.append(len(path)-1)
    grid.cleanup()

permutation, distance = solve_tsp_local_search(distance_matrix, [0,1,2,3])

print(permutation)
print(distance)