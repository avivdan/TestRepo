def normalize(lst: list):
    s = sum(lst)
    return [round(100 * i / s, 2) for i in lst]


def bundle_to_matrix(allocation):
    return tuple_matrix_to_matrix([list(bundle.enumerate_fractions()) for bundle in allocation])


def tuple_matrix_to_matrix(matrix):
    return [[0 if tup[1]==-0.0 else tup[1] for tup in matrix[i]] for i in range(len(matrix))]


def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]