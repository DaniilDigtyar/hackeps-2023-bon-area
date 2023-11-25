def euclidean_distance(matrix1, matrix2):
    return ((matrix1[0] - matrix2[0])**2 + (matrix1[1] - matrix2[1])**2)**0.5

def find_closest_matrix(target_matrix, matrix_set):
    min_distance = float('inf')
    closest_matrix = None

    for matrix in matrix_set:
        distance = euclidean_distance(target_matrix, matrix)
        if distance < min_distance:
            min_distance = distance
            closest_matrix = matrix

    return closest_matrix

# Ejemplo de uso
target_matrix = [3, 0]
matrix_set = [[0, 2], [0, 0], [2, 3], [0, 2]]

closest_matrix = find_closest_matrix(target_matrix, matrix_set)
print("La matriz más cercana es:", closest_matrix)