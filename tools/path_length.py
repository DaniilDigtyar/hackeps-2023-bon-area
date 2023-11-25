from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

def get_path_length(matrix, start_coords, end_coords):
    grid = Grid(matrix=matrix)
    start = grid.node(*start_coords)
    end = grid.node(*end_coords)
    
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)
    
    longitud_path = len(path)
    return longitud_path

# Ejemplo de uso:
matrix_ejemplo = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

start_coords_ejemplo = (0, 0)
end_coords_ejemplo = (2, 2)

longitud_path_ejemplo = calcular_longitud_path(matrix_ejemplo, start_coords_ejemplo, end_coords_ejemplo)
print("Longitud del path:", longitud_path_ejemplo)
