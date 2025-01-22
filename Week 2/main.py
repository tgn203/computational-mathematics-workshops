"""
main.py
Thomas Noakes
2025
"""


def matrix_addition(mat_a: list, mat_b: list):
    """Add two matrices of the same dimensions"""

    # Ensure matrices are of the same dimensions
    dim_a = (len(mat_a), len(mat_a[0]))
    dim_b = (len(mat_b), len(mat_b[0]))
    if dim_a != dim_b:
        raise ValueError("Matrices must be of the same dimensions")

    # Create and fill the output matrix
    mat_ans: list = []
    for i, row in enumerate(mat_a):
        mat_ans.append([])
        for j in range(len(row)):
            mat_ans[i].append(mat_a[i][j] + mat_b[i][j])

    return mat_ans


def matrix_subtraction(mat_a: list, mat_b: list):
    """Subtract two matrices of the same dimensions"""

    # Ensure matrices are of the same dimensions
    dim_a = (len(mat_a), len(mat_a[0]))
    dim_b = (len(mat_b), len(mat_b[0]))
    if dim_a != dim_b:
        raise ValueError("Matrices must be of the same dimensions")

    # Create and fill the output matrix
    mat_ans: list = []
    for i, row in enumerate(mat_a):
        mat_ans.append([])
        for j in range(len(row)):
            mat_ans[i].append(mat_a[i][j] - mat_b[i][j])

    return mat_ans


def matrix_scalar_multiplication(mat: list, scalar: float):
    """Multiply a matrix by a scalar"""

    # Create and fill the output matrix
    mat_ans: list = []
    for i, row in enumerate(mat):
        mat_ans.append([])
        for j in range(len(row)):
            mat_ans[i].append(mat[i][j] * scalar)

    return mat_ans


def matrix_multiplication(mat_a: list, mat_b: list):
    """Multiply two matrices of the correct dimensions"""

    # Ensure matrices are of the same dimensions
    dim_a = (len(mat_a), len(mat_a[0]))
    dim_b = (len(mat_b), len(mat_b[0]))
    if dim_a[1] != dim_b[0]:
        raise ValueError("Matrices must be of the correct dimensions")

    # Create and fill the output matrix
    mat_ans: list = []
    mat_ans = [[0 for _ in range(dim_b[1])] for _ in range(dim_a[0])]
    for r, row in enumerate(mat_a):
        for c, col in enumerate(mat_b[0]):
            for i, val in enumerate(row):
                mat_ans[r][c] += val * mat_b[i][c]

    return mat_ans


def matrix_determinant(mat: list):
    """Calculate the determinant of a 2x2 matrix"""

    # If the matrix is 2x2, calculate the determinant
    if len(mat) == 2 and len(mat[0]) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    # Larger matrices are not supported
    else:
        raise NotImplementedError("Matrices larger than 2x2 are not supported")


def dot_product(vec_a: list, vec_b: list):
    """Calculate the dot product of two vectors"""

    # Ensure vectors are of the same dimensions
    dim_a = len(vec_a)
    dim_b = len(vec_b)
    if dim_a != dim_b:
        raise ValueError("Vectors must be of the same dimensions")

    # Calculate the dot product
    dot_ans = 0
    for i in range(len(vec_a)):
        dot_ans += vec_a[i] * vec_b[i]

    return dot_ans


def cross_product(vec_a: list, vec_b: list):
    """Calculate the cross product of two vectors"""

    # Ensure both are 3D vectors
    dim_a = len(vec_a)
    dim_b = len(vec_b)
    if dim_a != 3 or dim_b != 3:
        raise ValueError("Vectors must be 3D")

    # Calculate the dot product
    cross_ans = [
        vec_a[1] * vec_b[2] - vec_a[2] * vec_b[1],
        vec_a[2] * vec_b[0] - vec_a[0] * vec_b[2],
        vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0],
    ]

    return cross_ans


def main():
    """
    Matrix and vector manipulation
    """

    # Matrix manipulation:
    a = [[6, -2], [-3, 5]]
    b = [[7, 1], [0, -3]]

    print("-" * 50)
    print(f"A = {a}")
    print(f"B = {b}")
    print("-" * 50)

    print(f"A + B = {matrix_addition(a, b)}")
    print(f"A - B = {matrix_subtraction(a, b)}\n")

    print(f"2A = {matrix_scalar_multiplication(a, 2)}")
    print(
        f"4A - 2B = {matrix_subtraction(
            matrix_scalar_multiplication(a, 4),
            matrix_scalar_multiplication(b, 2)
        )}\n"
    )

    print(f"A x B = {matrix_multiplication(a, b)}")
    print(f"B x A = {matrix_multiplication(b, a)}\n")

    print(f"det(A) = {matrix_determinant(a)}")

    # Vector manipulation:
    u = [-4, -7, 3]
    v = [6, -2, 5]
    q = [6, -7]

    print("-" * 50)
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"q = {q}")
    print("-" * 50)

    print(f"u * v = {dot_product(u, v)}")
    print(f"u x v = {cross_product(u, v)}")


if __name__ == "__main__":
    main()
