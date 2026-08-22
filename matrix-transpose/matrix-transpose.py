import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    A = np.asarray(A)
    row, col = np.shape(A)
    trans = np.zeros((col, row))

    for r in range(row):
        for c in range(col):
            trans[c][r] = A[r][c]

    return trans
    
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    pass
